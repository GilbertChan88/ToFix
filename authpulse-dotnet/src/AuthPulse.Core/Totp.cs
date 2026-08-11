using System.Security.Cryptography;

namespace AuthPulse.Core;

/// <summary>Supported HMAC algorithms for TOTP.</summary>
public enum TotpAlgorithm
{
    Sha1,
    Sha256,
    Sha512
}

/// <summary>The generated one-time password plus its live timing metadata.</summary>
public sealed record TotpResult(
    string Code,
    int SecondsLeft,
    int Period,
    int Digits,
    string Algorithm);

/// <summary>Thrown when a secret or otpauth URI cannot be parsed.</summary>
public sealed class TotpException(string message) : Exception(message);

/// <summary>
/// RFC 6238 (TOTP) / RFC 4226 (HOTP) engine — the .NET counterpart of the
/// Python build's <c>totp.py</c>. Uses only <see cref="System.Security.Cryptography"/>;
/// no third-party packages. Nothing is persisted.
/// </summary>
public static class Totp
{
    private const string Base32Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";

    /// <summary>Generate the current TOTP for a Base32 <paramref name="secret"/>.</summary>
    public static TotpResult Generate(
        string secret,
        int digits = 6,
        int period = 30,
        TotpAlgorithm algorithm = TotpAlgorithm.Sha1,
        DateTimeOffset? at = null)
    {
        if (digits is < 6 or > 10)
            throw new TotpException("Digits must be between 6 and 10.");
        if (period <= 0)
            throw new TotpException("Period must be a positive number of seconds.");

        byte[] key = DecodeBase32(secret);

        long unixSeconds = (at ?? DateTimeOffset.UtcNow).ToUnixTimeSeconds();
        long counter = unixSeconds / period;

        // RFC 4226: HMAC over the 8-byte big-endian counter.
        Span<byte> message = stackalloc byte[8];
        for (int i = 7; i >= 0; i--)
        {
            message[i] = (byte)(counter & 0xFF);
            counter >>= 8;
        }

        byte[] hash = ComputeHmac(algorithm, key, message.ToArray());

        // Dynamic truncation (RFC 4226 §5.3).
        int offset = hash[^1] & 0x0F;
        int binary =
            ((hash[offset] & 0x7F) << 24) |
            ((hash[offset + 1] & 0xFF) << 16) |
            ((hash[offset + 2] & 0xFF) << 8) |
            (hash[offset + 3] & 0xFF);

        int modulo = (int)Math.Pow(10, digits);
        string code = (binary % modulo).ToString().PadLeft(digits, '0');

        int secondsLeft = period - (int)(unixSeconds % period);

        return new TotpResult(code, secondsLeft, period, digits, algorithm.ToString().ToUpperInvariant());
    }

    /// <summary>Accept either a raw Base32 secret or a full <c>otpauth://</c> URI.</summary>
    public static TotpResult FromInput(string value)
    {
        value = (value ?? string.Empty).Trim();
        if (value.StartsWith("otpauth://", StringComparison.OrdinalIgnoreCase))
        {
            var p = ParseOtpAuth(value);
            return Generate(p.Secret, p.Digits, p.Period, p.Algorithm);
        }
        return Generate(value);
    }

    /// <summary>Parsed fields from an <c>otpauth://totp/...</c> URI.</summary>
    public sealed record OtpAuth(string Secret, int Digits, int Period, TotpAlgorithm Algorithm, string Label, string Issuer);

    public static OtpAuth ParseOtpAuth(string uri)
    {
        Uri parsed;
        try
        {
            parsed = new Uri(uri.Trim());
        }
        catch (UriFormatException)
        {
            throw new TotpException("Not a valid otpauth:// URI.");
        }

        if (!parsed.Scheme.Equals("otpauth", StringComparison.OrdinalIgnoreCase) ||
            !parsed.Host.Equals("totp", StringComparison.OrdinalIgnoreCase))
        {
            throw new TotpException("Not a valid otpauth://totp/ URI.");
        }

        var query = ParseQuery(parsed.Query);
        if (!query.TryGetValue("secret", out var secret) || string.IsNullOrWhiteSpace(secret))
            throw new TotpException("otpauth URI is missing the 'secret' parameter.");

        int digits = query.TryGetValue("digits", out var ds) && int.TryParse(ds, out var d) ? d : 6;
        int period = query.TryGetValue("period", out var ps) && int.TryParse(ps, out var p) ? p : 30;
        var algo = ParseAlgorithm(query.TryGetValue("algorithm", out var a) ? a : "SHA1");
        string label = Uri.UnescapeDataString(parsed.AbsolutePath.TrimStart('/'));
        string issuer = query.TryGetValue("issuer", out var iss) ? iss : string.Empty;

        return new OtpAuth(secret, digits, period, algo, label, issuer);
    }

    private static Dictionary<string, string> ParseQuery(string query)
    {
        var result = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        foreach (var pair in query.TrimStart('?').Split('&', StringSplitOptions.RemoveEmptyEntries))
        {
            int eq = pair.IndexOf('=');
            if (eq < 0)
                result[Uri.UnescapeDataString(pair)] = string.Empty;
            else
                result[Uri.UnescapeDataString(pair[..eq])] = Uri.UnescapeDataString(pair[(eq + 1)..]);
        }
        return result;
    }

    public static TotpAlgorithm ParseAlgorithm(string name) => name.Trim().ToUpperInvariant() switch
    {
        "SHA1" => TotpAlgorithm.Sha1,
        "SHA256" => TotpAlgorithm.Sha256,
        "SHA512" => TotpAlgorithm.Sha512,
        _ => throw new TotpException($"Unsupported algorithm '{name}'.")
    };

    private static byte[] ComputeHmac(TotpAlgorithm algorithm, byte[] key, byte[] message) => algorithm switch
    {
        TotpAlgorithm.Sha1 => HMACSHA1.HashData(key, message),
        TotpAlgorithm.Sha256 => HMACSHA256.HashData(key, message),
        TotpAlgorithm.Sha512 => HMACSHA512.HashData(key, message),
        _ => throw new TotpException("Unsupported algorithm.")
    };

    /// <summary>Decode an RFC 4648 Base32 string (spaces/hyphens/padding tolerated).</summary>
    public static byte[] DecodeBase32(string secret)
    {
        if (string.IsNullOrWhiteSpace(secret))
            throw new TotpException("Secret key is empty.");

        string cleaned = secret.Trim()
            .Replace(" ", "")
            .Replace("-", "")
            .ToUpperInvariant()
            .TrimEnd('=');

        if (cleaned.Length == 0)
            throw new TotpException("Secret key is empty.");

        var bytes = new List<byte>(cleaned.Length * 5 / 8);
        int buffer = 0;
        int bitsLeft = 0;

        foreach (char c in cleaned)
        {
            int val = Base32Alphabet.IndexOf(c);
            if (val < 0)
                throw new TotpException($"Secret contains a character that is not valid Base32: '{c}'.");

            buffer = (buffer << 5) | val;
            bitsLeft += 5;
            if (bitsLeft >= 8)
            {
                bitsLeft -= 8;
                bytes.Add((byte)((buffer >> bitsLeft) & 0xFF));
            }
        }

        if (bytes.Count == 0)
            throw new TotpException("Secret decoded to zero bytes.");

        return bytes.ToArray();
    }
}
