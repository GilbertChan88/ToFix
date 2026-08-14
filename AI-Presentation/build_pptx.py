#!/usr/bin/env python3
"""
Build the "Using AI in Our Lives" PowerPoint deck with a clean blue/teal theme.
Generates 24 slides matching 01-presentation-with-speaker-notes.md, with speaker
notes embedded in each slide's notes pane.

Usage:  python3 build_pptx.py
Output: Using-AI-in-Our-Lives.pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ---------- Theme ----------
NAVY      = RGBColor(0x0F, 0x2A, 0x43)   # deep navy (titles / dark bg)
BLUE      = RGBColor(0x1E, 0x6F, 0xB8)   # primary blue
TEAL      = RGBColor(0x18, 0xB6, 0xB0)   # accent teal
LIGHT_BG  = RGBColor(0xF4, 0xF8, 0xFB)   # off-white slide bg
INK       = RGBColor(0x22, 0x2B, 0x33)   # body text
MUTED     = RGBColor(0x5B, 0x6B, 0x79)   # muted text
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)

FONT = "Calibri"

SW, SH = Inches(13.333), Inches(7.5)     # 16:9 widescreen

prs = Presentation()
prs.slide_width = SW
prs.slide_height = SH
BLANK = prs.slide_layouts[6]


def add_slide():
    return prs.slides.add_slide(BLANK)


def bg(slide, color):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = color


def rect(slide, x, y, w, h, color, line=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
    shp.shadow.inherit = False
    return shp


def textbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    return tb, tf


def set_run(run, text, size, color, bold=False, italic=False):
    run.text = text
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def add_bullets(tf, bullets, size=20, color=INK, gap=10):
    """bullets: list of (text, level) or plain strings (level 0)."""
    first = True
    for item in bullets:
        if isinstance(item, tuple):
            text, level = item
        else:
            text, level = item, 0
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.level = level
        p.space_after = Pt(gap)
        p.space_before = Pt(0)
        run = p.add_run()
        bullet_char = "•  " if level == 0 else "–  "
        set_run(run, bullet_char + text, size - (level * 2), color,
                bold=(level == 0))
        if level == 0:
            run.font.color.rgb = INK
        else:
            run.font.color.rgb = MUTED


def accent_bar(slide):
    """Thin teal accent bar on the left of a content slide."""
    rect(slide, Inches(0), Inches(0), Inches(0.18), SH, TEAL)


def kicker(slide, text, y=Inches(0.55)):
    tb, tf = textbox(slide, Inches(0.7), y, Inches(11), Inches(0.5))
    p = tf.paragraphs[0]
    r = p.add_run()
    set_run(r, text.upper(), 13, TEAL, bold=True)
    return tb


def title_on_slide(slide, text, y=Inches(0.95)):
    tb, tf = textbox(slide, Inches(0.7), y, Inches(12), Inches(1.2))
    p = tf.paragraphs[0]
    r = p.add_run()
    set_run(r, text, 34, NAVY, bold=True)
    return tb


# =========================================================
# SLIDE BUILDERS
# =========================================================

def title_slide(title, subtitle, footer):
    s = add_slide()
    bg(s, NAVY)
    # teal accent block
    rect(s, Inches(0), Inches(0), SW, Inches(0.25), TEAL)
    rect(s, Inches(0), SH - Inches(0.25), SW, Inches(0.25), BLUE)
    # decorative dot grid (simple circles)
    for i in range(6):
        c = s.shapes.add_shape(MSO_SHAPE.OVAL,
                               Inches(10.4 + (i % 3) * 0.55),
                               Inches(0.9 + (i // 3) * 0.55),
                               Inches(0.28), Inches(0.28))
        c.fill.solid()
        c.fill.fore_color.rgb = TEAL if i % 2 == 0 else BLUE
        c.line.fill.background()
        c.shadow.inherit = False

    tb, tf = textbox(s, Inches(0.9), Inches(2.6), Inches(11.5), Inches(2), MSO_ANCHOR.TOP)
    p = tf.paragraphs[0]
    r = p.add_run()
    set_run(r, title, 54, WHITE, bold=True)
    p2 = tf.add_paragraph()
    p2.space_before = Pt(14)
    r2 = p2.add_run()
    set_run(r2, subtitle, 24, TEAL, italic=False)

    tbf, tff = textbox(s, Inches(0.9), SH - Inches(1.2), Inches(11.5), Inches(0.6))
    rp = tff.paragraphs[0]
    rr = rp.add_run()
    set_run(rr, footer, 16, RGBColor(0xB8, 0xC7, 0xD4))
    return s


def section_slide(number, title):
    s = add_slide()
    bg(s, BLUE)
    rect(s, Inches(0), Inches(0), Inches(0.35), SH, TEAL)
    tb, tf = textbox(s, Inches(1.0), Inches(2.7), Inches(11), Inches(2), MSO_ANCHOR.TOP)
    p = tf.paragraphs[0]
    r = p.add_run()
    set_run(r, number, 22, RGBColor(0xC9, 0xE8, 0xF0), bold=True)
    p2 = tf.add_paragraph()
    p2.space_before = Pt(8)
    r2 = p2.add_run()
    set_run(r2, title, 44, WHITE, bold=True)
    return s


def content_slide(kick, title, bullets, note, size=22):
    s = add_slide()
    bg(s, LIGHT_BG)
    accent_bar(s)
    if kick:
        kicker(s, kick)
    title_on_slide(s, title)
    # underline accent
    rect(s, Inches(0.72), Inches(1.95), Inches(1.4), Inches(0.06), TEAL)
    tb, tf = textbox(s, Inches(0.7), Inches(2.25), Inches(12), Inches(4.8))
    add_bullets(tf, bullets, size=size)
    notes(s, note)
    return s


def demo_slide(title, bullets, note):
    s = add_slide()
    bg(s, LIGHT_BG)
    # bold teal side panel to signal a DEMO
    rect(s, Inches(0), Inches(0), Inches(3.4), SH, TEAL)
    tb, tf = textbox(s, Inches(0.35), Inches(2.7), Inches(2.8), Inches(2))
    p = tf.paragraphs[0]
    r = p.add_run()
    set_run(r, "🎬", 54, WHITE, bold=True)
    p2 = tf.add_paragraph()
    r2 = p2.add_run()
    set_run(r2, "LIVE\nDEMO", 30, WHITE, bold=True)
    # title + bullets on right
    tbt, tft = textbox(s, Inches(3.8), Inches(0.9), Inches(9), Inches(1.2))
    pt = tft.paragraphs[0]
    rt = pt.add_run()
    set_run(rt, title, 30, NAVY, bold=True)
    rect(s, Inches(3.82), Inches(2.0), Inches(1.4), Inches(0.06), BLUE)
    tbb, tfb = textbox(s, Inches(3.8), Inches(2.3), Inches(9), Inches(4.6))
    add_bullets(tfb, bullets, size=22)
    notes(s, note)
    return s


def table_slide(kick, title, headers, rows, note, col_widths=None):
    s = add_slide()
    bg(s, LIGHT_BG)
    accent_bar(s)
    if kick:
        kicker(s, kick)
    title_on_slide(s, title)
    rect(s, Inches(0.72), Inches(1.95), Inches(1.4), Inches(0.06), TEAL)
    nrows = len(rows) + 1
    ncols = len(headers)
    left, top = Inches(0.7), Inches(2.25)
    width, height = Inches(12), Inches(0.55) * nrows
    gtbl = s.shapes.add_table(nrows, ncols, left, top, width, height).table
    if col_widths:
        for i, w in enumerate(col_widths):
            gtbl.columns[i].width = Inches(w)
    # header
    for j, h in enumerate(headers):
        cell = gtbl.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        cell.margin_left = Inches(0.12)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        para = cell.text_frame.paragraphs[0]
        run = para.add_run()
        set_run(run, h, 16, WHITE, bold=True)
    # body
    for i, row in enumerate(rows, start=1):
        for j, val in enumerate(row):
            cell = gtbl.cell(i, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = WHITE if i % 2 else RGBColor(0xE9, 0xF1, 0xF6)
            cell.margin_left = Inches(0.12)
            cell.margin_top = Inches(0.04)
            cell.margin_bottom = Inches(0.04)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            para = cell.text_frame.paragraphs[0]
            run = para.add_run()
            set_run(run, val, 13.5, INK, bold=(j == 0))
    notes(s, note)
    return s


# =========================================================
# BUILD THE DECK
# =========================================================

# --- Slide 1: Title ---
title_slide(
    "Using AI in Our Lives",
    "A practical, no-hype tour — using only free tools",
    "[Your name]  ·  [Date]  ·  45-minute sharing session",
)
notes(prs.slides[-1],
    "Welcome. In the next 45 minutes I'm not going to sell you on AI, and I'm not "
    "going to scare you about it. I'll show what free AI tools can genuinely do for "
    "everyday things — slides, studying, email, holidays. Everything today is usable "
    "tonight, for free, with an account you probably already have. Four live demos, "
    "so expect a few 'oh, it actually did that' moments.")

# --- Slide 2: Ground rules ---
content_slide("Opening", "Ground rules for today",
    ["Free tools only — no credit card",
     "Honest pros and cons for every tool",
     "4 live demos woven throughout",
     "Ask questions anytime"],
    "Three ground rules. One: everything is free-tier. Two: I'll always give the "
    "downside too — every tool has one. Three: interrupt me, this works best as a "
    "conversation. And remember: AI makes confident mistakes, so treat it as a very "
    "fast intern, not an oracle. We'll return to that at the end.")

# --- Slide 3: Agenda ---
content_slide("Opening", "What we'll cover",
    ["The story of AI (2 min)",
     "8 everyday jobs AI does well",
     "Live demos: slides · study · email · poster",
     "Ethics & pitfalls"],
    "Here's the map. A short history, then the main event: eight everyday jobs and "
    "the best free tool for each. Four come with a live demo. We finish on the stuff "
    "nobody likes to talk about — privacy, accuracy, and where to be careful.")

# --- Section 1 ---
section_slide("Section 1", "The Evolution of AI")
notes(prs.slides[-1], "A very short history so we understand how we got here.")

# --- Slide 4 ---
content_slide("Evolution of AI", "AI didn't start with ChatGPT",
    ["1950s: the idea is born",
     "1980s–90s: rules & expert systems",
     "2010s: the machine-learning wave",
     "2022 →: generative AI for everyone"],
    "AI is older than most think — the term was coined in 1956. For decades it was "
    "expert systems: humans hand-coding thousands of if-this-then-that rules, brittle "
    "and expensive. The 2010s brought machine learning — systems that learn patterns "
    "from data (spam filters, photo tagging, recommendations). The big shift for us was "
    "late 2022, when generative AI — tools that CREATE text, images, audio — became "
    "usable by anyone through a chat box. That's when AI left the lab and hit our phones.")

# --- Slide 5 ---
content_slide("Evolution of AI", "Why it suddenly feels everywhere",
    ["Bigger models + far more data",
     "Chat interface = no manual needed",
     "It now sees, hears, and speaks",
     "Built into apps you already use"],
    "Why now? Four things converged. Models got dramatically larger and trained on far "
    "more data. The interface became plain conversation. Models became multimodal — they "
    "read your PDF, look at a photo, listen, and talk back. And it's baked into Gmail, "
    "your keyboard, your browser. You don't 'go to' AI anymore; it comes to you. The "
    "skill that matters now isn't coding — it's knowing what to ask and how to check it.")

# --- Slide 6 ---
content_slide("Evolution of AI", "The one mental model to keep",
    ["AI = a fast, confident, well-read intern",
     "Brilliant first drafts in seconds",
     "But sometimes confidently wrong",
     "You always stay the editor"],
    "If you remember one thing, make it this. Treat AI like a fast, well-read intern who "
    "never sleeps. Great first draft in seconds — but it can be confidently wrong, and it "
    "doesn't know your context unless you tell it. You are always the editor and final "
    "decision-maker. Keep that frame and you get the benefit without the burns.")

# --- Section 2 ---
section_slide("Section 2", "8 Everyday Jobs AI Does Well")
notes(prs.slides[-1], "For each job: the free tool I'd reach for first, an alternative "
      "or two, and the catch.")

# --- Slide 7 ---
content_slide("Overview", "The everyday AI toolkit",
    ["Slides · Study · Email/Calendar",
     "Assignments · Posters · Video",
     "Travel · Daily life",
     "All on free tiers"],
    "Here are the eight jobs. Notice a theme: you rarely need a dedicated app. Two free "
    "general assistants — ChatGPT and Google Gemini — plus Canva and NotebookLM cover "
    "about 90% of this. Let's start with something everyone here does: making slides.")

# --- Slide 8: 2.1 ---
content_slide("2.1 Presentation preparation", "Make slides in seconds",
    ["Gamma — prompt → full designed deck",
     "Canva — best truly-free, templates",
     "Copilot / Gemini — inside Office / Google",
     "Catch: fact-check & re-style to your brand"],
    "First job: making a presentation — like this one. The standout is Gamma: paste your "
    "notes and ~30 seconds later you have a designed 10–15 slide deck. Canva Magic Design "
    "is the best FULLY free option with thousands of templates. If you live in PowerPoint "
    "or Google Slides, Copilot and Gemini build slides right inside them. The catch: "
    "AI decks can be generic and occasionally invent a statistic — re-style and check "
    "every number. This deck is what we'll build in Demo 1.")

# --- Slide 9: DEMO 1 ---
demo_slide("Demo 1 — Notes → stunning slides",
    ["Source: a page of plain notes",
     "Tool: Gamma (free)",
     "Watch: 30 seconds to a designed deck",
     "Wow: swap the theme live to restyle instantly"],
    "Let's see it. I've got a page of rough notes (demo1-source-reading.md). I paste them "
    "into Gamma with a specific prompt and ask for an 8-slide deck. While it generates, "
    "notice it chooses layouts, pulls images, writes headlines. [Generate.] Under a minute "
    "from a wall of text to something presentable. I'd tweak colours and fix any invented "
    "fact — minutes of polish, not hours of building. Full prompt in the run-sheet.")

# --- Slide 10: 2.2 ---
content_slide("2.2 AI for students' study", "Turn your notes into a tutor",
    ["NotebookLM — grounded in YOUR notes",
     "Summaries · quizzes · flashcards · mind maps",
     "Audio Overview = your notes as a podcast",
     "Catch: only as good as your sources"],
    "Second job: studying. Top pick is NotebookLM from Google — free with any Google "
    "account. Unlike a normal chatbot, it only answers from documents YOU upload and cites "
    "the exact line, so it rarely makes things up. Upload notes, a chapter, even a YouTube "
    "lecture, and get summaries, quizzes, flashcards, a mind map, a study guide. The "
    "showstopper is the Audio Overview — your notes as a two-host podcast for the bus. "
    "Catch: rubbish in, rubbish out — feed it good sources.")

# --- Slide 11: DEMO 2 ---
demo_slide("Demo 2 — Your notes become a podcast",
    ["Upload a reading",
     "Generate: study guide + quiz",
     "Play: 20 sec of the Audio Overview",
     "Pre-generate the audio before the session!"],
    "The wow moment for students. I've uploaded a reading (demo2-study-source.md). One click "
    "gives a study guide and a quiz drawn straight from the text. Now the fun part — I "
    "pre-generated an Audio Overview because it takes a few minutes. [Play 15–20 sec.] "
    "Two AI hosts discussing YOUR material naturally. Imagine revising by listening to a "
    "podcast made from your own lecture notes. That's the jaw-drop.")

# --- Slide 12: 2.3 ---
content_slide("2.3 Email · scheduling · meetings", "Tame the inbox-calendar treadmill",
    ["Gmail: 'Help me write' a reply",
     "Gmail → Calendar: one-tap 'Add to Calendar'",
     "Meet: auto notes & recap",
     "Know the free vs paid line"],
    "Third job: the email-calendar-meeting treadmill. On a free personal Google account "
    "you already get a lot: Gmail drafts and refines replies, and when an email mentions a "
    "date it offers one-tap 'Add to Calendar'. In Meet, AI can take notes and give a recap. "
    "Honesty moment: the deepest integrations — finding slots across colleagues' calendars, "
    "auto Meet transcription — are PAID Workspace features. So I'll show a version that "
    "works on a FREE account using the free Gemini app as the glue.")

# --- Slide 13: DEMO 3 ---
demo_slide("Demo 3 — Gmail + Calendar + Meet",
    ["Draft the invite email (Gemini)",
     "One tap → Calendar event",
     "Add Meet link → share",
     "Works on a free account"],
    "A realistic flow on a free account. Step one: in the free Gemini app I ask it to draft "
    "a meeting invitation email. Step two: drop it into Gmail; because it names a day and "
    "time, Gmail shows 'Add to Calendar' — one tap and the event exists. Step three: in "
    "Calendar I hit 'Add Google Meet', generating the link, and the invite goes out. Three "
    "tools, one minute, zero back-and-forth. Full click-path in the run-sheet.")

# --- Slide 14: 2.4 ---
content_slide("2.4 Assignment guidance", "Learn the work — don't outsource it",
    ["Ask AI to be a tutor, not a ghost-writer",
     "'Explain the question, don't answer it'",
     "Break the task into steps",
     "Socratic mode: it quizzes YOU"],
    "Fourth job — about integrity as much as productivity: using AI to UNDERSTAND an "
    "assignment, not do it for you. The trick is the prompt: 'Act as a tutor. Explain what "
    "this question is really asking, list the key concepts, and quiz me — do not write the "
    "answer.' NotebookLM's Learning Guide and ChatGPT's study mode both do this. You learn "
    "the material and keep a defensible, honest workflow.")

# --- Slide 15 ---
content_slide("2.4 Assignment guidance", "The 'tutor, not author' prompt",
    ["Paste your assignment brief",
     "'Be my Socratic tutor…'",
     "It explains + questions you",
     "You write the actual work"],
    "Here's the prompt (also in your handout). Notice it forbids the AI from writing the "
    "answer and forces it to check your understanding. This is how you use AI to get "
    "smarter instead of getting caught. If your school has an AI policy, this workflow "
    "usually sits on the right side of it — but check, because they vary.")

# --- Slide 16: 2.5 ---
content_slide("2.5 EDM & poster creation", "Design without a designer",
    ["Canva — fast, editable, free",
     "Microsoft Designer — genuinely free",
     "Ideogram — best text INSIDE the image",
     "Catch: proofread text & check licensing"],
    "Fifth job: posters and EDMs (electronic direct mail). For most people Canva Magic "
    "Design is fastest — describe your poster, get a fully editable design. Microsoft "
    "Designer is completely free and good for social graphics. For readable text INSIDE an "
    "AI image — normally AI's weak spot — Ideogram is the specialist. Two catches: AI still "
    "misspells words in images, so proofread; and free tiers usually forbid commercial use "
    "and may add a watermark. Let's make one using this session as the case study.")

# --- Slide 17: DEMO 4 ---
demo_slide("Demo 4 — Poster for THIS session",
    ["Case study: today's talk",
     "Tool: Canva (or Ideogram)",
     "Prompt → editable poster in ~90 sec",
     "Wow: live-edit the date on a finished design"],
    "Meta moment: let's make the promotional poster for this exact session. I paste the "
    "brief — title, date, audience, vibe — into Canva's AI (demo4-poster-brief.md). "
    "[Generate.] Several editable layouts appear. I pick one and, because it's editable, I "
    "fix the date or swap a colour in seconds. For headline text baked into the image, I'd "
    "use Ideogram — I'll show a pre-made one to compare. Proofread, download, done.")

# --- Slide 18: 2.6 ---
content_slide("2.6 AI video creation", "From text to moving pictures",
    ["Canva / CapCut — easiest, watermark-free path",
     "Google Veo (via Gemini) — most realistic clips",
     "Runway / Kling / Luma — creative control",
     "Catch: short, limited, non-commercial on free"],
    "Sixth job: video — the fastest-moving area, so treat specifics as 'true today'. For "
    "turning a script or slides into narrated video, Canva and CapCut are friendliest and "
    "export without watermark. For jaw-dropping generated clips from text, Google Veo (via "
    "the free Gemini app, small daily allowance) is most realistic and even generates sound. "
    "Runway, Kling, Luma give more control. Reality check: free video is short, rate-limited, "
    "often watermarked, and NOT licensed for commercial use. Prompt's in your handout.")

# --- Slide 19: 2.7 ---
content_slide("2.7 Holiday planning", "Your instant travel agent",
    ["ChatGPT / Gemini — day-by-day itineraries",
     "Wonderplan · Google Travel — free planners",
     "Give it: dates, budget, pace, tastes",
     "Catch: verify prices, hours, openings"],
    "Seventh — the fun one. A general assistant like ChatGPT or Gemini turns a vague idea — "
    "'10 relaxed days in Japan, food-focused, mid-budget' — into a day-by-day plan in "
    "seconds. Dedicated free tools like Wonderplan and Google Travel add maps and budgets. "
    "The secret is detail in your prompt. The big catch: AI's prices, hours, and 'this place "
    "exists' claims can be stale or invented — always verify before booking. Plan, don't pay.")

# --- Slide 20: 2.8 ---
content_slide("2.8 AI in daily life", "The small wins that add up",
    ["Meals from what's in your fridge",
     "Explain letters, contracts, jargon",
     "Summarise long articles / PDFs",
     "Draft awkward messages · translate · declutter"],
    "Eighth: small daily wins. Snap your fridge, get three dinner ideas. Paste a confusing "
    "letter: 'explain this like I'm busy, what do I do?' Drop a 40-page PDF, get five key "
    "points. Soften an awkward message, translate a menu with your camera, write the poem "
    "you're dreading. Individually minor; together they hand back real time each week. One "
    "caution: don't paste passwords, ID numbers, medical or financial details into free AI.")

# --- Section 3 ---
section_slide("Section 3", "Doing It Responsibly")

# --- Slide 21 ---
content_slide("Responsibly", "The honest limitations",
    ["Hallucinations — confident, but wrong",
     "Stale info — check dates & prices",
     "Bias — reflects its training data",
     "Privacy — free is not private"],
    "To stay balanced, four things to genuinely watch. Hallucinations: AI invents facts, "
    "citations and quotes with total confidence — verify anything that matters. Stale or "
    "wrong info, especially prices and current events. Bias: it mirrors its training data. "
    "Privacy: on free tiers your inputs may train the model, so never paste confidential or "
    "personal data. Not reasons to avoid AI — reasons to stay the editor.")

# --- Slide 22 ---
content_slide("Responsibly", "Five habits of good AI users",
    ["Give context & an example of 'good'",
     "Ask for its reasoning / sources",
     "Verify facts against a second source",
     "Iterate — don't accept draft 1",
     "Keep the final decision human"],
    "How do people who get great results use it? Five habits. Give context and an example of "
    "what 'good' looks like. Ask it to show reasoning or sources. Verify anything factual "
    "against a second source. Treat the first answer as a starting point and push back. And "
    "keep the final judgement human. Do these and you're ahead of most people using these tools.")

# --- Section 4 / Close ---
section_slide("Section 4", "Your Starter Kit & Close")

# --- Slide 23 ---
content_slide("Close", "Your starter kit (all free)",
    ["ChatGPT / Gemini — everyday assistant",
     "NotebookLM — study & documents",
     "Canva — anything visual",
     "Gamma — slides"],
    "If you do nothing else, install these four. A general assistant for daily questions, "
    "drafting and travel. NotebookLM for study and documents. Canva for posters, EDMs and "
    "simple video. Gamma for slides. All free. Pick one job from today and try it this week "
    "— that's how it sticks.")

# --- Slide 24 ---
content_slide("Close", "One challenge before you go",
    ["Tonight: automate one 15-min task",
     "Notice what it nailed — and what you fixed",
     "That gap is the skill",
     "Questions?"],
    "My challenge: tonight, pick one task that eats 15 minutes — a reply, a summary, a plan — "
    "and hand it to a free AI. Notice what it nailed and what you had to fix. That gap IS the "
    "skill. Thank you — I'd love your questions, especially on any of the demos.")

prs.save("Using-AI-in-Our-Lives.pptx")
print(f"Saved Using-AI-in-Our-Lives.pptx with {len(prs.slides._sldIdLst)} slides.")
