# Tutor Demo Guide — Click-by-Click Instructions
## "Using AI in Our Lives" — the most detailed, do-exactly-this walkthrough for the person running the demos

> **Who this is for:** the presenter/tutor operating the laptop. This is the most granular of the three demo documents. It tells you **exactly what to click, what to type, what you should see, and what to do when it goes wrong** — step by micro-step, with a running clock.
>
> **Document map:** high-level cues → `05-demo-runbook-PRESENTER.md` · audience follow-along → `04-demo-runbook-AUDIENCE.md` · slide script → `01-presentation-with-speaker-notes.md` · this file = the button-level script.
>
> **Legend:** 🖱 = click/action · ⌨ = type/paste · 👀 = what you should see · 🗣 = say this · ⏱ = elapsed time · 🛟 = if it breaks.

---

## 0. One-time setup the morning of (≈ 20 minutes)

### 0.1 Log in everywhere (and STAY logged in)
1. 🖱 Open your browser. Create a dedicated **presentation window** with these tabs, left to right, in this order (matches demo order):
   - Tab 1 — `gamma.app` (signed in, on the dashboard)
   - Tab 2 — `notebooklm.google` (signed in; your prepared notebook open — see 0.2)
   - Tab 3 — `gemini.google.com` (signed in)
   - Tab 4 — `mail.google.com` (same Google account)
   - Tab 5 — `calendar.google.com` (same account)
   - Tab 6 — `canva.com` (signed in)
   - Tab 7 — Fallbacks folder (see 0.4)
2. 🖱 Set browser zoom to **130%** (Ctrl/Cmd + a few times). Verify the back row can read a prompt box.
3. 🖱 Turn on **Do Not Disturb** on the OS. Quit Slack, Teams, and personal mail popups.

### 0.2 Pre-build the NotebookLM notebook (Demo 2 — do NOT skip)
1. 🖱 In Tab 2, click **Create new** → **New notebook**.
2. 🖱 **Add source** → **Upload** → choose `demo-materials/demo2-study-source.md` (or paste its text via **Copied text**).
3. 👀 Wait until the source shows a green/ready tick and a summary appears.
4. 🖱 Open the **Studio** panel (right side) → click **Audio Overview** → **Generate**.
5. ⏱ This takes **~3–6 minutes**. Do it now, early. Leave it done and ready.
6. 🖱 Once ready, click it once to confirm it plays, then **pause at 0:00** so it's cued.
7. (Optional but nice) 🖱 Also click **Study guide** now so it's pre-made; you can regenerate live for effect or fall back to this.

### 0.3 Pre-send the Demo 3 email trigger (optional, improves reliability)
1. 🖱 In Gmail (Tab 4), send yourself the sample "incoming email" from `demo-materials/demo3-email-scenario.md`.
2. 👀 Confirm it arrives. Replying to a dated email makes Gmail's "Add to Calendar" chip appear more reliably.

### 0.4 Build the fallback safety net (open each in Tab 7 or a folder)
- [ ] **Demo 1:** a finished Gamma deck you generated yesterday (open in a pinned tab).
- [ ] **Demo 2:** the **downloaded audio file** (Studio → ⋮ → Download) + a screenshot of the quiz/study guide.
- [ ] **Demo 3:** a **45–60 sec screen recording** of the full email→calendar→Meet flow. (Most important fallback — record this.)
- [ ] **Demo 4:** one pre-made Canva poster + one pre-made Ideogram poster (screenshots or open designs).

### 0.5 Fill in the real details before you present
- [ ] In every poster/email prompt, replace `[Fri 22 Aug]`, `[3:00 PM]`, `[Training Room 2]` with real values.
- [ ] Decide the Demo 3 recipient = **yourself** (never a live distribution list on stage).

### 0.6 Final 2-minute rehearsal check
- [ ] Run the Gamma generate once on a throwaway to confirm your account has credits.
- [ ] Confirm the NotebookLM audio plays through the **room speakers** (not just laptop).
- [ ] Note your remaining NotebookLM free chats (≈50/day) — don't burn them rehearsing on the live account.

