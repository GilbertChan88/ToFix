# AuthPulse .NET

The **.NET 9** reference build of [AuthPulse](../BRAND.md) — a 2fa.live-style TOTP
generator. *Your 2FA codes, in a heartbeat.*

This build is split into the **Web API** and **Razor Pages** projects requested, plus a
shared class library that holds the TOTP engine:

```
authpulse-dotnet/
├── AuthPulse.sln
└── src/
    ├── AuthPulse.Core/   # RFC 6238 TOTP engine (no third-party packages)
    ├── AuthPulse.Api/    # ASP.NET Core Web API — the TOTP microservice
    └── AuthPulse.Web/    # ASP.NET Core Razor Pages — the branded front-end
```

### How they fit together

```
Browser ──POST /?handler=Generate──▶ AuthPulse.Web (Razor Pages)
                                          │  server-side HttpClient ("AuthPulseApi")
                                          ▼
                                     AuthPulse.Api  ──uses──▶ AuthPulse.Core (Totp)
                                     POST /api/token
```

The Razor page keeps no TOTP logic of its own: it forwards each request to the Web API
(the single source of truth), which calls `AuthPulse.Core`. Nothing is stored anywhere.

## Run

Open two terminals from `authpulse-dotnet/`:

```bash
# 1) the API (defaults to http://localhost:5043)
dotnet run --project src/AuthPulse.Api

# 2) the Razor front-end (defaults to http://localhost:5002)
dotnet run --project src/AuthPulse.Web
```

Then open the Razor site (e.g. <http://localhost:5002>). The front-end reads the API
address from `ApiBaseUrl` in `src/AuthPulse.Web/appsettings.json` (default
`http://localhost:5043`, matching the API's default port).

> Tip: to pin ports explicitly, use `--urls`, e.g.
> `dotnet run --project src/AuthPulse.Api --no-launch-profile --urls http://localhost:5043`.

## Web API

| Endpoint          | Description                                   |
|-------------------|-----------------------------------------------|
| `POST /api/token` | Generate a TOTP from a secret or otpauth URI  |
| `GET /healthz`    | Health check                                  |
| `GET /`           | Service info / endpoint list                  |

```jsonc
// POST /api/token
{ "secret": "JBSWY3DPEHPK3PXP", "digits": 6, "period": 30, "algorithm": "SHA1" }
// -> { "ok": true, "token": "492039", "seconds_left": 17, "period": 30, "digits": 6, "algorithm": "SHA1" }
```

`secret` may also be a full `otpauth://totp/...` URI, whose embedded parameters are used.

## Correctness

`AuthPulse.Core.Totp` reproduces the official RFC 6238 Appendix B test vectors
(SHA1 & SHA256, 8-digit) and matches the Python build byte-for-byte.
