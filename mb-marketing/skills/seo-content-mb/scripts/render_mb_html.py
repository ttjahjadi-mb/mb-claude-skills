#!/usr/bin/env python3
"""
Wrap a drafted page's body HTML in MB's real brand styling: colours,
Poppins (Google Font), Reader Pro headings (self-hosted, base64-embedded,
only if the licensed font file is present, e.g. internal workspace; falls
back to a serif stack otherwise, e.g. the public plugin, which never
bundles Reader Pro), and the real MB logo (inline SVG). Produces one
self-contained, portable HTML file, no external file dependencies except
the Poppins Google Fonts request (a public font, safe to load externally).

Usage: python3 render_mb_html.py <input.json> <output.html>

Input JSON shape:
{
  "meta_title": "TPD Claim for Mental Illness | Maurice Blackburn",
  "meta_description": "...",
  "keywords": {"primary": ["..."], "secondary": ["...", "..."]},
  "people_also_asked": ["...", "..."],
  "internal_links": ["https://...", "https://..."],
  "body_html": "<nav>...</nav>\n<h1>...</h1>\n<p class=\"byline\">...</p>\n<h2>...</h2>..."
}

"body_html" is the drafted page markup: breadcrumb nav, the single H1,
byline, and every H2/H3 section already written as real semantic tags
(never styled <p>/<div>/<strong> standing in for a heading). This script
does not write copy, it only wraps and brands what was already drafted.
"""
import base64
import json
import sys
from pathlib import Path

BRAND_MB_DIR = Path(__file__).resolve().parents[2] / "brand-mb"
LOGO_SVG_PATH = BRAND_MB_DIR / "assets" / "mb-logo.svg"
READER_PRO_WOFF2_PATH = BRAND_MB_DIR / "assets" / "fonts" / "reader-medium-pro.woff2"

CSS_TEMPLATE = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
{font_face_block}

:root {{
  --mb-red: #DB333C;
  --mb-shade1: #CC2E57;
  --mb-shade4: #461C2F;
  --mb-warm-white: #F8F5F0;
  --mb-neutral03: #D8DAE0;
  --mb-dark-grey: #4E4E4E;
}}

* {{ box-sizing: border-box; }}

body {{
  font-family: 'Poppins', sans-serif;
  color: var(--mb-shade4);
  background: var(--mb-warm-white);
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 24px 80px;
  line-height: 1.65;
  font-size: 17px;
}}

h1, h2, h3, h4 {{
  font-family: {heading_font}, Georgia, serif;
  color: var(--mb-shade4);
  font-weight: 500;
  line-height: 1.15;
}}

h1 {{ font-size: 44px; margin-top: 0; }}
h2 {{ font-size: 30px; margin-top: 2em; border-bottom: 2px solid var(--mb-red); padding-bottom: 0.2em; }}
h3 {{ font-size: 22px; margin-top: 1.5em; }}

a {{ color: var(--mb-shade1); }}
a:hover {{ color: var(--mb-red); }}

table {{ border-collapse: collapse; width: 100%; margin: 1.5em 0; font-size: 15px; }}
th, td {{ border: 1px solid var(--mb-neutral03); padding: 10px 14px; text-align: left; }}
th {{ background: var(--mb-neutral03); }}

.byline {{ color: var(--mb-dark-grey); font-size: 14px; margin-top: -0.5em; }}

.site-header {{
  display: flex;
  align-items: center;
  gap: 12px;
  padding-bottom: 24px;
  margin-bottom: 32px;
  border-bottom: 1px solid var(--mb-neutral03);
}}
.site-header svg {{ height: 34px; width: auto; }}

nav[aria-label="Breadcrumb"] ol {{
  list-style: none;
  display: flex;
  gap: 6px;
  padding: 0;
  margin: 0 0 16px;
  font-size: 14px;
  color: var(--mb-dark-grey);
}}
nav[aria-label="Breadcrumb"] li:not(:last-child)::after {{ content: "/"; margin-left: 6px; }}
"""


def build_font_face_block():
    if READER_PRO_WOFF2_PATH.exists():
        b64 = base64.b64encode(READER_PRO_WOFF2_PATH.read_bytes()).decode("ascii")
        return (
            "@font-face {\n"
            "  font-family: 'Reader Pro';\n"
            f"  src: url(data:font/woff2;base64,{b64}) format('woff2');\n"
            "  font-weight: 500;\n"
            "  font-display: swap;\n"
            "}\n"
        )
    return ""


def build_logo_html():
    if LOGO_SVG_PATH.exists():
        return LOGO_SVG_PATH.read_text()
    return "<strong>Maurice Blackburn</strong>"


def render(data, out_path):
    heading_font = "'Reader Pro'" if READER_PRO_WOFF2_PATH.exists() else "Georgia"
    css = CSS_TEMPLATE.format(
        font_face_block=build_font_face_block(),
        heading_font=heading_font,
    )
    logo_html = build_logo_html()

    meta_title = data.get("meta_title", "")
    meta_description = data.get("meta_description", "")
    body_html = data["body_html"]

    html = f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{meta_title}</title>
<meta name="description" content="{meta_description}">
<style>{css}</style>
</head>
<body>
<header class="site-header">{logo_html}</header>
{body_html}
</body>
</html>
"""
    Path(out_path).write_text(html)


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 render_mb_html.py <input.json> <output.html>", file=sys.stderr)
        sys.exit(1)
    input_path, out_path = sys.argv[1], sys.argv[2]
    data = json.loads(Path(input_path).read_text())
    render(data, out_path)
    print(f"HTML -> {out_path}")


if __name__ == "__main__":
    main()