---

## 🎬 DEMO 1 — Messy notes → a stunning deck (Gamma)
**Appears on:** Slide 9/11 · **Budget:** 2:00 (hard cap 2:30) · **Source:** `demo-materials/demo1-source-reading.md`

### Before you switch to the demo
- 🖱 Have `demo1-source-reading.md` open; select **everything below the `---` line** and **copy** (Ctrl/Cmd+C).
- 🗣 Bridge line from the slide: *"Enough theory — let's watch it happen."*

### Step-by-step
| ⏱ | 🖱 Action | 👀 Expect | 🗣 Say |
|---|---|---|---|
| 0:00 | Switch to **Tab 1 (Gamma)** → click **Create new** | The create menu opens | "I've got a page of the kind of messy notes we all scribble." |
| 0:12 | Choose **Paste in text** | A large paste box appears | "I'll paste my own notes so it uses my content, not invented facts." |
| 0:18 | ⌨ **Paste** the notes into the box | Notes fill the box | — |
| 0:25 | Set **Cards = 8**, **Tone = Professional & friendly** (or default) | Options set | "I'll ask for 8 slides." |
| 0:30 | ⌨ Paste the **prompt** (below) into the instructions/prompt field | Prompt visible | — |
| 0:38 | 🖱 Click **Generate / Continue** | Progress animation starts | "Now watch — it's choosing layouts, writing headlines, pulling images." |
| 0:38–1:15 | *(keep talking while it works)* | Slides build one by one | Narrate what it's doing (don't go silent). |
| 1:15 | 🖱 Scroll through 2–3 finished slides | A designed deck | "From a wall of text to this, in about 40 seconds." |
| 1:35 | 🖱 Click **Theme** (top bar) → pick a different theme | Whole deck restyles instantly | 🌟 **WOW:** "One click restyles everything." |
| 1:55 | — | — | "I'd still verify facts and match our brand — minutes, not an afternoon." |

