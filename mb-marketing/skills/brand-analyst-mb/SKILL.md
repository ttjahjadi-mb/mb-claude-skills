---
name: brand-analyst-mb
description: Compare Maurice Blackburn's brand against a named competitor or the broader plaintiff-law-firm market during a conversation — positioning, tone, visual identity, digital presence, reputation signals. Use when the user asks "how does our brand compare to X", "what is [competitor] doing differently", "brand competitor analysis", or wants a quick brand-only read (not a full acquisition/digital audit — use acquisition-dashboard-mb for that). Pulls MB's own side from the brand-mb skill; researches the competitor live via web search.
allowed-tools: Read, WebSearch, WebFetch
---

# MB Brand Analyst

A conversational analysis skill: compare MB's brand against a competitor (or the market generally) and report findings directly in the conversation. This is lighter-weight than `acquisition-dashboard-mb` — no scored dashboard, no Excel workbook, no persistent project folder. If the user actually wants that level of rigour (acquisition due-diligence, a saved scorecard, a leadership deck), say so and point them at `acquisition-dashboard-mb` instead.

## When to use this vs. acquisition-dashboard-mb

- **This skill**: a quick, in-chat "how do we compare on brand/positioning/tone" read. Output is conversational analysis, not a saved artefact.
- **acquisition-dashboard-mb**: a full scored competitive teardown across nine weighted pillars (SEO, brand, CX, tech, risk, etc), producing a dashboard + Excel + report. Use that when the ask is bigger than a brand-only conversation, or when the output needs to be shareable/persistent.

## MB's side: read from brand-mb

Before analysing anything, read the `brand-mb` skill's reference files (`brand-guidelines.md`, `tone-of-voice.md`, `brand-history.md`) for MB's documented colours, typography, voice, and positioning. Treat gaps flagged in those files as genuine gaps — don't fill them in with invented MB positioning to make the comparison look more complete than it is.

## Competitor's side: research live, don't assume

Never rely on prior knowledge of a law firm's brand from training data alone — brand positioning, taglines, and visual identity change. For each comparison, actually look:

1. **Visual identity**: fetch the competitor's homepage. Note primary colours, typography feel (serif/sans, formal/casual), logo style, photography style (stock vs. real staff/clients, corporate vs. warm).
2. **Voice and tone**: read a sample of on-site copy (homepage, an practice-area page, an about-us page). Note formality, sentence length, use of jargon, how they address someone in distress (if it's a personal injury/compensation competitor) vs. a purely commercial firm voice.
3. **Positioning**: what's their stated differentiator (size, results, specialism, "no win no fee", local presence, etc)? How do they describe who they're for?
4. **Reputation signals**: Google reviews rating/volume if visible, any awards/rankings mentioned on-site, social proof style (client testimonials, case results, media mentions).

## Output format

Structure the comparison as:

1. **Snapshot table** — MB vs. competitor, one row per dimension (colour/visual, voice, positioning, reputation signals), one line each.
2. **Where MB is stronger** — specific, evidenced observations, not generic praise.
3. **Where the competitor is stronger, or doing something worth learning from** — be candid; the point of a competitor scan is to find real gaps, not confirm MB is already winning everywhere.
4. **Open questions / can't-confirm items** — anything that needed data MB doesn't have documented (see brand-mb's known gaps) or that wasn't visible from public research.

## Operating principles

- **Public sources only** — this is homepage/on-site research plus general web search, not access to internal competitor data.
- **Evidence over vibes** — every claim about the competitor should trace back to something actually observed on their site or in search results, not a general impression.
- **No invented MB positioning** — see brand-mb's known gaps. If MB's own tone-of-voice or history documentation is thin, say so in the "open questions" section rather than smoothing over it.
- **House style** — plain English, no em dashes, evidence-first (per MB's general content conventions).
