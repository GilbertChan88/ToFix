# AuthPulse — Brand Kit

> **AuthPulse** — *Your 2FA codes, in a heartbeat.*

AuthPulse is a free, privacy-first **TOTP (Time-based One-Time Password) generator**,
in the spirit of [2fa.live](https://2fa.live). Paste a 2FA secret key (or an
`otpauth://` URI) and instantly get the live 6-digit code with a countdown ring that
shows how long the code stays valid. All generation happens on the server per request —
no secrets are ever stored.

This repository ships **two independent reference implementations** of the same product,
sharing one brand and one visual language:

| Product        | Stack                                   | Folder               |
|----------------|-----------------------------------------|----------------------|
| AuthPulse **Py**   | Python + Flask (TOTP from scratch)      | `authpulse-python/`  |
| AuthPulse **.NET** | .NET 9 · Web API + Razor Pages + Core lib | `authpulse-dotnet/`  |

---

## Identity

- **Name:** AuthPulse
- **Wordmark:** `Auth` in slate/white, `Pulse` in the indigo→teal gradient.
- **Tagline:** *Your 2FA codes, in a heartbeat.*
- **Voice:** Fast, trustworthy, minimal. Security without the friction.

## Logo

A rounded shield containing a pulse/heartbeat waveform — security (shield) meets
"live" time-based codes (pulse). The canonical asset lives in each project and is
reproduced here:

```svg
<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="AuthPulse">
  <defs>
    <linearGradient id="ap" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#6366F1"/>
      <stop offset="1" stop-color="#14B8A6"/>
    </linearGradient>
  </defs>
  <path d="M24 3 6 9v13c0 11 7.5 18.5 18 23 10.5-4.5 18-12 18-23V9L24 3Z" fill="url(#ap)"/>
  <path d="M12 25h6l3-8 5 15 3-9 2 2h5" fill="none" stroke="#0F172A"
        stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

## Color palette

| Token            | Hex       | Usage                                  |
|------------------|-----------|----------------------------------------|
| Indigo (primary) | `#6366F1` | Brand, buttons, links, gradient start  |
| Indigo dark      | `#4F46E5` | Hover / active states                  |
| Teal (accent)    | `#14B8A6` | Highlights, gradient end, success      |
| Slate 900 (bg)   | `#0F172A` | App background                         |
| Slate 800        | `#1E293B` | Cards / surfaces                       |
| Slate 700        | `#334155` | Borders / inputs                       |
| Slate 100 (text) | `#F1F5F9` | Primary text                           |
| Slate 400        | `#94A3B8` | Muted text                             |
| Amber            | `#F59E0B` | Countdown "expiring soon" warning      |
| Red              | `#EF4444` | Errors                                 |

**Signature gradient:** `linear-gradient(135deg, #6366F1 0%, #14B8A6 100%)`

## Typography

- **Font:** `Inter`, falling back to `system-ui, -apple-system, Segoe UI, Roboto, sans-serif`.
- **Code / tokens:** `ui-monospace, "JetBrains Mono", "SF Mono", Menlo, monospace`,
  letter-spacing widened so the 6-digit code is easy to read.

## Product principles

1. **Zero storage** — secrets are used for a single request and discarded.
2. **Instant feedback** — live countdown ring, one-tap copy.
3. **Standards-correct** — RFC 6238 (TOTP) over RFC 4226 (HOTP), Base32 (RFC 4648) secrets.
4. **Same brand, two stacks** — the Python and .NET builds are visually indistinguishable.
