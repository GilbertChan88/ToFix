# AuthPulse Py

The **Python + Flask** reference build of [AuthPulse](../BRAND.md) — a 2fa.live-style
TOTP (Time-based One-Time Password) generator. *Your 2FA codes, in a heartbeat.*

Paste a Base32 secret key or an `otpauth://` URI and get the live 6-digit code with a
countdown ring. TOTP is implemented from scratch (RFC 6238 / RFC 4226) using only the
Python standard library — no third-party crypto. Secrets are never stored.

## Run

```bash
cd authpulse-python
python3 -m venv .venv && source .venv/bin/activate   # optional
pip install -r requirements.txt
python app.py
# open http://localhost:5000
```

## Layout

| File                    | Purpose                                             |
|-------------------------|-----------------------------------------------------|
| `totp.py`               | RFC 6238 TOTP engine (stdlib only) + otpauth parser |
| `app.py`                | Flask app: `GET /`, `POST /api/token`, `GET /healthz` |
| `templates/index.html`  | Branded UI                                          |
| `static/`               | `style.css`, `app.js` (live countdown), `logo.svg`  |

## API

`POST /api/token`

```jsonc
// request
{ "secret": "JBSWY3DPEHPK3PXP", "digits": 6, "period": 30, "algorithm": "SHA1" }
// response
{ "ok": true, "token": "492039", "seconds_left": 17, "period": 30, "digits": 6, "algorithm": "SHA1" }
```

`secret` may also be a full `otpauth://totp/...` URI, in which case its embedded
`digits` / `period` / `algorithm` are used.

## Correctness

`totp.py` passes the official RFC 6238 Appendix B test vectors (SHA1/SHA256, 8-digit).
