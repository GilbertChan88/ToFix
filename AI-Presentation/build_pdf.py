#!/usr/bin/env python3
"""
Convert the demo runbook markdown files into themed, print-ready PDFs.
Matches the deck's blue/teal theme. Adds a cover banner, styled tables,
code blocks, and a footer with page numbers.

Usage:  python3 build_pdf.py
Output: 04-demo-runbook-AUDIENCE.pdf, 05-demo-runbook-PRESENTER.pdf
"""

import re
import markdown
from weasyprint import HTML

# ---- files to convert: (source_md, output_pdf, doc_title, banner_subtitle, accent) ----
JOBS = [
    (
        "04-demo-runbook-AUDIENCE.md",
        "04-demo-runbook-AUDIENCE.pdf",
        "Live Demo Runbook",
        "Audience Handout  ·  Using AI in Our Lives",
        "#18B6B0",  # teal accent for audience
    ),
    (
        "05-demo-runbook-PRESENTER.md",
        "05-demo-runbook-PRESENTER.pdf",
        "Live Demo Runbook",
        "PRESENTER Cockpit (Confidential)  ·  Using AI in Our Lives",
        "#1E6FB8",  # blue accent for presenter
    ),
]

CSS_TEMPLATE = """
@page {{
    size: A4;
    margin: 20mm 16mm 18mm 16mm;
    @bottom-center {{
        content: "{footer}  —  page " counter(page) " of " counter(pages);
        font-family: 'Helvetica', 'Arial', sans-serif;
        font-size: 8pt;
        color: #8090a0;
    }}
}}
* {{ box-sizing: border-box; }}
body {{
    font-family: 'Helvetica', 'Arial', sans-serif;
    font-size: 10.5pt;
    line-height: 1.5;
    color: #222b33;
}}
/* Cover banner */
.cover {{
    background: linear-gradient(120deg, #0F2A43 0%, #1E6FB8 100%);
    color: #ffffff;
    padding: 26px 28px;
    border-radius: 10px;
    margin-bottom: 22px;
    border-left: 10px solid {accent};
}}
.cover h1 {{
    margin: 0 0 6px 0;
    font-size: 26pt;
    color: #ffffff;
    border: none;
    padding: 0;
}}
.cover .sub {{
    font-size: 12pt;
    color: {accent};
    font-weight: bold;
    letter-spacing: .3px;
}}
h1 {{
    font-size: 17pt;
    color: #0F2A43;
    border-bottom: 3px solid {accent};
    padding-bottom: 4px;
    margin-top: 22px;
    page-break-after: avoid;
}}
h2 {{
    font-size: 13.5pt;
    color: #1E6FB8;
    margin-top: 18px;
    page-break-after: avoid;
}}
h3 {{
    font-size: 11.5pt;
    color: #0F2A43;
    margin-top: 14px;
    page-break-after: avoid;
}}
p {{ margin: 6px 0; }}
a {{ color: #1E6FB8; text-decoration: none; }}
strong {{ color: #0F2A43; }}
ul, ol {{ margin: 6px 0 6px 0; padding-left: 22px; }}
li {{ margin: 3px 0; }}
/* Blockquotes = callouts */
blockquote {{
    background: #F4F8FB;
    border-left: 5px solid {accent};
    margin: 12px 0;
    padding: 8px 14px;
    color: #3a4650;
    border-radius: 4px;
    page-break-inside: avoid;
}}
blockquote p {{ margin: 4px 0; }}
/* Code */
code {{
    font-family: 'DejaVu Sans Mono', 'Courier New', monospace;
    background: #eef3f7;
    padding: 1px 5px;
    border-radius: 3px;
    font-size: 9pt;
    color: #0F2A43;
}}
pre {{
    background: #0F2A43;
    color: #eaf2f8;
    padding: 12px 14px;
    border-radius: 6px;
    font-size: 8.6pt;
    line-height: 1.45;
    overflow-wrap: break-word;
    white-space: pre-wrap;
    page-break-inside: avoid;
    border-left: 4px solid {accent};
}}
pre code {{ background: none; color: #eaf2f8; padding: 0; }}
/* Tables */
table {{
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
    font-size: 9.3pt;
    page-break-inside: avoid;
}}
th {{
    background: #0F2A43;
    color: #ffffff;
    text-align: left;
    padding: 7px 9px;
    font-size: 9pt;
}}
td {{
    padding: 6px 9px;
    border-bottom: 1px solid #d7e2ea;
    vertical-align: top;
}}
tr:nth-child(even) td {{ background: #F1F6FA; }}
hr {{
    border: none;
    border-top: 1px solid #cdd9e2;
    margin: 18px 0;
}}
/* Keep a demo section header with its content where possible */
h1 + p, h2 + p {{ page-break-before: avoid; }}
"""


def md_to_html_body(md_text):
    return markdown.markdown(
        md_text,
        extensions=["extra", "sane_lists", "nl2br"],
    )


def build(src, out, title, subtitle, accent):
    with open(src, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Strip the first H1 (we render it in the cover banner instead)
    md_text = re.sub(r"^#\s+.*\n", "", md_text, count=1)

    body_html = md_to_html_body(md_text)
    footer = subtitle.split("·")[0].strip()

    css = CSS_TEMPLATE.format(accent=accent, footer=footer)
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><style>{css}</style></head>
<body>
  <div class="cover">
    <h1>{title}</h1>
    <div class="sub">{subtitle}</div>
  </div>
  {body_html}
</body></html>"""

    HTML(string=html).write_pdf(out)
    print(f"  ✔ {out}")


if __name__ == "__main__":
    print("Building runbook PDFs...")
    for job in JOBS:
        build(*job)
    print("Done.")