**⌨ PROMPT (paste into Gamma's instructions box):**
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

**🛟 If it breaks**
- *Spinner stuck >20 sec* → 🗣 "While that thinks, here's one I made earlier" → switch to the pre-made Gamma tab and scroll it.
- *Asks you to log in* → you should already be logged in (setup 0.1); if not, switch straight to the fallback tab.
- *Output has a wrong fact* → **use it**: 🗣 "See — first draft, not final. This is exactly why we stay the editor."

**🗣 Transition out:** *"That's AI helping us create. Now let's help us learn — for the students in the room."*

---

## 🎬 DEMO 2 — Study notes → quiz + podcast (NotebookLM)
**Appears on:** Slide 11/13 · **Budget:** 2:00 (hard cap 2:30) · **Prep:** audio already generated (setup 0.2)

### Step-by-step
| ⏱ | 🖱 Action | 👀 Expect | 🗣 Say |
|---|---|---|---|
| 0:00 | Switch to **Tab 2 (NotebookLM)** — your prepared notebook | Source listed, Studio panel visible | "I've uploaded a reading on how memory works." |
| 0:10 | 🖱 Click the source → hover a sentence in an answer to show a **citation** | Citation chip / source highlight | "Every claim links to the exact line — that's why it doesn't make things up." |
| 0:30 | 🖱 In **Studio**, click **Quiz** (or show the pre-made **Study guide**) | A quiz/study guide generates | "One click turns my notes into a self-test." |
| 0:50 | 🖱 Read **one** quiz question aloud | Question on screen | Read it, pause. "Straight from my own material." |
| 1:05 | 🖱 Click the **chat box** → ⌨ paste the **prompt** (below) → Enter | A cited, structured self-test appears | "I can shape it too — harder questions, hidden answers, with citations." |
| 1:25 | 🖱 Switch to **Studio → Audio Overview** → press **Play** | Two AI voices start | 🌟 **WOW:** "This is the bit that gets people." |
| 1:25–1:45 | Let it play **15–20 seconds**, then **pause** | Natural two-host chat | "Two AI hosts discussing *your* notes — revise on the bus." |
| 1:55 | — | — | "One rule: it only knows what you upload. Great sources in, great study out." |

**⌨ PROMPT (paste into the NotebookLM chat):**
```
From my source, create a 5-question self-test that gets progressively harder,
then hide the answers below a line so I can check myself afterwards. Focus on the
concepts I'm most likely to be examined on, and cite the section each question
comes from.
```

**🛟 If it breaks**
- *Audio won't play through speakers* → play the **downloaded audio file** from Tab 7; if audio is dead entirely, describe it and show the quiz screenshot. Never let dead audio stall you >15 sec.
- *Chat says limit reached* → you rehearsed on a different account (setup 0.6), so this shouldn't happen; if it does, show the pre-generated study guide instead.
- *Generation slow* → talk over it; you have the pre-made study guide as instant backup.

**🗣 Transition out:** *"Learning, handled. Now the thing that eats everyone's mornings — email and meetings."*

---

## 🎬 DEMO 3 — Gmail + Calendar + Meet, end-to-end (free account)
**Appears on:** Slide 13/15 · **Budget:** 2:00 (hard cap 2:30) · **This is the fragile one — consider leading with the recording if Wi-Fi is unknown.**

### Framing to say first
🗣 *"Everything here works on a FREE personal account. The deep automation — matching five calendars, auto-transcription — is paid Workspace. I'll be clear about the line."*

### Step-by-step
| ⏱ | 🖱 Action | 👀 Expect | 🗣 Say |
|---|---|---|---|
| 0:00 | Switch to **Tab 3 (Gemini)** → ⌨ paste **Prompt A** → Enter | A drafted invite email appears | "First, I ask Gemini to write the invite." |
| 0:15 | 🖱 Read the draft; 🖱 **Copy** it | Clean <120-word invite | "Five seconds, done." |
| 0:30 | Switch to **Tab 4 (Gmail)** → 🖱 **Compose** → ⌨ paste the draft | Draft in the compose window | — |
| 0:45 | 👀 Look for the **"Add to Calendar"** chip (because a date/time is present) | Chip appears below the email | "Because it names a time, Gmail offers this." |
| 0:55 | 🖱 Click **Add to Calendar** | An event panel opens, pre-filled | 🌟 **WOW:** "From the email's text to a real event — one tap." |
| 1:10 | Switch to **Tab 5 (Calendar)** → open the new event → 🖱 **Add Google Meet video conferencing** | A Meet link is generated | "Now a video link, in one click." |
| 1:20 | 🖱 **Save** → confirm send invite | Event saved with Meet link | "Invite's out — I never typed the date twice." |
| 1:35 | Switch to **Tab 3 (Gemini)** → ⌨ paste **Prompt B** → Enter | An agenda + 3 questions appears | "And it just prepped the meeting for me too." |
| 2:00 | — | — | "On free it assists each step; full cross-calendar automation is paid." |

**⌨ PROMPT A (into Gemini):**
```
Write a short, friendly meeting invitation email.
Purpose: kick-off for our "AI in Our Lives" learning session.
Attendees: my team (5 people).
Proposed time: next Tuesday 3:00–3:45 PM.
Include: a one-line purpose, a 3-bullet agenda, and a line saying a Google Meet
link is attached. Keep it under 120 words, warm but professional.
```
**⌨ PROMPT B (into Gemini):**
```
Create a 45-minute agenda for the session above with rough timings, 3 discussion
questions to open the room, and a list of what I should prepare beforehand.
```

**🛟 If it breaks**
- *"Add to Calendar" chip doesn't appear* → Plan B: reply to the **pre-sent sample email** (setup 0.3), which triggers detection more reliably. Plan C: in Gmail click **Help me write** to refine, then create the event manually in Calendar — still fast, still on-message.
- *Wi-Fi flaky / anything freezes* → play the **screen recording** and narrate over it. It's completely fine to *lead* with the recording and say "I recorded this earlier so we don't gamble on the venue Wi-Fi."
- *Privacy slip* → only ever send to yourself on stage.

**🗣 Transition out:** *"Last demo — and it's the crowd-pleaser. Let's make something visual."*

---

## 🎬 DEMO 4 — Poster / EDM for THIS session (Canva)
**Appears on:** Slide 17/19 · **Budget:** 2:00 (hard cap 2:30) · **Source:** `demo-materials/demo4-poster-brief.md`

### Before you switch
- 🖱 Have the **Canva prompt** (below, with real date/venue filled in) copied.
- 🖱 Have the pre-made **Ideogram** poster open in a background tab for the compare.

### Step-by-step
| ⏱ | 🖱 Action | 👀 Expect | 🗣 Say |
|---|---|---|---|
| 0:00 | Switch to **Tab 6 (Canva)** → search **"Poster"** → open **Design with AI / Magic Design** | AI design entry box | "Let's make the poster for THIS session — very meta." |
| 0:15 | ⌨ Paste the **prompt** → 🖱 **Generate** | Several poster layouts appear | "I describe it in plain English." |
| 0:40 | 🖱 Click a layout you like → **Customise / Edit** | It opens fully editable | "Notice — these are editable, not flat images." |
| 1:00 | 🖱 Click the **date** text → ⌨ change it | Text updates live | 🌟 **WOW:** "Try editing the date on a JPEG a designer emailed you." |
| 1:20 | 🖱 (optional) change one **colour** to brand it | Colour updates | "One minute to on-brand." |
| 1:35 | 🖱 **Share/Download** → PNG or PDF; mention **Resize** → "Email header" | Download starts | "And Resize turns this poster into the EDM email header." |
| 1:50 | 🖱 Flash the pre-made **Ideogram** tab | Text-in-image poster | "Canva = editable & on-brand; Ideogram = artistic, but text is baked in." |
| 2:00 | — | — | "Whatever tool — proofread every letter. AI still misspells text in images." |

**⌨ PROMPT (into Canva Magic Design):**
```
Create a modern, eye-catching event poster (portrait) for a staff learning session.
Title: "Using AI in Our Lives"
Subtitle: "A hands-on 45-minute session — free tools only"
Details to include: Date [Fri 22 Aug], Time [3:00 PM], Venue [Training Room 2],
"Bring your laptop."
Style: clean, friendly, tech-forward; blue and teal palette; lots of white space;
one simple AI/lightbulb motif. Leave text fully editable.
```

**🛟 If it breaks**
- *Generation slow/down* → show the **pre-made Canva poster**; read the prompt aloud so they see the input→output link.
- *Layouts look poor* → pick a different option from the set: 🗣 "Part of the workflow is choosing — you're the art director."
- *Misspelling in output* → point at it: 🗣 "And there's the classic AI text bug — always proofread."

**🗣 Transition out:** *"Four demos, four free tools, zero dollars. Let's wrap up with how to do all this responsibly."*

---

## 5. Master timing & the four "wow" beats

| Demo | Slide | Target | Hard cap | The one beat to land |
|---|---|---|---|---|
| 1 Gamma | 9/11 | 2:00 | 2:30 | Theme-swap restyles the whole deck |
| 2 NotebookLM | 11/13 | 2:00 | 2:30 | The podcast of the audience's own notes |
| 3 Gmail+Cal+Meet | 13/15 | 2:00 | 2:30 | Email text → real event in one tap |
| 4 Canva | 17/19 | 2:00 | 2:30 | Live-editing the date on a finished poster |

**Total live demo budget ≈ 8 minutes.**

### Universal recovery script (memorise this one line)
> 🗣 *"This is a perfect reminder — AI is a fast first draft, not magic. Here's one I prepared earlier."* → switch to the fallback tab → keep moving. A graceful fallback beats a frozen screen every time; audiences respect the honesty.

### Golden rules to repeat during demos
1. **AI can be confidently wrong** — verify anything that matters.
2. **Free is not private** — never paste passwords, IDs, or confidential data on stage.
3. **Watch the clock** — if a demo misbehaves for more than ~20 seconds, go to the fallback.
