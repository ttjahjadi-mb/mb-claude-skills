---
name: brand-mb
description: Maurice Blackburn brand reference — colours, typography, logo usage, tone of voice, and brand history. Use when building any MB-branded output (site component, dashboard, deck, EDM, document) that needs exact brand colours/fonts/logo, when writing content that needs to sound like MB rather than a generic assistant, or when asked about MB's brand story, positioning, or design system. Distinct from a personal voice-principles.md (an individual's writing style) — this is the company-level brand.
allowed-tools: Read
---

# Maurice Blackburn Brand Reference

A lookup skill, not a task skill. When triggered, read the relevant reference file(s) below and apply them directly — don't ask the user to repeat brand facts that are already documented here.

## What's in this skill

| File | Use when... |
|---|---|
| `reference/brand-guidelines.md` | Building anything visual — need exact hex colours, type scale, logo usage rules |
| `reference/tone-of-voice.md` | Writing MB-facing content (site copy, EDMs, docs) that needs to sound like the firm, not a generic assistant |
| `reference/brand-history.md` | Answering "who is MB", brand story, positioning questions |
| `assets/mb-logo.svg` | Need the actual logo file to embed |

**Not bundled in this public copy**: the Reader Pro webfont files and the internal writing-guide PDF are excluded here — Reader Pro is a licensed font (not MB's to redistribute publicly) and the PDF is MB's internal brand document. Both exist in the internal workspace copy of this skill (`Tony 2.0/.claude/skills/brand-mb/assets/`) for anyone working from inside MB's own environment. This public copy relies on the serif CSS fallback for headings instead of the real Reader Pro file.

## How to apply

- **Building UI/output**: read `brand-guidelines.md` first, use its CSS-custom-property-style token table directly rather than inventing colours. Poppins is a public Google Font (safe to `@import`). Reader Pro isn't bundled here (see note above) — use the serif fallback, or pull the real font files from the internal workspace copy if you have access to it.
- **Writing content**: read `tone-of-voice.md`. If the task is drafting for a specific named person (not MB as a company), check for that person's own `voice-principles.md` first — the two are not interchangeable. Company brand voice governs site/EDM/official copy; personal voice governs an individual's emails and drafts.
- **Brand/positioning questions**: read `brand-history.md`. If a question falls outside what's documented there, say so rather than guessing — flag it as a gap for the marketing team to fill in, don't invent MB history or messaging.

## Sources

- `brand-guidelines.md` — Figma file "MB UI Guidelines - 2026" (`fileKey: dTVH3EntgwPtA7Jrq4MSEo`).
- `tone-of-voice.md` — MB's own internal "Brand guidelines Version 1.1" writing guide PDF, read in full. This is the real, finalised company voice, not a draft.
- `brand-history.md` — MB's own "About us" page, cross-checked against Wikipedia (both the firm's page and the founder's biography) and general web search, with no contradictions found across all four sources.

All three are real, sourced documents now — not placeholders. Still flag anything a task needs that genuinely isn't covered (e.g. specific internal timelines, board changes since research date) rather than extrapolating past what's documented.

## Keeping this current

- **Colours/typography**: source is the Figma file above. If it changes, re-pull via the Figma MCP (`get_design_context` on the colour/typography frames) and update `reference/brand-guidelines.md` — the tool's rendered fill extraction runs ~1 unit off from Figma's printed swatch labels on most swatches; trust the printed label (confirmed correct against the real mauriceblackburn.com.au logo SVG), not the tool's rendered fill.
- **Tone of voice**: source is the internal writing-guide PDF. If MB issues a newer version, re-read it and update `reference/tone-of-voice.md`.
- **Brand history**: leadership/scale figures (chairman, CEO, revenue, office count) date-stamp quickly — reconfirm via a fresh web check before quoting them in anything long-lived.
