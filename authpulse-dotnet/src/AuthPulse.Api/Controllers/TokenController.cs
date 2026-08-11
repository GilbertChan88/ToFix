using AuthPulse.Core;
using Microsoft.AspNetCore.Mvc;

namespace AuthPulse.Api.Controllers;

/// <summary>Request body for <c>POST /api/token</c>.</summary>
public sealed class TokenRequest
{
    public string? Secret { get; set; }
    public int Digits { get; set; } = 6;
    public int Period { get; set; } = 30;
    public string Algorithm { get; set; } = "SHA1";
}

[ApiController]
[Route("api/[controller]")]
public sealed class TokenController : ControllerBase
{
    /// <summary>Generate a TOTP from a Base32 secret or otpauth:// URI. Nothing is stored.</summary>
    [HttpPost]
    public IActionResult Post([FromBody] TokenRequest request)
    {
        var secret = (request?.Secret ?? string.Empty).Trim();
        if (string.IsNullOrEmpty(secret))
            return BadRequest(new { ok = false, error = "Please enter a secret key or otpauth URI." });

        try
        {
            TotpResult result = secret.StartsWith("otpauth://", StringComparison.OrdinalIgnoreCase)
                ? Totp.FromInput(secret)
                : Totp.Generate(
                    secret,
                    request!.Digits,
                    request.Period,
                    Totp.ParseAlgorithm(request.Algorithm));

            return Ok(new
            {
                ok = true,
                token = result.Code,
                seconds_left = result.SecondsLeft,
                period = result.Period,
                digits = result.Digits,
                algorithm = result.Algorithm
            });
        }
        catch (TotpException ex)
        {
            return BadRequest(new { ok = false, error = ex.Message });
        }
    }
}

[ApiController]
[Route("[controller]")]
public sealed class HealthzController : ControllerBase
{
    [HttpGet]
    public IActionResult Get() => Ok(new { status = "ok", service = "authpulse-dotnet-api" });
}
