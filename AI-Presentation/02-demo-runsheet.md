# Demo Run-Sheet — 4 Live "Wow" Demos
### Everything you need to run each demo: prep, tools, exact prompts, the wow moment, and a fallback if the Wi-Fi/tool fails.

> **Golden rule of live demos:** rehearse each one once the day before, and **pre-generate anything slow** (audio/video). Keep a screenshot or screen-recording of the finished result open in a browser tab as your fallback — if the live run stalls, switch to the tab and keep talking. Nobody will know.

**Prep checklist (do this the morning of):**
- [ ] Log in to all accounts in advance: Gamma, NotebookLM (Google), Gmail/Calendar, Canva.
- [ ] Demo 2 audio: **pre-generate the NotebookLM Audio Overview** (takes a few minutes) and have it queued.
- [ ] Demo 4: optionally pre-make one Ideogram poster to compare against the live Canva one.
- [ ] Open each `demo-materials/…` source file so you can copy-paste fast.
- [ ] Have fallback screenshots ready in tabs.
- [ ] Increase browser zoom to ~125–150% so the back row can read it.

---

## 🎬 DEMO 1 — Turn plain notes into a stunning deck
**Point it proves:** 2.1 Presentation preparation
**Tool (free):** [Gamma](https://gamma.app) · Alternatives: Canva Magic Design, ChatSlide (accepts PDF/URL/YouTube)
**Time:** ~2 min · **Wow factor:** a wall of text becomes a designed deck in ~30 seconds.

### Source material
Use `demo-materials/demo1-source-reading.md` — a one-page set of rough notes on "The Science of a Good Night's Sleep" (a neutral, relatable topic). Copy the whole file.

### Steps
1. Go to Gamma → **Create new** → **Paste in text** (not "Generate," so it uses *your* content).
2. Paste the notes from the source file.
3. Set: **8 cards**, tone **"Professional & friendly,"** and paste the prompt below into the instructions box.
4. Click **Generate**. Talk through what it's doing while it works.
5. When done, change the **Theme** (top bar) live to show instant restyling.

### Exact prompt (paste into Gamma's "instructions/prompt" box)
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

### The wow moment
Right after it generates, switch the theme once. Say: *"Building this by hand is an afternoon. That was 40 seconds."*

### Honest caveat to say aloud
"It can still produce generic images or over-confident wording — so I'd re-check facts and match our brand colours before presenting."

### Fallback
If Gamma is slow/down: open your pre-made deck in a tab, OR run the same prompt in Canva Magic Design ("Docs to Deck") which you've pre-tested.

---

## 🎬 DEMO 2 — Your study notes become a quiz + a podcast
**Point it proves:** 2.2 AI for students' study
**Tool (free):** [NotebookLM](https://notebooklm.google) (any Google account)
**Time:** ~2 min · **Wow factor:** two AI hosts discuss *your* notes in a natural podcast.

### Source material
Use `demo-materials/demo2-study-source.md` — a ~600-word explainer on "How Memory Works: Encoding, Storage, Retrieval." Neutral, exam-style content students relate to.

### Prep (IMPORTANT — do before the session)
- Upload the source and **generate the Audio Overview in advance** (Studio panel → Audio Overview). It takes several minutes, so never do this live.
- Keep the notebook open on the Studio tab.

### Steps (live)
1. Show the uploaded source in the notebook. Point out **inline citations** — "every answer links to the exact line, so it doesn't make things up."
2. In **Studio**, click **Study guide** (or **Quiz**/**Flashcards**) → generated in seconds. Read one quiz question aloud.
3. In the chat box, paste the prompt below and show the grounded, cited answer.
4. Play **15–20 seconds** of the pre-generated **Audio Overview**. That's the mic-drop.

### Exact prompt (paste into NotebookLM chat)
```
From my source, create a 5-question self-test that gets progressively harder,
then hide the answers below a line so I can check myself afterwards. Focus on the
concepts I'm most likely to be examined on, and cite the section each question
comes from.
```
*(Optional tutor prompt to show Learning Guide):*
```
Act as my tutor for this material. Explain "encoding vs. retrieval" using a simple
everyday analogy, then ask me two questions to check I understood. Do not give me
the answers until I respond.
```

### The wow moment
Playing the Audio Overview. Say: *"That's your own lecture notes, as a podcast you can revise to on the bus."*

### Honest caveat to say aloud
"It only knows what you upload and stays inside those sources — which is the point — but that also means it won't add outside context unless you give it."

### Fallback
If audio won't play, have the audio file downloaded locally AND a screenshot of the generated quiz/study guide in a tab.

---

## 🎬 DEMO 3 — Gmail + Calendar + Meet, end to end (free account)
**Point it proves:** 2.3 AI with email, scheduling & meeting prep
**Tools (free):** [Gemini app](https://gemini.google.com) + Gmail + Google Calendar + Google Meet
**Time:** ~2 min · **Wow factor:** draft → calendar event → Meet link → sent, in about a minute, no back-and-forth typing.

> **Honesty note for the audience:** The deepest AI features here (auto-finding slots across colleagues' calendars, auto Meet transcription) are **paid Google Workspace** features. This demo deliberately uses only what a **free personal account** gives you, with the free Gemini app as the "brain."

### Steps (live)
1. **Draft (Gemini app):** paste the prompt below → get a clean invite email.
2. **Email (Gmail):** paste the draft into a new email to yourself/a colleague. Because it names a date/time, Gmail surfaces **"Add to Calendar"** — click it; the event auto-fills.
   - *If it doesn't surface:* in Gmail's compose, use **"Help me write"** to refine, then create the event manually — still fast.
3. **Meet (Calendar):** open the new event → **Add Google Meet video conferencing** → a link is generated → **Save** to send invites.
4. **Prep bonus:** back in Gemini, paste the second prompt to get an agenda + talking points for the meeting.

### Exact prompts
**Prompt A — draft the invite (Gemini app):**
```
Write a short, friendly meeting invitation email.
Purpose: kick-off for our "AI in Our Lives" learning session.
Attendees: my team (5 people).
Proposed time: next Tuesday 3:00–3:45 PM.
Include: a one-line purpose, a 3-bullet agenda, and a line saying a Google Meet
link is attached. Keep it under 120 words, warm but professional.
```
**Prompt B — meeting prep (Gemini app):**
```
Create a 45-minute agenda for the session above with rough timings, 3 discussion
questions to open the room, and a list of what I should prepare beforehand.
```

### The wow moment
The one-tap **"Add to Calendar"** jump from an email's text to a real event. Say: *"I never opened the calendar or typed a date twice."*

### Honest caveat to say aloud
"On a free account the AI helps at each step but doesn't fully automate across people's calendars — that's a paid Workspace feature. Still, this removes most of the busywork."

### Fallback (fully offline-safe)
Record a 45-second screen capture of the whole flow beforehand and play it. Live demos of email are the most fragile, so a recorded backup here is strongly recommended.

---

## 🎬 DEMO 4 — AI poster / EDM for THIS session (case study)
**Point it proves:** 2.5 AI EDM/poster creation
**Tools (free):** [Canva](https://www.canva.com) (Magic Design) · [Ideogram](https://ideogram.ai) (best for text-in-image) · Microsoft Designer (alt)
**Time:** ~2 min · **Wow factor:** a designed, editable event poster from one description.

### Source material
Use `demo-materials/demo4-poster-brief.md` — the full creative brief for promoting today's session. Copy the relevant prompt from it.

### Steps (live) — Canva path (recommended for editability)
1. Canva → search **"Poster"** → **Magic Design** / **"Design with AI."**
2. Paste the prompt below.
3. Pick one of the generated layouts → it opens fully editable.
4. Live-edit one thing (change the date or a colour) to prove it's not a flat image.
5. **Download** as PNG/PDF. Mention the EDM angle: "Resize to 'Email header' with one click for the EDM version."

### Steps (optional compare) — Ideogram path (for text baked into art)
1. Ideogram → paste the second prompt.
2. Show how the headline text renders *inside* a stylised image (AI's traditional weak spot).
3. Contrast: "Canva = editable & on-brand; Ideogram = artistic, but text is baked in and must be proofread."

### Exact prompts
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
**Prompt B — Ideogram (text-in-image):**
```
A vibrant, modern event poster with the bold headline text "USING AI IN OUR LIVES"
clearly readable at the top, subtitle "Free tools, real results — 45-min session"
below. Flat vector illustration style, blue and teal, a glowing lightbulb made of
circuit lines, plenty of clean space. High legibility text.
```

### The wow moment
Live-editing the date on the Canva design. Say: *"Try that with a poster a designer sent you as a flat JPG."*

### Honest caveat to say aloud
"Always proofread text in AI images — it still misspells words — and remember free tiers usually can't be used commercially and may add a watermark."

### Fallback
Pre-make one Canva poster and one Ideogram poster; show those and explain the prompts if live generation stalls.

---

## Bonus (no live demo, but give them the prompt) — 2.6 AI Video
If someone asks, offer this to try at home in the **free Gemini app (Veo)** or **Canva**:
```
Create a short 8-second video: a cozy desk at night, a laptop glowing, a cup of tea
steaming, gentle camera push-in, warm cinematic lighting, calm mood. No text.
```
Say: "Free video is short, rate-limited, watermarked on some tools, and not for commercial use — but it's astonishing for a text prompt."

---

## Demo timing summary
| Demo | Topic | Live time | Must pre-generate? |
|---|---|---|---|
| 1 | Notes → slides (Gamma) | ~2 min | No (but have fallback deck) |
| 2 | Study notes → quiz + podcast (NotebookLM) | ~2 min | **YES — the audio** |
| 3 | Gmail + Calendar + Meet | ~2 min | Recommended: screen recording |
| 4 | Poster/EDM (Canva/Ideogram) | ~2 min | Optional compare poster |

**Total live demo time ≈ 8 min**, woven into the deck at slides 9, 11, 13, and 17.
