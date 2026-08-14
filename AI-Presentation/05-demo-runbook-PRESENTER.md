# Live Demo Runbook — PRESENTER (Confidential)
## "Using AI in Our Lives" — full operational guide

> **This is your cockpit.** It has everything the audience handout has, PLUS: pre-session setup, minute-by-minute timing with cues, exact narration, wow-moment callouts, transitions, fallbacks, and troubleshooting. Do **not** distribute this version.
>
> **Companion files:** slide script → `01-presentation-with-speaker-notes.md`; source content → `demo-materials/`; audience copy → `04-demo-runbook-AUDIENCE.md`.

**Demo placement in the deck:** Demo 1 → Slide 9 · Demo 2 → Slide 11 · Demo 3 → Slide 13 · Demo 4 → Slide 17.
**Total live demo budget: ~8 minutes** (4 × ~2 min), inside the 45-min session.

---

## PART A — Pre-session setup (do the morning of, ~15 min)

### A1. Accounts & logins (log in NOW, stay logged in)
- [ ] **Gamma** (gamma.app) — logged in, on the dashboard.
- [ ] **NotebookLM** (notebooklm.google) — logged into the Google account you'll use.
- [ ] **Gmail + Google Calendar** — same Google account, open in tabs.
- [ ] **Gemini app** (gemini.google.com) — logged in.
- [ ] **Canva** (canva.com) — logged in. (Optional: Ideogram, Microsoft Designer.)

### A2. Pre-generate the slow assets (CRITICAL)
- [ ] **Demo 2 Audio Overview** — upload `demo-materials/demo2-study-source.md` to a NotebookLM notebook and **generate the Audio Overview now**. It takes several minutes; never do it live. Leave the notebook open on the Studio tab, audio ready to play.
- [ ] **Demo 4 comparison** — optionally pre-make one Ideogram poster so you can contrast it with the live Canva one.

### A3. Fallback safety net (open each in its own browser tab)
- [ ] Demo 1: a **finished Gamma deck** you generated earlier.
- [ ] Demo 2: the **downloaded audio file** + a screenshot of a generated quiz/study guide.
- [ ] Demo 3: a **45-second screen recording** of the full Gmail→Calendar→Meet flow (email demos are the most fragile — record this backup).
- [ ] Demo 4: a **pre-made Canva poster** + **pre-made Ideogram poster**.

### A4. Room & display
- [ ] Browser zoom **125–150%** so the back row can read prompts.
- [ ] Close notification-heavy apps (Slack/email popups on screen = bad look).
- [ ] Have `demo-materials/` files open to copy-paste prompts fast.
- [ ] Test audio output for Demo 2 through the room speakers.

### A5. Edit before presenting
- [ ] In the poster prompts, replace `[Fri 22 Aug]`, `[3:00 PM]`, `[Training Room 2]` with your real details.
- [ ] Decide who Demo 3's invite is "to" (yourself is safest for a live send).

---

## PART B — Timing map

| # | Demo | Slide | Target duration | Hard cap | Must pre-gen? |
|---|---|---|---|---|---|
| 1 | Notes → slides (Gamma) | 9 | 2:00 | 2:30 | Fallback deck |
| 2 | Study notes → quiz + podcast | 11 | 2:00 | 2:30 | **YES — audio** |
| 3 | Gmail + Calendar + Meet | 13 | 2:00 | 2:30 | Screen recording |
| 4 | Poster / EDM | 17 | 2:00 | 2:30 | Compare poster |

> **If you're running behind:** shrink Demo 4 to just showing the generation + one edit (skip the Ideogram compare). Never cut Demo 2's audio — it's the biggest wow.

---

## 🎬 DEMO 1 — Notes → stunning deck (Slide 9) · Target 2:00

**Setup state:** Gamma dashboard open. `demo-materials/demo1-source-reading.md` copied to clipboard.

**Run (with timing cues):**
- **0:00–0:20** — "I've got a page of rough notes here — the kind of mess we all jot down." Create new → **Paste in text** → paste notes.
- **0:20–0:35** — Set **8 cards**, tone **Professional & friendly**, paste the prompt (below). Hit **Generate**.
- **0:35–1:20** — *While it generates, keep talking:* "Notice it's not just dumping text — it's choosing layouts, pulling images, writing headlines." 
- **1:20–1:45** — Deck appears. Scroll through 2–3 slides.
- **1:45–2:00** — 🌟 **WOW:** change the **Theme** at the top. "Building this by hand is an afternoon. That was 40 seconds." Then: "I'd re-check facts and match our brand — minutes of polish, not hours of building."

