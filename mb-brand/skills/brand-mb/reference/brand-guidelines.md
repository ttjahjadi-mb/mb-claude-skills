# Maurice Blackburn Brand Guidelines

Source of truth: Figma file **"MB UI Guidelines - 2026"** (`fileKey: dTVH3EntgwPtA7Jrq4MSEo`), page "UI Styleguide". Pulled via the Figma MCP 2026-07-11.

Assets bundled with this skill:
- `assets/mb-logo.svg` — official logo (solid MB Shade 4 `#461C2F` on transparent; invert to white for dark backgrounds)
- `assets/fonts/reader-medium-pro.woff` / `.woff2` — the licensed display font, self-host only, never link externally

## Colours

The values below are Figma's **printed swatch labels**, confirmed correct against the actual mauriceblackburn.com.au logo SVG (its fills — `#DB333C`, `#A82660`, `#461C2F` — match these printed labels exactly). The Figma MCP's `get_design_context` tool renders swatch fills roughly 1 unit off from these on most swatches — treat any value pulled that way as needing a cross-check against a real production asset before trusting it.

| Token | Hex | Use |
|---|---|---|
| MB Red | `#DB333C` | Primary accent / CTA |
| MB Shade 1 | `#CC2E57` | Links, secondary accent |
| MB Shade 2 | `#A82660` | Tertiary accent |
| MB Shade 3 | `#75264F` | Tertiary accent (darker) |
| MB Shade 4 | `#461C2F` | Primary heading / dark UI colour (deep plum) |
| MB Warm White | `#F8F5F0` | Page background |
| Warmer White | `#F4F1EA` | Alternate background |
| Pure White | `#FFFFFF` | Surface / card background |
| Neutral 03 | `#D8DAE0` | Borders, dividers |
| Neutral 05/06 | `#181A20` | Near-black, dark surfaces (e.g. code blocks) |
| Dark Grey | `#4E4E4E` | Muted/secondary text |
| Tint — Shade 03 20% | `#DED1DB` | Light accent background (e.g. active nav state) |
| Tint — 50% | `#AE93A4` | Mid tint |
| Tint — 80% | `#7F5070` | Dark tint |

## Typography

- **Headings** — "Reader Pro" Medium (licensed display face; files in `assets/fonts/`). Scale: H1 80px/80px, H2 60px/60px, H3 40px/44px, H4 24px/32px, H5 20px/26px, H6 18px/24px. Heading colour is MB Shade 4 (`#461C2F`).
- **Subtitle** — Poppins Regular, 20px/28px.
- **Overline** — Poppins SemiBold, 10pt/12pt, uppercase, wide letter-spacing.
- **Body text** — Poppins Regular, 17px/25px, colour `#461C2F`.
- **Body text small / captions** — Poppins Regular, 12px/20px, colour Dark Grey `#4E4E4E`.
- **Link text** — Poppins Regular, underlined, 17px/25px, colour MB Shade 1 `#CC2E57`.
- **Blockquote** — Reader Pro Medium, 60px/60px.

Poppins is a public Google Font (safe to load via `@import`/`<link>`). Reader Pro is **not** publicly distributed — always self-host from `assets/fonts/` via `@font-face`, never link externally.

## Logo usage

- Solid single-colour mark, MB Shade 4 (`#461C2F`) on transparent background.
- On a light/white background, use as-is.
- On a dark background, invert to white (e.g. CSS `filter: brightness(0) invert(1)`) rather than sourcing a separate white variant file.
- Don't recolour it to any other brand colour (e.g. MB Red) — logo is always neutral dark or white.

## Other MB fonts you may encounter (legacy — not current brand)

MB's various microsites bundle a wider font stack (Roboto, Rubik, Source Sans Pro, Stag, Proxima Nova, Font Awesome icon fonts) left over from older site sections. These are **not** part of the current 2026 brand system — Poppins + Reader Pro are the only two confirmed-current faces. Don't default to the legacy fonts for new work; ask if a project genuinely needs to match an existing legacy page.
