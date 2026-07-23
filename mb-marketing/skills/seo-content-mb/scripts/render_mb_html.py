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
  "canonical_url": "https://www.mauriceblackburn.com.au/...",
  "og_type": "article",
  "published_date": "2026-07-23",
  "modified_date": "2026-07-23",
  "author_url": "https://www.mauriceblackburn.com.au/our-lawyers/josh-mennen/",
  "body_html": "<div class=\"meta-block\">...</div>\n<nav>...</nav>\n<h1>...</h1>..."
}

Only "meta_title" and "body_html" are required. "canonical_url",
"og_type", "published_date", "modified_date", "author_url" are optional,
each is only emitted as a meta tag if provided, never fabricate one.

"body_html" is the drafted page markup, using these standard classes for
the CSS this script already provides (do not invent alternative class
names or inline styles):

- .meta-block   the internal Targeting-brief/metadata block, a clearly
                 visible dashed-border box labelled "internal, remove
                 before publish", never a hidden HTML comment, a reviewer
                 must not be able to miss it and accidentally ship it.
- .disclaimer   the compliance disclaimer + jurisdiction paragraph,
                 tinted background with a left accent border.
- .support-box  a soft, non-alarming box for crisis-line / support info
                 or a CTA lead-in, white card on the page background.
- .cta-btn      a filled MB-red button for the primary conversion link.
- .faq-item     one Q&A pair, bottom-bordered, used inside the FAQ section.
- .related-card a bordered card for a related-article link.
- .flag         a yellow warning callout for anything the reviewer must
                 action before publish (an unapproved quote, a claim to
                 verify, a consent status to confirm). This is the visible
                 equivalent of this skill's own "flag it" instructions,
                 make gaps impossible to miss in the file, not just
                 mentioned in the chat response.

Every heading in body_html must be a real <h1>/<h2>/<h3> tag, never a
styled <p>/<div>/<strong> standing in for one.
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
  --mb-pure-white: #FFFFFF;
  --mb-neutral03: #D8DAE0;
  --mb-dark-grey: #4E4E4E;
  --mb-tint20: #DED1DB;
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
  font-family: {heading_font};
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
th {{ background: var(--mb-tint20); color: var(--mb-shade4); }}

.byline {{
  color: var(--mb-dark-grey);
  font-size: 14px;
  border-bottom: 1px solid var(--mb-neutral03);
  padding-bottom: 16px;
  margin-bottom: 16px;
}}

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

.meta-block {{
  background: var(--mb-pure-white);
  border: 2px dashed var(--mb-red);
  padding: 20px;
  margin-bottom: 36px;
  font-size: 14px;
}}
.meta-block h2 {{ margin-top: 0; font-size: 20px; border-bottom: none; }}
.meta-block h3 {{ font-size: 15px; margin-bottom: 4px; margin-top: 1em; }}

.disclaimer {{
  background: var(--mb-tint20);
  border-left: 4px solid var(--mb-red);
  padding: 14px 18px;
  font-size: 14px;
  margin: 20px 0;
}}

.support-box {{
  background: var(--mb-pure-white);
  border: 1px solid var(--mb-neutral03);
  padding: 16px 18px;
  border-radius: 6px;
  font-size: 15px;
}}

.cta-btn {{
  display: inline-block;
  background: var(--mb-red);
  color: #fff;
  padding: 12px 24px;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 600;
  margin: 16px 0;
}}
.cta-btn:hover {{ background: var(--mb-shade1); color: #fff; }}

.faq-item {{ border-bottom: 1px solid var(--mb-neutral03); padding: 14px 0; }}

.related-card {{
  border: 1px solid var(--mb-neutral03);
  border-radius: 6px;
  padding: 14px;
  margin-bottom: 10px;
}}

.flag {{
  background: #FFF3CD;
  border-left: 4px solid #E0A800;
  padding: 10px 14px;
  font-size: 13px;
  margin: 10px 0;
}}
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


def build_head_meta(data):
    lines = []
    canonical = data.get("canonical_url")
    if canonical:
        lines.append(f'<link rel="canonical" href="{canonical}">')

    og_type = data.get("og_type")
    meta_title = data.get("meta_title", "")
    meta_description = data.get("meta_description", "")
    if og_type:
        lines.append(f'<meta property="og:type" content="{og_type}">')
    if meta_title:
        lines.append(f'<meta property="og:title" content="{meta_title}">')
    if meta_description:
        lines.append(f'<meta property="og:description" content="{meta_description}">')
    if canonical:
        lines.append(f'<meta property="og:url" content="{canonical}">')

    published = data.get("published_date")
    modified = data.get("modified_date")
    author_url = data.get("author_url")
    if published:
        lines.append(f'<meta property="article:published_time" content="{published}">')
    if modified:
        lines.append(f'<meta property="article:modified_time" content="{modified}">')
    if author_url:
        lines.append(f'<meta property="article:author" content="{author_url}">')

    return "\n".join(lines)


def render(data, out_path):
    heading_font = "'Reader Pro', Georgia, serif" if READER_PRO_WOFF2_PATH.exists() else "Georgia, serif"
    css = CSS_TEMPLATE.format(
        font_face_block=build_font_face_block(),
        heading_font=heading_font,
    )
    logo_html = build_logo_html()
    head_meta = build_head_meta(data)

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
{head_meta}
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