**Prompt (Gamma instructions box):**
```
Turn the notes I pasted into a clean, engaging 8-slide presentation for a general
adult audience. Requirements:
- Slide 1: a punchy title slide with a one-line hook.
- One clear idea per slide, max 6 words per bullet, max 4 bullets per slide.
- Rewrite my rough notes into confident, plain-English headlines.
- Add one relevant image or icon per slide.
- End with a "3 things to try tonight" takeaway slide.
- Keep all facts strictly to what's in my notes; do not invent statistics.
```

**Say the caveat aloud:** "It can produce generic images or over-confident wording — you stay the editor."

**Troubleshooting:**
- *Slow/stuck generating* → switch to your pre-made deck tab; narrate as if planned.
- *Login dropped* → have Gamma open and authenticated before you start; never log in live.
- *Bad output* → that's a teaching moment: "See? First draft, not final — this is why we edit."

**Transition to next:** "That's creating. Now let's talk about *learning* — for the students in the room."

---

## 🎬 DEMO 2 — Study notes → quiz + podcast (Slide 11) · Target 2:00

**Setup state:** NotebookLM notebook open with `demo2-study-source.md` uploaded and **Audio Overview already generated**.

**Run (with timing cues):**
- **0:00–0:25** — Show the uploaded source. Point at **inline citations**: "Every answer links to the exact line, so it doesn't make things up — unlike a normal chatbot."
- **0:25–0:55** — In **Studio**, click **Study guide** (or **Quiz**). Read one generated quiz question aloud.
- **0:55–1:25** — Paste the chat prompt (below); show the cited, grounded answer.
- **1:25–2:00** — 🌟 **WOW:** play **15–20 seconds** of the pre-generated **Audio Overview**. "That's your own lecture notes, as a podcast you revise to on the bus." Stop the audio cleanly.

**Prompt (NotebookLM chat):**
```
From my source, create a 5-question self-test that gets progressively harder,
then hide the answers below a line so I can check myself afterwards. Focus on the
concepts I'm most likely to be examined on, and cite the section each question
comes from.
```
**Optional tutor prompt (only if time):**
```
Act as my tutor for this material. Explain "encoding vs. retrieval" using a simple
everyday analogy, then ask me two questions to check I understood. Do not give me
the answers until I respond.
```

**Say the caveat aloud:** "It stays inside your sources — great for trust, but it won't add outside context unless you ask."

**Troubleshooting:**
- *Audio won't play in-app* → play the downloaded audio file; or if all else fails, describe it and show the quiz screenshot.
- *Quiz slow to generate* → you can pre-generate the study guide too; screenshot as backup.
- *Chat limit reached (free = ~50/day)* → don't burn queries rehearsing on the same account you'll present with; use a second account for practice.

**Transition to next:** "Learning, sorted. Now the thing that eats everyone's mornings — email and meetings."

---

## 🎬 DEMO 3 — Gmail + Calendar + Meet (Slide 13) · Target 2:00

**Setup state:** Gemini app, Gmail, and Google Calendar each open in a tab. Optional: the sample "incoming email" from `demo-materials/demo3-email-scenario.md` already sent to yourself.

**Honesty framing (say up front):** "Everything here works on a FREE personal account. The deepest automation — finding slots across colleagues' calendars, auto Meet transcription — is paid Workspace. I'll be clear about the line."

**Run (with timing cues):**
- **0:00–0:30** — In **Gemini**, paste **Prompt A**. Read the drafted invite aloud — "5 seconds, done."
- **0:30–1:00** — Paste the draft into a new **Gmail** message. Point out **"Add to Calendar"** appearing because a date/time is detected. Click it → event auto-fills.
- **1:00–1:30** — In the **Calendar** event → **Add Google Meet video conferencing** → link generated → **Save**.
- **1:30–2:00** — 🌟 **WOW:** "I never opened the calendar or typed a date twice." Then paste **Prompt B** in Gemini for instant agenda + prep. "And it just prepped the meeting too."

