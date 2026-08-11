"""
AuthPulse Py — Flask web app.

A 2fa.live-style TOTP generator. Paste a Base32 secret (or otpauth:// URI)
and get the live 6-digit code with a countdown. Nothing is stored: each
request decodes the secret, generates the code, and forgets it.
"""

from __future__ import annotations

from flask import Flask, jsonify, render_template, request

import totp

app = Flask(__name__)

BRAND = {
    "name": "AuthPulse",
    "tagline": "Your 2FA codes, in a heartbeat.",
    "stack": "Python + Flask",
}


@app.get("/")
def index():
    return render_template("index.html", brand=BRAND)


@app.post("/api/token")
def api_token():
    """Generate a TOTP from JSON: {"secret": "...", "digits":6, "period":30}."""
    data = request.get_json(silent=True) or {}
    secret = (data.get("secret") or "").strip()
    if not secret:
        return jsonify(ok=False, error="Please enter a secret key or otpauth URI."), 400

    try:
        if secret.lower().startswith("otpauth://"):
            result = totp.from_input(secret)
        else:
            result = totp.generate(
                secret,
                digits=int(data.get("digits", 6)),
                period=int(data.get("period", 30)),
                algorithm=str(data.get("algorithm", "SHA1")),
            )
    except totp.TotpError as exc:
        return jsonify(ok=False, error=str(exc)), 400
    except (ValueError, TypeError):
        return jsonify(ok=False, error="Invalid options provided."), 400

    return jsonify(
        ok=True,
        token=result.code,
        seconds_left=result.seconds_left,
        period=result.period,
        digits=result.digits,
        algorithm=result.algorithm,
    )


@app.get("/healthz")
def healthz():
    return jsonify(status="ok", service="authpulse-py")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
