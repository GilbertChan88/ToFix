#!/usr/bin/env python3
"""
Build the "Using AI in Our Lives" PowerPoint deck — VISUAL UPGRADE.
A richer design system: tool cards, tool chips, a timeline, do/don't columns,
free-vs-paid comparisons, warning callouts, icon badges, and slide footers.
More on-slide content and significantly expanded speaker notes.

Usage:  python3 build_pptx.py
Output: Using-AI-in-Our-Lives.pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

# ---------------- Theme ----------------
NAVY     = RGBColor(0x0F, 0x2A, 0x43)
NAVY2    = RGBColor(0x15, 0x3A, 0x5C)
BLUE     = RGBColor(0x1E, 0x6F, 0xB8)
BLUE_LT  = RGBColor(0xDF, 0xEC, 0xF6)
TEAL     = RGBColor(0x14, 0xB8, 0xB0)
TEAL_LT  = RGBColor(0xDD, 0xF4, 0xF2)
AMBER    = RGBColor(0xE8, 0x9A, 0x18)
AMBER_BG = RGBColor(0xFB, 0xF1, 0xDA)
GREEN    = RGBColor(0x2E, 0x9E, 0x5B)
LIGHT_BG = RGBColor(0xF5, 0xF9, 0xFC)
CARD_BG  = RGBColor(0xFF, 0xFF, 0xFF)
CARD_BRD = RGBColor(0xD5, 0xE1, 0xEA)
INK      = RGBColor(0x24, 0x2D, 0x35)
MUTED    = RGBColor(0x5C, 0x6B, 0x79)
WHITE    = RGBColor(0xFF, 0xFF, 0xFF)
CLOUD    = RGBColor(0xC3, 0xD3, 0xDF)

FONT = "Calibri"
MONO = "Consolas"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]

# ---------------- Low-level helpers ----------------

def add_slide():
    return prs.slides.add_slide(BLANK)

def bg(slide, color):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = color

def _no_shadow(shp):
    shp.shadow.inherit = False

def rect(slide, x, y, w, h, color, line=None, line_w=None, rounded=False):
    shape = MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE
    shp = slide.shapes.add_shape(shape, x, y, w, h)
    if color is None:
        shp.fill.background()
    else:
        shp.fill.solid()
        shp.fill.fore_color.rgb = color
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = line_w or Pt(1)
    _no_shadow(shp)
    return shp

def oval(slide, x, y, d, color):
    shp = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y, d, d)
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.fill.background()
    _no_shadow(shp)
    return shp

def tbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    return tf

def run(p, text, size, color, bold=False, italic=False, font=FONT):
    r = p.add_run()
    r.text = text
    r.font.name = font
    r.font.size = Pt(size)
    r.font.color.rgb = color
    r.font.bold = bold
    r.font.italic = italic
    return r

def para(tf, first, space_after=6, space_before=0, level=0, align=None):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.space_after = Pt(space_after)
    p.space_before = Pt(space_before)
    p.level = level
    if align:
        p.alignment = align
    return p

def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text

def center_text(shp, runs, anchor=MSO_ANCHOR.MIDDLE):
    """Put centered text into a shape. runs = list of (text,size,color,bold)."""
    tf = shp.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = Pt(4); tf.margin_right = Pt(4)
    tf.margin_top = Pt(2); tf.margin_bottom = Pt(2)
    for i, (t, s, c, b) in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.CENTER
        run(p, t, s, c, bold=b)

# ---------------- Component helpers ----------------

def footer(slide, section, page):
    rect(slide, Inches(0.7), Inches(7.02), Inches(11.93), Pt(1), CARD_BRD)
    tf = tbox(slide, Inches(0.7), Inches(7.08), Inches(8), Inches(0.35))
    p = para(tf, True)
    run(p, section, 9, MUTED, bold=True)
    tf2 = tbox(slide, Inches(9), Inches(7.08), Inches(3.63), Inches(0.35))
    p2 = para(tf2, True, align=PP_ALIGN.RIGHT)
    run(p2, "Using AI in Our Lives", 9, MUTED)
    run(p2, f"   ·   {page}", 9, TEAL, bold=True)

def kicker(slide, text):
    tf = tbox(slide, Inches(0.72), Inches(0.5), Inches(11), Inches(0.4))
    p = para(tf, True)
    run(p, text.upper(), 12.5, TEAL, bold=True)

def title(slide, text, y=Inches(0.86)):
    tf = tbox(slide, Inches(0.7), y, Inches(12), Inches(1.0))
    p = para(tf, True)
    run(p, text, 30, NAVY, bold=True)
    rect(slide, Inches(0.74), Inches(1.62), Inches(1.3), Pt(4), TEAL)

def icon_badge(slide, x, y, d, color, glyph, glyph_size=18):
    oval(slide, x, y, d, color)
    tf = tbox(slide, x, y, d, d, anchor=MSO_ANCHOR.MIDDLE)
    p = para(tf, True, align=PP_ALIGN.CENTER)
    run(p, glyph, glyph_size, WHITE, bold=True)

def pill(slide, x, y, w, text, fill, txt_color=WHITE, h=Inches(0.42), size=12):
    shp = rect(slide, x, y, w, h, fill, rounded=True)
    center_text(shp, [(text, size, txt_color, True)])
    return shp

def tool_card(slide, x, y, w, h, accent, name, role, great, catch):
    """A tool comparison card: colored header, strengths (✓) and catch (⚠)."""
    card = rect(slide, x, y, w, h, CARD_BG, line=CARD_BRD, line_w=Pt(1), rounded=True)
    # header band
    hb = rect(slide, x, y, w, Inches(0.62), accent, rounded=True)
    # square off the bottom of the header by overlaying a rect
    rect(slide, x, y + Inches(0.31), w, Inches(0.31), accent)
    htf = hb.text_frame
    htf.word_wrap = True
    htf.vertical_anchor = MSO_ANCHOR.MIDDLE
    htf.margin_left = Pt(8); htf.margin_right = Pt(6)
    hp = htf.paragraphs[0]
    run(hp, name, 15, WHITE, bold=True)
    hp2 = htf.add_paragraph()
    run(hp2, role, 9.5, RGBColor(0xEA, 0xF3, 0xF8))
    # body
    tf = tbox(slide, x + Inches(0.16), y + Inches(0.78), w - Inches(0.32), h - Inches(0.9))
    p = para(tf, True, space_after=5)
    run(p, "✓ ", 12, GREEN, bold=True)
    run(p, great, 11, INK)
    p2 = para(tf, False, space_after=0, space_before=3)
    run(p2, "⚠ ", 12, AMBER, bold=True)
    run(p2, catch, 11, MUTED)

def callout(slide, x, y, w, h, glyph, text, accent=AMBER, fill=AMBER_BG):
    rect(slide, x, y, w, h, fill, rounded=True)
    rect(slide, x, y, Inches(0.12), h, accent, rounded=True)
    tf = tbox(slide, x + Inches(0.28), y + Inches(0.02), w - Inches(0.45), h, anchor=MSO_ANCHOR.MIDDLE)
    p = para(tf, True)
    run(p, f"{glyph}  ", 13, accent, bold=True)
    run(p, text, 11.5, INK, bold=False)

def prompt_box(slide, x, y, w, h, label, lines):
    rect(slide, x, y, w, h, NAVY, rounded=True)
    rect(slide, x, y, Inches(0.12), h, TEAL, rounded=True)
    tf = tbox(slide, x + Inches(0.28), y + Inches(0.12), w - Inches(0.45), h - Inches(0.2))
    p = para(tf, True, space_after=4)
    run(p, label, 10, TEAL, bold=True)
    for ln in lines:
        pp = para(tf, False, space_after=1)
        run(pp, ln, 9.5, RGBColor(0xE7, 0xEF, 0xF5), font=MONO)

def bullets(slide, x, y, w, h, items, size=15, gap=8):
    tf = tbox(slide, x, y, w, h)
    first = True
    for it in items:
        if isinstance(it, tuple):
            text, lvl = it
        else:
            text, lvl = it, 0
        p = para(tf, first, space_after=gap, level=lvl)
        first = False
        mark = "●  " if lvl == 0 else "–  "
        run(p, mark, size - lvl*2, TEAL if lvl == 0 else BLUE, bold=True)
        run(p, text, size - lvl*2, INK if lvl == 0 else MUTED, bold=False)
    return tf

def num_step(slide, x, y, w, num, head, body, accent=BLUE):
    d = Inches(0.42)
    oval(slide, x, y, d, accent)
    ntf = tbox(slide, x, y, d, d, anchor=MSO_ANCHOR.MIDDLE)
    np = para(ntf, True, align=PP_ALIGN.CENTER)
    run(np, str(num), 15, WHITE, bold=True)
    tf = tbox(slide, x + Inches(0.6), y - Inches(0.02), w - Inches(0.6), Inches(1.1))
    p = para(tf, True, space_after=2)
    run(p, head, 13, NAVY, bold=True)
    if body:
        p2 = para(tf, False, space_after=2)
        run(p2, body, 10.5, MUTED)

# ---------------- Slide templates ----------------

def s_title():
    s = add_slide(); bg(s, NAVY)
    rect(s, 0, 0, SW, Inches(0.28), TEAL)
    rect(s, 0, SH - Inches(0.28), SW, Inches(0.28), BLUE)
    # dotted circuit motif top-right
    for i in range(9):
        c = TEAL if i % 2 == 0 else BLUE
        oval(s, Inches(10.2 + (i % 3) * 0.62), Inches(0.75 + (i // 3) * 0.62), Inches(0.26), c)
    tf = tbox(s, Inches(0.9), Inches(2.35), Inches(11.5), Inches(2.0))
    p = para(tf, True, space_after=10)
    run(p, "Using AI in Our Lives", 52, WHITE, bold=True)
    p2 = para(tf, False)
    run(p2, "A practical, no-hype tour — using only free tools", 22, TEAL)
    # chips
    chips = [("🎬  4 live demos", TEAL), ("💸  Free tools only", BLUE), ("⏱  45 minutes", NAVY2)]
    cx = Inches(0.92)
    for label, col in chips:
        w = Inches(2.5)
        pill(s, cx, Inches(4.55), w, label, col, h=Inches(0.5), size=13)
        cx += w + Inches(0.2)
    tf3 = tbox(s, Inches(0.92), SH - Inches(1.05), Inches(11.5), Inches(0.5))
    p3 = para(tf3, True)
    run(p3, "[Your name]   ·   [Date]   ·   Sharing session", 15, CLOUD)
    notes(s,
        "Welcome everyone, and thanks for coming. Over the next 45 minutes I'm not going "
        "to sell you on AI, and I'm not going to scare you about it either. My goal is "
        "simple: show you what free AI tools can genuinely do for the ordinary things we "
        "all deal with — building slides, studying, wrangling email, planning a holiday. "
        "Everything I show you today is usable tonight, for free, with an account you "
        "almost certainly already have. To keep it real rather than theoretical, I've "
        "built in four live demos — so expect a few 'wait, it actually did that?' moments. "
        "Set expectations: I'll go fast, the handout has every prompt, and you don't need "
        "to follow along live — take it home and try at your own pace.")
    return s

def s_section(number, heading, items):
    s = add_slide(); bg(s, BLUE)
    rect(s, 0, 0, Inches(0.35), SH, TEAL)
    for i in range(4):
        oval(s, Inches(11.6), Inches(0.7 + i*0.5), Inches(0.22), TEAL if i % 2 else NAVY2)
    tf = tbox(s, Inches(1.0), Inches(2.3), Inches(10.5), Inches(2.5))
    p = para(tf, True, space_after=6)
    run(p, number, 20, RGBColor(0xC9, 0xE8, 0xF0), bold=True)
    p2 = para(tf, False, space_after=14)
    run(p2, heading, 42, WHITE, bold=True)
    for it in items:
        pp = para(tf, False, space_after=4)
        run(pp, "›  ", 16, TEAL, bold=True)
        run(pp, it, 15, RGBColor(0xDD, 0xEA, 0xF3))
    return s

def content_base(kick, ttl, section, page):
    s = add_slide(); bg(s, LIGHT_BG)
    rect(s, 0, 0, Inches(0.18), SH, TEAL)
    kicker(s, kick)
    title(s, ttl)
    footer(s, section, page)
    return s

# =====================================================================
# BUILD DECK
# =====================================================================

s_title()

# ---- Slide 2: ground rules ----
s = content_base("Opening", "Ground rules for today", "Opening", 2)
data = [
    (TEAL, "💸", "Free tools only", "Every tool today has a genuine free tier. No credit card, no trial traps."),
    (BLUE, "⚖️", "Honest pros & cons", "I'll always name the catch. Every tool is great at something and weak at something else."),
    (NAVY2, "💬", "Ask anytime", "Interrupt me. This works best as a conversation, not a lecture."),
]
x = Inches(0.75)
for accent, glyph, head, body in data:
    w = Inches(3.75)
    card = rect(s, x, Inches(2.15), w, Inches(2.75), CARD_BG, line=CARD_BRD, rounded=True)
    icon_badge(s, x + Inches(0.28), Inches(2.45), Inches(0.75), accent, glyph, 22)
    tf = tbox(s, x + Inches(0.28), Inches(3.4), w - Inches(0.56), Inches(1.4))
    p = para(tf, True, space_after=5)
    run(p, head, 15.5, NAVY, bold=True)
    p2 = para(tf, False)
    run(p2, body, 11.5, MUTED)
    x += w + Inches(0.29)
callout(s, Inches(0.75), Inches(5.25), Inches(11.83), Inches(0.9), "🧭",
        "One mental model for the whole session: treat AI like a fast, confident intern — brilliant first drafts, but you stay the editor.",
        accent=BLUE, fill=BLUE_LT)
notes(s,
    "Three quick ground rules before we dive in. One: everything is free-tier — I'm "
    "assuming you don't want to spend a cent, so I've deliberately excluded paid tools. "
    "Two: I'll always give you the downside, not just the shiny demo. Marketing shows you "
    "the best case; I'll show you where each tool falls over so you're not disappointed "
    "later. Three: please interrupt me — questions make this far more useful. And hold on "
    "to that mental model at the bottom: a fast, confident intern. It gives you a great "
    "first draft in seconds, it never gets tired, but it will occasionally make things up "
    "with total confidence. Your job shifts from 'doing' to 'directing and checking'. "
    "Keep that frame and you'll get all the upside without the classic mistakes.")

# ---- Slide 3: agenda ----
s = content_base("Opening", "What we'll cover", "Opening", 3)
agenda = [
    ("1", "The story of AI", "How we got from 1950s theory to AI on your phone", "~2 min"),
    ("2", "8 everyday jobs", "The best free tool for each — with the honest catch", "~28 min"),
    ("🎬", "4 live demos", "Slides · Study · Email · Poster", "woven in"),
    ("3", "Doing it responsibly", "Limitations, privacy, and 5 habits of good users", "~3 min"),
]
y = Inches(2.2)
for num, head, body, tmark in agenda:
    rect(s, Inches(0.75), y, Inches(11.83), Inches(1.02), CARD_BG, line=CARD_BRD, rounded=True)
    icon_badge(s, Inches(1.0), y + Inches(0.24), Inches(0.55), BLUE if num.isdigit() else TEAL, num, 17)
    tf = tbox(s, Inches(1.85), y + Inches(0.12), Inches(8.3), Inches(0.85), anchor=MSO_ANCHOR.MIDDLE)
    p = para(tf, True, space_after=2)
    run(p, head, 15, NAVY, bold=True)
    p2 = para(tf, False)
    run(p2, body, 11, MUTED)
    tf2 = tbox(s, Inches(10.2), y, Inches(2.2), Inches(1.02), anchor=MSO_ANCHOR.MIDDLE)
    p3 = para(tf2, True, align=PP_ALIGN.RIGHT)
    run(p3, tmark, 12, TEAL, bold=True)
    y += Inches(1.16)
notes(s,
    "Here's the map for the next 45 minutes. First, a very short history — two minutes — "
    "just so we understand why this suddenly feels everywhere. Then the main event: eight "
    "everyday jobs, and for each one I'll name the free tool I'd reach for, an alternative "
    "or two, and the trade-off. Four of those jobs come with a live demo, marked with the "
    "clapperboard. We finish on the part nobody enjoys but everyone needs — the "
    "limitations, the privacy issues, and five simple habits that separate people who get "
    "great results from people who get burned. If we run short on time, the safe things to "
    "cut are the video and holiday sections; the demos stay no matter what.")

# ---- Section 1 ----
s_section("Section 1", "The Evolution of AI",
          ["From 1950s theory to generative AI for everyone",
           "Why it suddenly feels like it's everywhere",
           "The one mental model to carry through the talk"])
notes(prs.slides[-1], "A quick two-minute history so the rest of the session makes sense. "
      "I won't dwell — the point is just to show this isn't magic that appeared overnight; "
      "it's decades of work that recently crossed a usability threshold.")

# ---- Slide 4: timeline ----
s = content_base("Evolution of AI", "AI didn't start with ChatGPT", "Evolution of AI", 5)
rect(s, Inches(1.0), Inches(3.35), Inches(11.3), Pt(4), CLOUD)
milestones = [
    ("1950s", "The idea", "Term coined in 1956; more theory than practice", NAVY2),
    ("1980s–90s", "Expert systems", "Humans hand-code thousands of rules — brittle", BLUE),
    ("2010s", "Machine learning", "Systems learn from data: spam filters, photo tags", TEAL),
    ("2022 →", "Generative AI", "Anyone can create text, images & audio via chat", GREEN),
]
x = Inches(1.0)
step = Inches(2.83)
for era, head, body, col in milestones:
    cx = x + Inches(0.35)
    oval(s, cx, Inches(3.2), Inches(0.34), col)
    oval(s, cx + Inches(0.08), Inches(3.28), Inches(0.18), WHITE)
    tf = tbox(s, x, Inches(2.35), step - Inches(0.2), Inches(0.7))
    p = para(tf, True, align=PP_ALIGN.LEFT)
    run(p, era, 15, col, bold=True)
    ctf = tbox(s, x, Inches(3.75), step - Inches(0.2), Inches(1.9))
    p2 = para(ctf, True, space_after=3)
    run(p2, head, 13.5, NAVY, bold=True)
    p3 = para(ctf, False)
    run(p3, body, 10.5, MUTED)
    x += step
callout(s, Inches(1.0), Inches(5.9), Inches(11.3), Inches(0.85), "💡",
        "The big shift for us was late 2022: AI left the research lab and landed in a simple chat box on everyone's phone.",
        accent=TEAL, fill=TEAL_LT)
notes(s,
    "AI is much older than most people realise — the term was coined back in 1956. For "
    "decades it lived in universities as 'expert systems': human experts would hand-code "
    "thousands of if-this-then-that rules. That approach was brilliant in narrow cases but "
    "brittle and hugely expensive to maintain. The 2010s brought the machine-learning wave "
    "— instead of coding rules by hand, we let systems learn patterns from enormous amounts "
    "of data. That's what quietly powered your spam filter, photo face-tagging, and Netflix "
    "recommendations for years. Then late 2022 was the inflection point: generative AI — "
    "tools that actually create text, images and audio — became usable by anyone through "
    "plain conversation. No code, no manual. That's the moment AI stopped being something "
    "engineers used and became something all of us use. Analogy I like: this is the "
    "'spreadsheet moment' — a capability that was specialist suddenly became everyday.")

# ---- Slide 5: why now (4 cards) ----
s = content_base("Evolution of AI", "Why it suddenly feels everywhere", "Evolution of AI", 6)
why = [
    (TEAL, "📈", "Scale", "Far bigger models trained on far more data"),
    (BLUE, "💬", "Chat interface", "Plain language in — no manual, no code needed"),
    (NAVY2, "👁", "Multimodal", "It now reads, sees, hears, and speaks back"),
    (GREEN, "🔌", "Embedded", "Built into Gmail, your keyboard, your browser"),
]
x = Inches(0.75); w = Inches(2.83)
for accent, glyph, head, body in why:
    rect(s, x, Inches(2.15), w, Inches(2.9), CARD_BG, line=CARD_BRD, rounded=True)
    icon_badge(s, x + Inches(0.28), Inches(2.42), Inches(0.72), accent, glyph, 20)
    tf = tbox(s, x + Inches(0.24), Inches(3.35), w - Inches(0.48), Inches(1.6))
    p = para(tf, True, space_after=5)
    run(p, head, 15, NAVY, bold=True)
    p2 = para(tf, False)
    run(p2, body, 11, MUTED)
    x += w + Inches(0.19)
callout(s, Inches(0.75), Inches(5.4), Inches(11.83), Inches(0.85), "🎯",
        "The skill that matters now isn't coding — it's knowing what to ask, and how to check the answer.",
        accent=BLUE, fill=BLUE_LT)
notes(s,
    "So why now, and not five years ago? Four things converged. First, scale: the models "
    "got dramatically larger and were trained on far more data, which made them "
    "surprisingly capable and general. Second, the interface became plain conversation — "
    "this is the underrated one. You no longer need to learn software; you just type or "
    "speak what you want. Third, they became multimodal: a modern assistant can read your "
    "PDF, look at a photo you snap, listen to audio, and talk back. Fourth, and most "
    "importantly for daily life, it's now embedded in tools you already use — Gmail, your "
    "phone keyboard, your browser. You don't 'go to' AI anymore; it comes to you. Put "
    "those together and you get the punchline at the bottom: the valuable skill has shifted "
    "from technical know-how to good questioning and good judgement — and that's something "
    "everyone in this room can build.")

# ---- Slide 6: mental model ----
s = content_base("Evolution of AI", "The one idea to keep all session", "Evolution of AI", 7)
big = rect(s, Inches(0.75), Inches(2.15), Inches(11.83), Inches(1.5), NAVY, rounded=True)
center_text(big, [("AI = a fast, confident, well-read intern", 26, WHITE, True),
                  ("Amazing first drafts in seconds — but you are always the editor", 14, TEAL, False)])
trio = [
    (GREEN, "✓", "Brilliant drafts", "Turns a blank page into a solid starting point instantly"),
    (AMBER, "!", "Sometimes wrong", "Can state false facts with total confidence"),
    (BLUE, "✎", "You decide", "Direct it, correct it, and make the final call"),
]
x = Inches(0.75); w = Inches(3.83)
for accent, glyph, head, body in trio:
    rect(s, x, Inches(3.95), w, Inches(2.4), CARD_BG, line=CARD_BRD, rounded=True)
    icon_badge(s, x + Inches(0.28), Inches(4.2), Inches(0.65), accent, glyph, 20)
    tf = tbox(s, x + Inches(0.24), Inches(5.05), w - Inches(0.48), Inches(1.2))
    p = para(tf, True, space_after=4)
    run(p, head, 14.5, NAVY, bold=True)
    p2 = para(tf, False)
    run(p2, body, 11, MUTED)
    x += w + Inches(0.17)
notes(s,
    "If you forget everything else today, keep this one image: AI is a fast, confident, "
    "incredibly well-read intern who never sleeps. Think about what that means "
    "practically. On the plus side, it turns a blank page into a solid first draft in "
    "seconds — that alone is transformational for anyone who's ever stared at a cursor. "
    "But an intern, however bright, can be confidently wrong, and doesn't know your "
    "specific context unless you tell them. So your role changes: you're no longer the "
    "person doing every keystroke; you're the editor and the decision-maker. You brief it "
    "well, you sanity-check the output, and you own the final result. Everything else in "
    "this talk is really just applications of this one idea. When a demo dazzles you, "
    "remember the middle card; when it stumbles, remember the first and third.")

# ---- Section 2 ----
s_section("Section 2", "8 Everyday Jobs AI Does Well",
          ["Presentations · Study · Email & meetings · Assignments",
           "Posters/EDMs · Video · Holiday planning · Daily life",
           "For each: the free pick, an alternative, and the catch"])
notes(prs.slides[-1], "Now the heart of the session. Eight jobs. A recurring theme you'll "
      "notice: you rarely need a niche app — two general assistants plus Canva and "
      "NotebookLM cover about 90% of everything here.")

# ---- Slide 7: toolkit overview ----
s = content_base("Overview", "The everyday AI toolkit", "8 Everyday Jobs", 9)
jobs = [("📊","2.1 Presentations"),("📚","2.2 Study"),("✉️","2.3 Email & meetings"),
        ("🎓","2.4 Assignments"),("🎨","2.5 Posters / EDM"),("🎬","2.6 Video"),
        ("✈️","2.7 Holiday planning"),("🏠","2.8 Daily life")]
x0 = Inches(0.75); y0 = Inches(2.15); w = Inches(2.87); h = Inches(1.35)
for i, (glyph, label) in enumerate(jobs):
    col = i % 4; rowi = i // 4
    x = x0 + col * (w + Inches(0.16)); y = y0 + rowi * (h + Inches(0.16))
    rect(s, x, y, w, h, CARD_BG, line=CARD_BRD, rounded=True)
    icon_badge(s, x + Inches(0.2), y + Inches(0.32), Inches(0.7), [TEAL,BLUE,NAVY2,GREEN][i%4], glyph, 18)
    tf = tbox(s, x + Inches(1.0), y, w - Inches(1.1), h, anchor=MSO_ANCHOR.MIDDLE)
    p = para(tf, True)
    run(p, label, 13, NAVY, bold=True)
callout(s, Inches(0.75), Inches(5.5), Inches(11.83), Inches(0.85), "⭐",
        "Install just four and you're covered: ChatGPT/Gemini · NotebookLM · Canva · Gamma.",
        accent=TEAL, fill=TEAL_LT)
notes(s,
    "Here are the eight jobs we'll walk through, and I've grouped them the way you'd "
    "actually meet them in a week — making things, learning things, communicating, and "
    "living. Before we get into specifics, notice the big idea on the bottom strip: you do "
    "not need eight different apps. Two general assistants — ChatGPT or Google Gemini — "
    "plus Canva for anything visual and NotebookLM for documents and study will handle the "
    "vast majority of what follows. So if the number of tools feels overwhelming, "
    "relax — the shortlist is short. Let's start with something every single person in "
    "this room has suffered through: building a slide deck.")

# ---- Slide 8: 2.1 presentations ----
s = content_base("2.1 Presentation preparation", "Build a deck in minutes, not hours", "8 Everyday Jobs", 10)
tool_card(s, Inches(0.75), Inches(2.05), Inches(3.75), Inches(2.65), TEAL,
          "Gamma", "Prompt / notes → full deck",
          "Designed 10–15 slide deck in ~30 sec; generous free tier",
          "Can look generic; may invent a stat — restyle & verify")
tool_card(s, Inches(4.79), Inches(2.05), Inches(3.75), Inches(2.65), BLUE,
          "Canva Magic Design", "Best truly-free option",
          "Thousands of templates; no expiry; great for brand control",
          "More manual styling than a one-prompt tool")
tool_card(s, Inches(8.83), Inches(2.05), Inches(3.75), Inches(2.65), NAVY2,
          "Copilot / Gemini", "Inside PowerPoint / Slides",
          "Builds slides where you already work",
          "Best features often need a paid plan")
callout(s, Inches(0.75), Inches(4.95), Inches(11.83), Inches(1.25), "🎬",
        "DEMO 1 up next: I'll paste a page of messy notes into Gamma and we'll watch it become a designed 8-slide deck in about 30 seconds — then restyle it with one click.",
        accent=TEAL, fill=TEAL_LT)
notes(s,
    "First job: making a presentation — exactly like this one. The standout tool here is "
    "Gamma. You give it a topic, or better, paste in your own rough notes, and about thirty "
    "seconds later you have a designed deck — layout, headlines, images, the lot. The free "
    "tier is genuinely usable, not a bait-and-switch. If you want maximum control and a "
    "completely free option with no expiry, Canva Magic Design is the pick — it's more "
    "template-driven, so slightly more hands-on, but excellent for matching a brand. And if "
    "you refuse to leave PowerPoint or Google Slides, Copilot and Gemini now build slides "
    "right inside those apps, though the best bits usually sit behind a paid plan. The catch "
    "that applies to all of them: AI decks can feel generic and will occasionally invent a "
    "statistic, so you restyle to your brand and check every number before presenting. "
    "Speaking of which — let's actually watch it happen.")

# ---- Slide 9: DEMO 1 ----
def demo_slide(page, dnum, ttl, steps, prompt_label, prompt_lines, wow, accent=TEAL):
    s = add_slide(); bg(s, LIGHT_BG)
    rect(s, 0, 0, Inches(3.5), SH, accent)
    # left panel
    tf = tbox(s, Inches(0.35), Inches(0.7), Inches(2.85), Inches(2.2))
    p = para(tf, True, space_after=2); run(p, "🎬", 46, WHITE, bold=True)
    p2 = para(tf, False, space_after=2); run(p2, f"LIVE DEMO {dnum}", 20, WHITE, bold=True)
    tf2 = tbox(s, Inches(0.35), Inches(2.7), Inches(2.85), Inches(3.8))
    pp = para(tf2, True, space_after=4); run(pp, ttl, 15, WHITE, bold=True)
    # timing chip
    pill(s, Inches(0.35), Inches(6.35), Inches(2.2), "⏱  ~2 minutes", NAVY, h=Inches(0.45), size=12)
    # right: numbered steps
    y = Inches(0.7)
    for i, (head, body) in enumerate(steps, 1):
        num_step(s, Inches(3.9), y, Inches(8.9), i, head, body, accent=BLUE)
        y += Inches(0.82)
    # prompt box
    prompt_box(s, Inches(3.9), y + Inches(0.02), Inches(8.7), Inches(1.5), prompt_label, prompt_lines)
    # wow callout
    callout(s, Inches(3.9), y + Inches(1.62), Inches(8.7), Inches(0.72), "🌟", wow, accent=accent, fill=TEAL_LT if accent==TEAL else BLUE_LT)
    return s

s = demo_slide(11, 1, "Messy notes → a stunning slide deck",
    [("Paste notes into Gamma", "Create new → 'Paste in text' → drop in the sleep notes"),
     ("Set 8 cards + tone, add the prompt", "Professional & friendly; paste the instruction below"),
     ("Generate & scroll", "~30 sec to a designed deck with images & headlines"),
     ("Swap the Theme live", "Restyle the whole deck instantly to prove it's flexible")],
    "PROMPT (into Gamma instructions box):",
    ["Turn my pasted notes into a clean, engaging 8-slide deck.",
     "One idea per slide, ≤6 words/bullet, add an image each,",
     "end with a '3 things to try tonight' slide. Don't invent stats."],
    "WOW: a wall of text becomes a presentable deck in ~40 seconds. 'That's an afternoon of work, gone.'")
notes(s,
    "Let's see it live. I've got a page of genuinely rough notes — the kind you'd scribble "
    "in a lecture or meeting; it's the 'science of sleep' reading in the handout. Step one, "
    "I paste them into Gamma using 'Paste in text' so it uses my content rather than "
    "inventing its own. Step two, I set eight cards, pick a friendly tone, and paste the "
    "short instruction you can see on screen. Step three, I hit generate — and while it "
    "works, notice it isn't just dumping my text onto slides; it's choosing layouts, "
    "writing proper headlines, and pulling in images. Give it about thirty seconds. There "
    "it is. Now the crowd-pleaser: I'll switch the theme at the top, and the entire deck "
    "restyles instantly. The honest bit: I'd still fix any fact it got creative with and "
    "match our brand colours — but that's a few minutes of polish, not an afternoon of "
    "building from a blank page. If the Wi-Fi misbehaves, I've got a finished one ready.")

# ---- Slide 10: 2.2 study ----
s = content_base("2.2 AI for students' study", "Turn your notes into a personal tutor", "8 Everyday Jobs", 12)
# NotebookLM feature strip
feat = ["📄 Summaries","❓ Quizzes","🃏 Flashcards","🧠 Mind maps","🎧 Audio Overview","🧑\u200d🏫 Learning Guide"]
x = Inches(0.75); 
for i,f in enumerate(feat):
    col=i%3; rowi=i//3
    xx=Inches(0.75)+col*Inches(3.95); yy=Inches(2.15)+rowi*Inches(0.72)
    pill(s, xx, yy, Inches(3.75), f, BLUE if i%2 else TEAL, h=Inches(0.55), size=13)
callout(s, Inches(0.75), Inches(3.75), Inches(11.83), Inches(1.0), "🎯",
        "NotebookLM (free, any Google account) answers ONLY from the sources you upload — and cites the exact line, so it rarely makes things up.",
        accent=TEAL, fill=TEAL_LT)
tool_card(s, Inches(0.75), Inches(4.95), Inches(5.8), Inches(1.55), NAVY2,
          "Alternatives", "For open-ended explaining",
          "ChatGPT / Gemini study modes for concepts & Socratic tutoring",
          "Not grounded in your notes — can hallucinate")
callout(s, Inches(6.78), Inches(4.95), Inches(5.8), Inches(1.55), "⚠️",
        "Grounded in what you give it: great sources in = great study out. Rubbish in = rubbish out.",
        accent=AMBER, fill=AMBER_BG)
notes(s,
    "Second job: studying — and this one genuinely lands with students. My top pick is "
    "NotebookLM from Google, free with any Google account. Here's what makes it different "
    "from a normal chatbot: it only answers from the documents you upload, and it cites the "
    "exact line it used, so it very rarely makes things up. You can feed it lecture notes, "
    "a textbook chapter, a stack of PDFs, even a YouTube lecture, and it will spin up "
    "summaries, quizzes, flashcards, a mind map, and a guided 'Learning Guide' tutor mode. "
    "The feature that makes jaws drop is the Audio Overview — it turns your material into a "
    "two-host podcast you can listen to on the bus. For open-ended 'explain this concept to "
    "me' work, a general assistant like ChatGPT or Gemini is better, but remember it isn't "
    "grounded in your notes and can invent things. The one rule with NotebookLM: it's only "
    "as good as your sources — feed it the real material, not a random blog. Let me show you "
    "the podcast trick.")

# ---- Slide 11: DEMO 2 ----
s = demo_slide(13, 2, "Your study notes become a quiz + a podcast",
    [("Upload a reading", "'How Memory Works' explainer → new NotebookLM notebook"),
     ("Generate a quiz / study guide", "One click in Studio; read a question aloud"),
     ("Ask a question in chat", "Show the cited, grounded answer — no hallucination"),
     ("Play the Audio Overview", "Pre-generated! 15–20 sec of two AI hosts on your notes")],
    "PROMPT (into NotebookLM chat):",
    ["Make a 5-question self-test that gets progressively harder,",
     "hide answers below a line, focus on likely exam concepts,",
     "and cite the section each question comes from."],
    "WOW: your own lecture notes, playing back as a natural two-host podcast. Pre-generate this before the session!")
notes(s,
    "This is the wow moment for anyone who studies. I've already uploaded a reading — the "
    "'how memory works' explainer from the handout. First, I'll point out the inline "
    "citations: every answer links back to the exact line in the source, which is why it "
    "doesn't drift into making things up. Then one click in the Studio panel gives me a "
    "study guide and a quiz drawn straight from the text — I'll read a question aloud. I'll "
    "drop the prompt on screen into the chat to generate a progressive self-test. And now "
    "the part that lands: I pre-generated an Audio Overview, because it takes a few minutes "
    "and you should never do that live. Listen to fifteen seconds. Two AI hosts, having a "
    "natural conversation about your material. Imagine revising for an exam by listening to "
    "a podcast made from your own lecture notes while you walk to class. Critical tip for "
    "anyone recreating this: generate the audio beforehand, and keep the file downloaded as "
    "a backup in case the room Wi-Fi is flaky.")

# ---- Slide 12: 2.3 email (free vs paid) ----
s = content_base("2.3 Email · scheduling · meetings", "Cut the inbox–calendar busywork", "8 Everyday Jobs", 14)
# Free column
rect(s, Inches(0.75), Inches(2.05), Inches(5.8), Inches(3.2), CARD_BG, line=CARD_BRD, rounded=True)
rect(s, Inches(0.75), Inches(2.05), Inches(5.8), Inches(0.6), GREEN, rounded=True)
rect(s, Inches(0.75), Inches(2.35), Inches(5.8), Inches(0.3), GREEN)
ct = rect(s, Inches(0.75), Inches(2.05), Inches(5.8), Inches(0.6), None); center_text(ct, [("✓  Free personal account", 15, WHITE, True)])
bullets(s, Inches(1.0), Inches(2.85), Inches(5.4), Inches(2.3),
        ["Gmail 'Help me write' drafts & replies",
         "Email date → one-tap 'Add to Calendar'",
         "Create Google Meet links in Calendar",
         "Gemini app: summarise, draft, prep agendas"], size=12.5, gap=9)
# Paid column
rect(s, Inches(6.78), Inches(2.05), Inches(5.8), Inches(3.2), CARD_BG, line=CARD_BRD, rounded=True)
pt = rect(s, Inches(6.78), Inches(2.05), Inches(5.8), Inches(0.6), MUTED, rounded=True); rect(s, Inches(6.78), Inches(2.35), Inches(5.8), Inches(0.3), MUTED)
center_text(pt, [("＄  Paid Workspace only", 15, WHITE, True)])
bullets(s, Inches(7.03), Inches(2.85), Inches(5.4), Inches(2.3),
        ["Auto-suggest times across colleagues' calendars",
         "'Take notes for me' transcription in Meet",
         "'Ask Gemini' live during a meeting"], size=12.5, gap=9)
callout(s, Inches(0.75), Inches(5.45), Inches(11.83), Inches(0.85), "🎬",
        "DEMO 3: draft → calendar event → Meet link, end-to-end, using only a FREE account with the Gemini app as the glue.",
        accent=BLUE, fill=BLUE_LT)
notes(s,
    "Third job: the email-calendar-meeting treadmill that eats everyone's mornings. I want "
    "to be scrupulously honest here, because this is where free-versus-paid really matters. "
    "On a free personal Google account you already get a lot, shown on the left: Gmail can "
    "draft and polish replies with 'Help me write'; when an email mentions a date, Gmail "
    "offers a one-tap 'Add to Calendar' that fills in the details; you can generate a "
    "Google Meet link inside any calendar event; and the free Gemini app will summarise "
    "threads, draft messages, and prep an agenda. The genuinely automated, cross-calendar "
    "features on the right — finding a slot that works for five colleagues, auto-"
    "transcribing a meeting, answering questions live in the call — those are paid "
    "Workspace features. So the demo I'll run deliberately uses only the free column, with "
    "the Gemini app acting as the brain that stitches the steps together. Please don't paste "
    "confidential client names into a free consumer AI while drafting.")

# ---- Slide 13: DEMO 3 ----
s = demo_slide(15, 3, "Gmail + Calendar + Meet, end-to-end (free)",
    [("Draft the invite in Gemini", "Paste Prompt A → a clean, warm invitation in seconds"),
     ("Drop into Gmail", "It names a time, so Gmail shows 'Add to Calendar' — one tap"),
     ("Add a Meet link in Calendar", "'Add Google Meet' → Save → invite goes out"),
     ("Prep the meeting", "Prompt B → instant agenda + 3 opening questions")],
    "PROMPT A (into the Gemini app):",
    ["Write a short, friendly meeting invite. Kick-off for our",
     "'AI in Our Lives' session, 5 people, next Tue 3:00–3:45 PM.",
     "One-line purpose + 3-bullet agenda + Meet link note. <120 words."],
    "WOW: from an email's text to a real calendar event in one tap — no retyping the date.",
    accent=BLUE)
notes(s,
    "Here's a realistic flow that works on a free account. Step one: in the free Gemini "
    "app I paste Prompt A and it drafts a warm, professional meeting invitation in about "
    "five seconds. Step two: I drop that draft into a new Gmail message; because it names a "
    "day and a time, Gmail recognises it and surfaces 'Add to Calendar' — one tap and the "
    "event exists, pre-filled. Step three: I open that event in Calendar, click 'Add Google "
    "Meet video conferencing', which generates the link, and save — the invite with the "
    "link goes out. Then a bonus: I paste Prompt B back in Gemini and it produces an agenda "
    "with timings and three questions to open the room. Three tools, about a minute, and I "
    "never typed the date twice or opened a blank calendar. The caveat, again: on free it "
    "assists at each step rather than fully automating across people — but it removes most "
    "of the friction. Email demos are fragile, so if anything stalls I'll switch to my "
    "recorded backup and keep talking.")

# ---- Slide 14: 2.4 assignments (do/don't) ----
s = content_base("2.4 Assignment guidance", "Use AI to learn — not to cheat", "8 Everyday Jobs", 16)
rect(s, Inches(0.75), Inches(2.05), Inches(5.8), Inches(3.0), CARD_BG, line=CARD_BRD, rounded=True)
gt = rect(s, Inches(0.75), Inches(2.05), Inches(5.8), Inches(0.6), GREEN, rounded=True); rect(s, Inches(0.75), Inches(2.35), Inches(5.8), Inches(0.3), GREEN)
center_text(gt, [("✓  DO — tutor mode", 15, WHITE, True)])
bullets(s, Inches(1.0), Inches(2.85), Inches(5.4), Inches(2.1),
        ["'Explain what the question is really asking'",
         "'List the key concepts I need'",
         "'Quiz me to check my understanding'",
         "'Break the task into steps'"], size=12.5, gap=9)
rect(s, Inches(6.78), Inches(2.05), Inches(5.8), Inches(3.0), CARD_BG, line=CARD_BRD, rounded=True)
dt = rect(s, Inches(6.78), Inches(2.05), Inches(5.8), Inches(0.6), AMBER, rounded=True); rect(s, Inches(6.78), Inches(2.35), Inches(5.8), Inches(0.3), AMBER)
center_text(dt, [("✗  DON'T — ghost-writer", 15, WHITE, True)])
bullets(s, Inches(7.03), Inches(2.85), Inches(5.4), Inches(2.1),
        ["'Write my essay for me'",
         "Submitting AI text as your own",
         "Copying answers you can't explain",
         "Skipping the actual thinking"], size=12.5, gap=9)
callout(s, Inches(0.75), Inches(5.25), Inches(11.83), Inches(0.95), "🎓",
        "NotebookLM's Learning Guide and ChatGPT/Gemini study modes both do Socratic tutoring — always check your institution's AI policy too.",
        accent=BLUE, fill=BLUE_LT)
notes(s,
    "Fourth job, and this one is about integrity as much as productivity: using AI to "
    "understand an assignment rather than to have it done for you. The entire difference "
    "lives in the prompt. On the right is the trap — 'write my essay' — which teaches you "
    "nothing and, increasingly, gets flagged. On the left is the productive pattern: ask it "
    "to act as a tutor, explain what the question is genuinely asking, list the concepts "
    "you'll need, break the task into steps, and — crucially — quiz you to check your "
    "understanding rather than handing you the answer. You end up actually learning the "
    "material, which is the whole point of the assignment, and you keep a defensible, "
    "honest workflow. NotebookLM's Learning Guide and the study modes in ChatGPT and Gemini "
    "are built for exactly this. One important caveat: AI policies vary by school and "
    "employer, so check yours — but this 'tutor, not author' approach almost always sits on "
    "the right side of the line.")

# ---- Slide 15: tutor prompt ----
s = content_base("2.4 Assignment guidance", "The 'tutor, not author' prompt", "8 Everyday Jobs", 17)
prompt_box(s, Inches(0.75), Inches(2.1), Inches(11.83), Inches(2.15),
           "COPY-PASTE PROMPT:",
           ["Act as my Socratic tutor. Here is my assignment brief: [paste it].",
            "1) Explain what the question is really asking, in plain English.",
            "2) List the key concepts and skills I'll need.",
            "3) Then ask me questions to check my understanding — one at a time.",
            "Do NOT write the answer for me. Wait for my reply before continuing."])
threep = [("1","It reframes the task","so you understand it before starting"),
          ("2","It surfaces the concepts","so you know what to revise"),
          ("3","It quizzes you","so the learning actually sticks")]
x = Inches(0.75); w=Inches(3.83)
for num,head,body in threep:
    rect(s, x, Inches(4.55), w, Inches(1.7), CARD_BG, line=CARD_BRD, rounded=True)
    icon_badge(s, x+Inches(0.24), Inches(4.78), Inches(0.55), TEAL, num, 16)
    tf=tbox(s, x+Inches(0.24), Inches(5.45), w-Inches(0.48), Inches(0.75))
    p=para(tf,True,space_after=2); run(p,head,12.5,NAVY,bold=True)
    p2=para(tf,False); run(p2,body,10.5,MUTED)
    x += w+Inches(0.17)
notes(s,
    "Here's the actual prompt to steal — it's in your handout too. Read how it's "
    "constructed, because the design is the lesson. It explicitly asks the AI to explain "
    "the question, surface the concepts, and then quiz you one question at a time — and it "
    "explicitly forbids the AI from writing the answer and tells it to wait for your reply. "
    "Those constraints flip the dynamic: instead of a vending machine that spits out an "
    "essay, you get a patient tutor that makes you do the thinking. The three cards below "
    "show why each part matters — reframing, surfacing, and testing map neatly onto how "
    "memory actually works, which, if you saw the earlier demo, is not a coincidence. Use "
    "this and you'll finish assignments understanding them, which is the only version of "
    "'using AI for schoolwork' that's both effective and honest.")

# ---- Slide 16: 2.5 poster ----
s = content_base("2.5 EDM & poster creation", "Design without a designer", "8 Everyday Jobs", 18)
tool_card(s, Inches(0.75), Inches(2.05), Inches(3.75), Inches(2.55), TEAL,
          "Canva Magic Design", "Fast + fully editable",
          "Describe it → editable design; resize poster→EDM in a click",
          "Some media/features gated on free")
tool_card(s, Inches(4.79), Inches(2.05), Inches(3.75), Inches(2.55), BLUE,
          "Microsoft Designer", "Genuinely free",
          "Strong free social graphics with no real paywall",
          "Fewer templates than Canva")
tool_card(s, Inches(8.83), Inches(2.05), Inches(3.75), Inches(2.55), NAVY2,
          "Ideogram", "Text inside the image",
          "Best at rendering readable words inside AI art",
          "Text is baked in; editing is limited")
callout(s, Inches(0.75), Inches(4.85), Inches(11.83), Inches(1.35), "⚠️",
        "Two catches for every tool: proofread every letter (AI still misspells text in images), and free tiers usually forbid commercial use and may add a watermark. DEMO 4 next: a poster for THIS session.",
        accent=AMBER, fill=AMBER_BG)
notes(s,
    "Fifth job: posters and EDMs — that's electronic direct mail, the marketing emails you "
    "get. For most people, Canva Magic Design is the fastest route: you describe the poster "
    "and it produces a fully editable layout, and you can resize the same design into an "
    "email header for the EDM version in a click. Microsoft Designer is completely free and "
    "surprisingly capable for quick social graphics. And when you specifically need a lot "
    "of readable text baked inside an AI-generated image — which is traditionally AI's weak "
    "spot — Ideogram is the specialist. Two catches apply across all of them, and they're "
    "on the amber bar: first, proofread every single letter, because image generators still "
    "misspell words; second, free tiers generally forbid commercial use and may stamp a "
    "watermark, so they're perfect for learning and internal use but not client work. Let's "
    "make one — and to be playful, let's make the poster for this very session.")

# ---- Slide 17: DEMO 4 ----
s = demo_slide(19, 4, "A poster / EDM for THIS session (case study)",
    [("Open Canva → Design with AI", "Search 'Poster' → paste the brief prompt"),
     ("Generate & pick a layout", "Several editable options appear; choose one"),
     ("Live-edit the date/colour", "Prove it's editable, not a flat image"),
     ("Download + resize to EDM", "PNG/PDF, then 'Resize' to an email header")],
    "PROMPT (into Canva Magic Design):",
    ["Modern portrait event poster. Title 'Using AI in Our Lives',",
     "subtitle 'free tools only'. Include date/time/venue + 'bring laptop'.",
     "Clean, blue & teal, white space, lightbulb motif. Keep text editable."],
    "WOW: live-edit the date on a finished poster. 'Try that with a flat JPG from a designer.'")
notes(s,
    "A nice meta moment to finish the tools: let's generate the promotional poster for this "
    "exact session. I open Canva, choose Design with AI, and paste the brief you can see — "
    "title, subtitle, the date, time and venue, the 'bring your laptop' line, and a style "
    "direction that matches our blue-and-teal theme. It generates several editable layouts; "
    "I pick one. Now the point that always lands: because it's fully editable, I can change "
    "the date or swap a colour live, in seconds — try doing that with a flat JPEG a designer "
    "emailed you. Then I download it and, to make the EDM version, I use Canva's Resize to "
    "turn the poster into an email header. If I wanted the headline text artistically baked "
    "into the image I'd show Ideogram instead, and I've got one pre-made so you can compare "
    "the trade-off: Canva is editable and on-brand; Ideogram is more artistic but the text "
    "is locked in. And remember — proofread every word.")

# ---- Slide 18: 2.6 video ----
s = content_base("2.6 AI video creation", "From a text prompt to moving pictures", "8 Everyday Jobs", 20)
tool_card(s, Inches(0.75), Inches(2.05), Inches(3.75), Inches(2.4), TEAL,
          "Canva / CapCut", "Easiest, beginner-friendly",
          "Script/slides → narrated video; watermark-free path",
          "Template-driven, not generated 'cinema'")
tool_card(s, Inches(4.79), Inches(2.05), Inches(3.75), Inches(2.4), BLUE,
          "Google Veo (Gemini)", "Most realistic clips",
          "Text → lifelike short clips, with generated sound",
          "Short clips; small free daily allowance")
tool_card(s, Inches(8.83), Inches(2.05), Inches(3.75), Inches(2.4), NAVY2,
          "Runway / Kling / Luma", "Creative control",
          "Styles, motion control, editing tools",
          "Watermarks; limited free credits")
callout(s, Inches(0.75), Inches(4.7), Inches(11.83), Inches(1.5), "⚠️",
        "Reality check for ALL free video: clips are short (seconds, not minutes), rate-limited, often watermarked, and NOT licensed for commercial use. Astonishing for learning & personal projects — not yet for client work. (No live demo — generation is slow; prompt is in your handout.)",
        accent=AMBER, fill=AMBER_BG)
notes(s,
    "Sixth job: video — and this is the fastest-moving area of the lot, so treat every "
    "specific as 'true today, check tomorrow.' If you want to turn a script or a set of "
    "slides into a narrated video, Canva and CapCut are the friendliest on-ramps and can "
    "export without a watermark. If you want genuinely jaw-dropping clips generated from a "
    "text prompt, Google Veo — reachable through the free Gemini app with a small daily "
    "allowance — is the most realistic, and it even generates matching sound. Runway, Kling "
    "and Luma give you more creative and motion control. But please internalise the reality "
    "check on the amber bar: free video is short, rate-limited, frequently watermarked, and "
    "explicitly not licensed for commercial use. It is spectacular for learning and personal "
    "fun, and not yet dependable for client or commercial work. I'm not running this live "
    "because generation can be slow and unpredictable on stage, but the prompt is in your "
    "handout so you can try it tonight.")

# ---- Slide 19: 2.7 holiday ----
s = content_base("2.7 Holiday planning", "Your instant travel brainstorming partner", "8 Everyday Jobs", 21)
tool_card(s, Inches(0.75), Inches(2.05), Inches(5.8), Inches(2.3), TEAL,
          "ChatGPT / Gemini", "Best all-round planner",
          "Turns a vague idea into a day-by-day itinerary in seconds",
          "Prices & 'this place exists' claims can be wrong")
tool_card(s, Inches(6.78), Inches(2.05), Inches(5.8), Inches(2.3), BLUE,
          "Wonderplan · Google Travel", "Free dedicated tools",
          "Maps, budgets, and real listings alongside the plan",
          "Less flexible than an open chat")
prompt_box(s, Inches(0.75), Inches(4.5), Inches(7.6), Inches(1.7), "GIVE IT THE DETAILS:",
           ["'10 relaxed days in Japan, food-focused, mid-budget,",
            "2 adults, first visit, hate early starts — build a",
            "day-by-day plan with 2–3 options each day.'"])
callout(s, Inches(8.5), Inches(4.5), Inches(4.08), Inches(1.7), "⚠️",
        "Always verify prices, opening hours & bookings. Use AI to plan — not to pay.",
        accent=AMBER, fill=AMBER_BG)
notes(s,
    "Seventh — the fun one — planning a trip. A general assistant like ChatGPT or Gemini is "
    "genuinely brilliant at this: give it a vague idea — say, ten relaxed days in Japan, "
    "food-focused, mid-budget, two adults, first visit, and we hate early starts — and it "
    "turns that into a coherent day-by-day plan in seconds, which normally takes hours of "
    "stitching together blogs and forums. Dedicated free tools like Wonderplan and Google "
    "Travel add maps, budgets and real listings on top. The secret to a good result is "
    "detail in your prompt, as shown in the box — the more constraints you give, the better "
    "the plan. But here's the catch that really matters for travel: AI's prices, opening "
    "hours, and even 'this restaurant exists' claims can be out of date or completely "
    "invented. So use it to plan and to spark ideas, and always verify before you book "
    "anything. Plan with AI; pay only after you've checked.")

# ---- Slide 20: 2.8 daily life ----
s = content_base("2.8 AI in daily life", "The small wins that add up", "8 Everyday Jobs", 22)
uses = [("🍳","Fridge → dinner","3 meal ideas from a photo of what you have"),
        ("📑","Explain the jargon","Decode a contract, letter, or insurance form"),
        ("✂️","Summarise anything","5 key points from a 40-page PDF or article"),
        ("💬","Soften a message","Draft the awkward email you're avoiding"),
        ("🌐","Translate live","Point your camera at a menu or sign"),
        ("🎁","Write the tricky bit","The birthday poem, the toast, the caption")]
x0=Inches(0.75); y0=Inches(2.1); w=Inches(3.83); h=Inches(1.5)
for i,(g,head,body) in enumerate(uses):
    col=i%3; rowi=i//3
    x=x0+col*(w+Inches(0.17)); y=y0+rowi*(h+Inches(0.16))
    rect(s,x,y,w,h,CARD_BG,line=CARD_BRD,rounded=True)
    icon_badge(s,x+Inches(0.2),y+Inches(0.28),Inches(0.6),[TEAL,BLUE,NAVY2][i%3],g,17)
    tf=tbox(s,x+Inches(0.95),y+Inches(0.16),w-Inches(1.1),h-Inches(0.3),anchor=MSO_ANCHOR.MIDDLE)
    p=para(tf,True,space_after=2); run(p,head,12.5,NAVY,bold=True)
    p2=para(tf,False); run(p2,body,10,MUTED)
callout(s, Inches(0.75), Inches(5.55), Inches(11.83), Inches(0.8), "🔒",
        "Never paste passwords, ID numbers, or medical/financial details into a free consumer AI.",
        accent=AMBER, fill=AMBER_BG)
notes(s,
    "Eighth: the small daily wins that, added together, hand you back real time every week. "
    "Snap a photo of your fridge and ask for three dinner ideas from what's actually in "
    "there. Paste in a baffling insurance letter or contract and ask, 'explain this like "
    "I'm busy — what do I actually need to do?' Drop in a forty-page PDF and get the five "
    "key points before a meeting. Ask it to soften the slightly awkward message to your "
    "landlord, point your phone camera at a foreign menu for a live translation, or write "
    "the birthday poem or wedding toast you've been dreading. None of these is dramatic on "
    "its own, but the cumulative time saving is significant. The one firm rule, on the "
    "amber bar: never paste truly sensitive information — passwords, ID numbers, medical or "
    "financial details — into a free consumer AI, because on free tiers your inputs may be "
    "used to improve the model.")

# ---- Section 3 ----
s_section("Section 3", "Doing It Responsibly",
          ["The four honest limitations to watch",
           "Five habits of people who get great results",
           "Staying the editor, not the passenger"])

# ---- Slide 21: limitations ----
s = content_base("Doing it responsibly", "The four honest limitations", "Responsibly", 24)
lims = [(AMBER,"🎭","Hallucinations","Invents facts, quotes & citations with total confidence"),
        (BLUE,"🕰","Stale info","Prices, hours & current events can be out of date"),
        (NAVY2,"⚖️","Bias","Mirrors patterns — and stereotypes — in its training data"),
        (GREEN,"🔒","Privacy","On free tiers your inputs may train the model")]
x0=Inches(0.75); y0=Inches(2.1); w=Inches(5.8); h=Inches(1.9)
for i,(accent,g,head,body) in enumerate(lims):
    col=i%2; rowi=i//2
    x=x0+col*(w+Inches(0.23)); y=y0+rowi*(h+Inches(0.2))
    rect(s,x,y,w,h,CARD_BG,line=CARD_BRD,rounded=True)
    icon_badge(s,x+Inches(0.26),y+Inches(0.3),Inches(0.7),accent,g,20)
    tf=tbox(s,x+Inches(1.15),y+Inches(0.28),w-Inches(1.35),h-Inches(0.5),anchor=MSO_ANCHOR.MIDDLE)
    p=para(tf,True,space_after=3); run(p,head,15,NAVY,bold=True)
    p2=para(tf,False); run(p2,body,11.5,MUTED)
notes(s,
    "Because this session is meant to be balanced, not a sales pitch, here are the four "
    "things to genuinely watch. First, hallucinations: AI will invent facts, quotes, and "
    "even fake citations with complete confidence — so verify anything that matters, "
    "especially names, numbers and references. Second, stale information: it may not know "
    "recent events, and prices and opening hours in particular go out of date. Third, bias: "
    "the model mirrors the patterns in its training data, which includes society's "
    "stereotypes, so be thoughtful when it's making judgements about people. Fourth, "
    "privacy: on free tiers your inputs may be used to train future models, so treat "
    "anything you type as potentially non-private. None of these are reasons to avoid AI — "
    "they're the reasons the 'stay the editor' mental model matters. Know the failure modes "
    "and you can use these tools confidently rather than naively.")

# ---- Slide 22: habits ----
s = content_base("Doing it responsibly", "Five habits of great AI users", "Responsibly", 25)
habits = [("Give context & an example","Vague prompts get vague answers — show it what 'good' looks like"),
          ("Ask for its reasoning","Have it show sources or explain how it got there"),
          ("Verify what matters","Cross-check any fact against a second source"),
          ("Iterate — don't accept draft 1","Push back: 'shorter', 'more formal', 'you missed X'"),
          ("Keep the decision human","You own the final call, every time")]
y=Inches(2.1)
for i,(head,body) in enumerate(habits,1):
    rect(s, Inches(0.75), y, Inches(11.83), Inches(0.82), CARD_BG, line=CARD_BRD, rounded=True)
    icon_badge(s, Inches(1.0), y+Inches(0.16), Inches(0.5), [TEAL,BLUE,NAVY2,TEAL,BLUE][i-1], str(i), 15)
    tf=tbox(s, Inches(1.75), y, Inches(10.6), Inches(0.82), anchor=MSO_ANCHOR.MIDDLE)
    p=para(tf,True,space_after=1); run(p,head,14,NAVY,bold=True); run(p,f"   — {body}",11,MUTED)
    y += Inches(0.92)
notes(s,
    "So how do the people who consistently get great results actually work? Five habits. "
    "One: give context and an example of what good looks like — the single biggest lever; "
    "vague prompts get vague answers. Two: ask it to show its reasoning or its sources, "
    "which both improves quality and lets you spot nonsense. Three: verify anything factual "
    "against a second source before you rely on it. Four: treat the first answer as a rough "
    "draft and push back — 'make it shorter', 'more formal', 'you missed this' — the second "
    "and third attempts are usually far better. Five: keep the final judgement human; the "
    "tool advises, you decide. Do these five things and you're already using AI more "
    "skilfully than the vast majority of people, and you'll sidestep almost every horror "
    "story you've heard.")

# ---- Section 4 ----
s_section("Section 4", "Your Starter Kit & Close",
          ["The four free tools to install tonight",
           "One challenge before you leave",
           "Questions & discussion"])

# ---- Slide 23: starter kit ----
s = content_base("Your starter kit", "Four free tools, and you're covered", "Close", 27)
kit = [(TEAL,"🤖","ChatGPT / Gemini","Everyday questions, drafting, brainstorming, travel"),
       (BLUE,"📚","NotebookLM","Studying and making sense of your own documents"),
       (NAVY2,"🎨","Canva","Posters, EDMs, and simple video — anything visual"),
       (GREEN,"📊","Gamma","Fast, good-looking presentation decks")]
x0=Inches(0.75); y0=Inches(2.15); w=Inches(2.87); h=Inches(3.1)
for i,(accent,g,head,body) in enumerate(kit):
    x=x0+i*(w+Inches(0.16))
    rect(s,x,y0,w,h,CARD_BG,line=CARD_BRD,rounded=True)
    rect(s,x,y0,w,Inches(0.16),accent,rounded=True)
    icon_badge(s,x+Inches(0.9),y0+Inches(0.45),Inches(1.05),accent,g,28)
    tf=tbox(s,x+Inches(0.2),y0+Inches(1.75),w-Inches(0.4),Inches(1.25))
    p=para(tf,True,space_after=5,align=PP_ALIGN.CENTER); run(p,head,15,NAVY,bold=True)
    p2=para(tf,False,align=PP_ALIGN.CENTER); run(p2,body,11,MUTED)
    x += w
callout(s, Inches(0.75), Inches(5.5), Inches(11.83), Inches(0.85), "✅",
        "All free. Pick ONE job from today and try it this week — that's how it sticks.",
        accent=GREEN, fill=RGBColor(0xE4,0xF3,0xEA))
notes(s,
    "If you do nothing else after today, install these four and you're covered for almost "
    "everything we've discussed. A general assistant — ChatGPT or Google Gemini — for "
    "everyday questions, drafting, brainstorming and travel. NotebookLM for studying and "
    "making sense of your own documents. Canva for anything visual — posters, EDMs, simple "
    "video. And Gamma for presentations. All free. But here's the thing about tools: "
    "knowing about them changes nothing. So my ask is on the green bar — pick just one job "
    "from today, the one most relevant to your week, and actually try it in the next few "
    "days. One real attempt will teach you more than this whole talk.")

# ---- Slide 24: close ----
s = add_slide(); bg(s, NAVY)
rect(s, 0, 0, SW, Inches(0.28), TEAL)
rect(s, 0, SH - Inches(0.28), SW, Inches(0.28), BLUE)
tf = tbox(s, Inches(0.9), Inches(1.5), Inches(11.5), Inches(1.4))
p=para(tf,True,space_after=6); run(p,"One challenge before you go", 40, WHITE, bold=True)
challenge = [("🎯","Tonight","Hand one 15-minute task to a free AI"),
             ("🔍","Notice","What it nailed — and what you had to fix"),
             ("💡","That gap","is exactly the skill worth building")]
y=Inches(3.05)
for g,head,body in challenge:
    icon_badge(s, Inches(1.4), y, Inches(0.6), TEAL, g, 18)
    t=tbox(s, Inches(2.25), y-Inches(0.05), Inches(9.5), Inches(0.7), anchor=MSO_ANCHOR.MIDDLE)
    pp=para(t,True); run(pp,head+"  ",16,TEAL,bold=True); run(pp,body,15,WHITE)
    y += Inches(0.85)
big = rect(s, Inches(4.35), Inches(6.0), Inches(4.6), Inches(0.85), TEAL, rounded=True)
center_text(big, [("Thank you — questions?", 20, NAVY, True)])
notes(s,
    "Let me leave you with a challenge rather than a summary. Tonight, pick one task that "
    "normally eats about fifteen minutes — a reply you're avoiding, a document to summarise, "
    "a plan to draft — and hand it to a free AI. Then pay attention to two things: what it "
    "nailed, and what you had to fix. That gap between the draft and what you'd actually "
    "send is precisely the skill worth building — knowing how to brief it and how to edit "
    "it. Do that once and these tools stop being abstract. Thank you all for your time and "
    "attention — I've really enjoyed this, and I'd love to take your questions, especially "
    "on any of the four demos or on anything you're now itching to try.")

prs.save("Using-AI-in-Our-Lives.pptx")
print(f"Saved Using-AI-in-Our-Lives.pptx with {len(prs.slides._sldIdLst)} slides.")