**Prompt A — draft the invite (Gemini):**
```
Write a short, friendly meeting invitation email.
Purpose: kick-off for our "AI in Our Lives" learning session.
Attendees: my team (5 people).
Proposed time: next Tuesday 3:00–3:45 PM.
Include: a one-line purpose, a 3-bullet agenda, and a line saying a Google Meet
link is attached. Keep it under 120 words, warm but professional.
```
**Prompt B — meeting prep (Gemini):**
```
Create a 45-minute agenda for the session above with rough timings, 3 discussion
questions to open the room, and a list of what I should prepare beforehand.
```

**Say the caveat aloud:** "On free, AI helps at each step but doesn't auto-coordinate across people — that's paid. Still removes most of the busywork. And don't paste confidential names into a free consumer AI."

**Troubleshooting (this demo is the most fragile):**
- *"Add to Calendar" doesn't appear* → use Gmail's **"Help me write"** to refine, then create the event manually; still fast. OR reply to the pre-sent sample email, which triggers detection more reliably.
- *Anything stalls* → play your **45-sec screen recording** and narrate over it. Strongly consider leading with the recording if the venue Wi-Fi is unknown.
- *Privacy* → send the invite to yourself, not a real distribution list, on stage.

**Transition to next:** "Last one — and it's the crowd-pleaser. Let's make something visual."

---

## 🎬 DEMO 4 — Poster / EDM for THIS session (Slide 17) · Target 2:00

**Setup state:** Canva open. `demo-materials/demo4-poster-brief.md` prompt copied (with real date/venue filled in). Optional pre-made Ideogram poster in a tab.

**Run (with timing cues):**
- **0:00–0:20** — "Meta moment — let's make the poster for THIS session." Canva → Poster → **Design with AI**.
- **0:20–0:35** — Paste **Prompt A**. Generate.
- **0:35–1:10** — Layouts appear; pick one; it opens editable.
- **1:10–1:35** — 🌟 **WOW:** live-edit the **date** (or a colour). "Try that with a flat JPG a designer emailed you."
- **1:35–2:00** — Mention EDM: "One click to **Resize** into an email header for a marketing email." *(If time)* flash the pre-made **Ideogram** poster: "Canva = editable & on-brand; Ideogram = artistic, text baked in."

**Prompt A — Canva Magic Design:**
```
Create a modern, eye-catching event poster (portrait) for a staff learning session.
Title: "Using AI in Our Lives"
Subtitle: "A hands-on 45-minute session — free tools only"
Details to include: Date [Fri 22 Aug], Time [3:00 PM], Venue [Training Room 2],
"Bring your laptop."
Style: clean, friendly, tech-forward; blue and teal palette; lots of white space;
one simple AI/lightbulb motif. Leave text fully editable.
```
**Prompt B — Ideogram (text-in-image compare):**
```
A vibrant, modern event poster with the bold headline text "USING AI IN OUR LIVES"
clearly readable at the top, subtitle "Free tools, real results — 45-min session"
below. Flat vector illustration style, blue and teal, a glowing lightbulb made of
circuit lines, plenty of clean space. High legibility text.
```

**Say the caveat aloud:** "Proofread every letter — AI still misspells text in images — and free tiers usually forbid commercial use and may add a watermark."

**Troubleshooting:**
- *Generation slow/down* → show pre-made Canva + Ideogram posters, explain the prompts.
- *Layout looks off* → pick a different one from the set; "part of the workflow is choosing."

**Transition out:** "Four demos, four free tools, zero dollars. Let's wrap up with how to do this responsibly."

---

## PART C — Presenter reminders

**The 4 wow moments (land these):**
1. Gamma theme-swap restyling the whole deck.
2. NotebookLM podcast of the audience's own notes.
3. The one-tap email→calendar jump.
4. Live-editing the date on a finished poster.

**Pacing discipline:** each demo has a **2:00 target / 2:30 hard cap**. Watch the clock; the demos are where sessions overrun. If a demo misbehaves for >20 seconds, switch to the fallback and keep moving.

**Recovery line if anything breaks:** "This is a great reminder — AI is a fast first draft, not magic. Here's one I prepared earlier." (Switch to fallback tab.) Audiences love honesty; a graceful fallback beats a frozen screen.

**Repeat throughout — the two rules:** AI can be confidently wrong (verify what matters); free is not private (never paste confidential data).
