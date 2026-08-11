"""
AuthPulse — TOTP engine (RFC 6238 / RFC 4226).

Pure Python standard library only: no third-party crypto dependency.
Generates Time-based One-Time Passwords from a Base32 secret, exactly like
the codes an authenticator app (Google Authenticator, Authy, ...) produces.
"""

from __future__ import annotations

import base64
import binascii
import hashlib
import hmac
import struct
import time
from dataclasses import dataclass
from urllib.parse import parse_qs, unquote, urlparse

# Supported HMAC algorithms for TOTP.
_ALGORITHMS = {
    "SHA1": hashlib.sha1,
    "SHA256": hashlib.sha256,
    "SHA512": hashlib.sha512,
}


class TotpError(ValueError):
    """Raised when a secret or otpauth URI cannot be parsed."""


@dataclass(frozen=True)
class TotpResult:
    code: str          # zero-padded OTP, e.g. "004321"
    seconds_left: int  # seconds until this code rotates
    period: int        # length of the time step (usually 30s)
    digits: int
    algorithm: str


def normalize_secret(secret: str) -> str:
    """Strip spaces/hyphens, upper-case, and fix Base32 padding."""
    if not secret or not secret.strip():
        raise TotpError("Secret key is empty.")
    cleaned = secret.strip().replace(" ", "").replace("-", "").upper()
    # Base32 alphabet is A-Z, 2-7 (and '=' padding).
    invalid = set(cleaned) - set("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567=")
    if invalid:
        raise TotpError(
            "Secret contains characters that are not valid Base32: "
            + "".join(sorted(invalid))
        )
    # Base32 needs the length to be a multiple of 8; re-pad.
    cleaned = cleaned.rstrip("=")
    pad = (-len(cleaned)) % 8
    return cleaned + ("=" * pad)


def _decode_secret(secret: str) -> bytes:
    try:
        key = base64.b32decode(normalize_secret(secret), casefold=True)
    except binascii.Error as exc:  # pragma: no cover - defensive
        raise TotpError(f"Could not decode Base32 secret: {exc}") from exc
    if not key:
        raise TotpError("Secret decoded to zero bytes.")
    return key


def generate(
    secret: str,
    *,
    digits: int = 6,
    period: int = 30,
    algorithm: str = "SHA1",
    at: float | None = None,
) -> TotpResult:
    """Generate the current TOTP for a Base32 ``secret``."""
    algo = algorithm.upper()
    if algo not in _ALGORITHMS:
        raise TotpError(f"Unsupported algorithm '{algorithm}'.")
    if digits < 6 or digits > 10:
        raise TotpError("Digits must be between 6 and 10.")
    if period <= 0:
        raise TotpError("Period must be a positive number of seconds.")

    key = _decode_secret(secret)
    now = time.time() if at is None else at
    counter = int(now // period)

    # RFC 4226: HMAC of the 8-byte big-endian counter.
    msg = struct.pack(">Q", counter)
    digest = hmac.new(key, msg, _ALGORITHMS[algo]).digest()

    # Dynamic truncation (RFC 4226 §5.3).
    offset = digest[-1] & 0x0F
    binary = struct.unpack(">I", digest[offset : offset + 4])[0] & 0x7FFFFFFF
    code = str(binary % (10 ** digits)).zfill(digits)

    seconds_left = period - int(now % period)
    return TotpResult(
        code=code,
        seconds_left=seconds_left,
        period=period,
        digits=digits,
        algorithm=algo,
    )


def parse_otpauth(uri: str) -> dict:
    """Parse an ``otpauth://totp/...`` URI into generate() kwargs + label."""
    parsed = urlparse(uri.strip())
    if parsed.scheme != "otpauth" or parsed.netloc.lower() != "totp":
        raise TotpError("Not a valid otpauth://totp/ URI.")
    params = {k: v[0] for k, v in parse_qs(parsed.query).items()}
    if "secret" not in params:
        raise TotpError("otpauth URI is missing the 'secret' parameter.")

    label = unquote(parsed.path.lstrip("/"))
    issuer = params.get("issuer", "")
    return {
        "secret": params["secret"],
        "digits": int(params.get("digits", 6)),
        "period": int(params.get("period", 30)),
        "algorithm": params.get("algorithm", "SHA1"),
        "label": label,
        "issuer": issuer,
    }


def from_input(value: str) -> TotpResult:
    """Accept either a raw Base32 secret or a full otpauth:// URI."""
    value = (value or "").strip()
    if value.lower().startswith("otpauth://"):
        kwargs = parse_otpauth(value)
        kwargs.pop("label", None)
        kwargs.pop("issuer", None)
        return generate(**kwargs)
    return generate(value)
