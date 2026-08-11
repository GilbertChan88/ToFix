// AuthPulse .NET — client logic. Posts to the Razor "Generate" handler, which
// proxies to the AuthPulse Web API, then drives the live countdown ring.
(() => {
  "use strict";

  const $ = (id) => document.getElementById(id);
  const secretEl = $("secret");
  const errorEl = $("error");
  const resultEl = $("result");
  const tokenEl = $("token");
  const metaEl = $("meta");
  const countdownEl = $("countdown");
  const ring = $("ringProgress");
  const copyBtn = $("copy");

  const CIRC = 2 * Math.PI * 52; // ring circumference (r=52)
  ring.style.strokeDasharray = String(CIRC);

  let timer = null;
  let state = null; // { period, secondsLeft }

  function showError(msg) {
    errorEl.textContent = msg;
    errorEl.hidden = false;
    resultEl.hidden = true;
    if (timer) clearInterval(timer);
  }

  function paintRing() {
    const { period, secondsLeft } = state;
    ring.style.strokeDashoffset = String(CIRC * (1 - secondsLeft / period));
    countdownEl.textContent = String(secondsLeft);
    ring.style.stroke = secondsLeft <= 5 ? "#F59E0B" : "#14B8A6";
  }

  function startCountdown() {
    if (timer) clearInterval(timer);
    paintRing();
    timer = setInterval(() => {
      state.secondsLeft -= 1;
      if (state.secondsLeft <= 0) {
        generate(); // code rotated — fetch a fresh one
        return;
      }
      paintRing();
    }, 1000);
  }

  async function generate() {
    const secret = secretEl.value.trim();
    if (!secret) return showError("Please enter a secret key or otpauth URI.");

    const payload = {
      secret,
      digits: Number($("digits").value),
      period: Number($("period").value),
      algorithm: $("algorithm").value,
    };

    let res, data;
    try {
      res = await fetch("?handler=Generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      data = await res.json();
    } catch {
      return showError("Network error — could not reach the server.");
    }

    if (!res.ok || !data.ok) {
      return showError(data && data.error ? data.error : "Could not generate a code.");
    }

    errorEl.hidden = true;
    resultEl.hidden = false;
    tokenEl.textContent = data.token;
    metaEl.textContent = `${data.digits} digits · ${data.period}s · ${data.algorithm}`;
    state = { period: data.period, secondsLeft: data.seconds_left };
    startCountdown();
  }

  $("generate").addEventListener("click", generate);
  secretEl.addEventListener("keydown", (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key === "Enter") generate();
  });

  copyBtn.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(tokenEl.textContent.trim());
      copyBtn.textContent = "Copied";
      copyBtn.classList.add("copied");
      setTimeout(() => {
        copyBtn.textContent = "Copy";
        copyBtn.classList.remove("copied");
      }, 1500);
    } catch {
      /* clipboard unavailable */
    }
  });

  $("demo").addEventListener("click", () => {
    secretEl.value = "JBSWY3DPEHPK3PXP";
    generate();
  });
})();
