---
name: repurpose-mb
description: Turns one long-form input (case update, media coverage, blog post, or investigation summary) into a batch of platform-native MB posts across LinkedIn, Instagram, TikTok, and Meta (Facebook). Extracts the core themes first, opens every output with a hook from viral-hooks-mb, sizes each to its platform, and runs post-grader-mb (compliance + quality) before returning. Triggers on "repurpose this," "turn this into posts," "break this into content for our channels."
argument-hint: "[paste long-form content] [optional: channels to prioritize]"
allowed-tools: Read, Write, Edit, Glob, AskUserQuestion
---

# Repurpose (MB)

You take one long piece of content — a case update, an investigation summary, media coverage, a blog post — and turn it into a batch of platform-native posts across MB's real channels: LinkedIn, Instagram, TikTok, Meta (Facebook).

If the input is short (a single idea, under a paragraph), this is the wrong skill — use `post-writer-mb` instead.

## Workflow

### Step 1: Load context

1. Invoke `brand-mb` for voice/tone, and read `brand-mb/reference/legal-marketing-guardrails.md` for the compliance checklist and channel list.
2. Confirm the source type (case update, investigation summary, media coverage, blog). Media/transcript sources may have quotes that need attribution care — check before lifting language directly.
3. Ask which of the 4 channels to prioritize (LinkedIn, Instagram, TikTok, Meta), or default to all 4 if the user doesn't specify.

### Step 2: Extract the core themes

Read the full input. Pull out:

- **The 1 central point** — what people need to know or do.
- **2-5 supporting points** — distinct angles, each strong enough to stand alone as a post (e.g. eligibility criteria, timeline, what to do next, background on the matter).
- **Every confirmed fact** — real numbers, names (consent-checked), dates, quotes. Never invent or round up a fact to make a post land.

List the themes back to the user in 2-3 lines before writing, so they can redirect. Don't make them approve a long outline.

### Step 3: Map themes to channels

Default output (adjust to what the source actually supports — don't pad with weak angles just to hit a count):

- **2 LinkedIn posts** — the most substantive/professional angles (legal context, what changed, what it means).
- **2 Instagram posts** — the most visual or human angle (client impact where consent allows, a clear callout).
- **1 TikTok script** — the most direct, spoken-explainer angle (HOOK / BODY / CTA format).
- **2 Meta (Facebook) posts** — the broadest-reach, plainest-language angle.

### Step 4: Open every output with a hook

Invoke `viral-hooks-mb` for each output, passing the theme and channel. Vary the category across the batch so it doesn't read as formulaic — but every hook still passes the compliance guardrails, no exceptions for "it's just a hook."

### Step 5: Write each output to its channel

Format limits + MB's own observed conventions (from 109 of MB's real posts; see `tone-of-voice.md`, "How MB writes on social"). The channel split follows `tone-of-voice.md`'s audiences: **LinkedIn ≈ Audience 01** (professionals/referrers/media), **Instagram ≈ Audience 02** (claimants/public).

**LinkedIn** (Aud 01): hook in first ~140 characters. 1,200-1,500 characters sweet spot. 3-5 firm/topic hashtags optional at the end. **MB convention: name the spokesperson lawyer** and **put the (trackable) link inline**, often citing the source outlet. Tag partner orgs/people where relevant.

**Instagram** (Aud 02): hook in first 125 characters. Requires media reference/placeholder. 3-5 niche/campaign hashtags. One CTA. **MB convention: "link in bio" (no inline links)**; use the carousel "Swipe through…" mechanic for educational angles; warmer register, more emoji; POV/trend hooks OK for lighter topics only.

**TikTok script**: HOOK (spoken line + on-screen text, first 1.7 seconds) / BODY (15-40 seconds, short spoken lines with [on-screen text] and [b-roll] cues) / CTA (final 3 seconds). Keep total spoken length under 45 seconds. Assume burned-in bold white captions.

**Meta (Facebook)**: 40-80 characters optimal for the hook. No hashtags. No engagement bait.

Structure every written output the way MB actually does: very short 1-2 sentence paragraphs with line breaks; for case content, setup → what went wrong → the legal point → an explicit takeaway; hedged conversion language ("you may be entitled," "you have options"), never a guarantee.

### Step 6: Apply MB voice + compliance

Every output:
- Follows `tone-of-voice.md` (contractions, active voice, real names only with consent, Australian English).
- **Em dash applied by default** — MB's house style permits it, no need to ask per output.
- One concrete idea per post. Specific, confirmed details only.
- Passes every item in `legal-marketing-guardrails.md` — no outcome guarantees, no misleading comparisons, trigger warning if the subject is distressing, hedge absolute legal claims.

### Step 7: Grade and improve

Run `post-grader-mb` on each output. Compliance must pass; quality should clear 8/10. Apply fixes and re-grade as needed.

### Step 8: CTA pass

For each output, pick from MB's real CTA set (Free claim check, Ask Morry AI, Chat with Morry AI, Request a callback, Get in touch) matched to the channel and angle. After the batch, ask which CTAs to keep or swap.

### Step 9: Return the batch

```
## LinkedIn (2 posts)
### Post 1 — [theme] — [hook category] — [score]/10 — Compliance: PASS
[full post]

## Instagram (2 posts)
### Post 1 — [theme] — [hook category] — [score]/10 — Compliance: PASS
[full post]

## TikTok Script (1)
### Script 1 — [theme] — [hook category]
HOOK: [spoken] / [on-screen text]
BODY: ...
CTA: ...

## Meta / Facebook (2 posts)
### Post 1 — [theme] — [hook category] — [score]/10 — Compliance: PASS
[full post]
```

After the batch: "Which CTAs do you want to keep or swap? Want a matching Canva creative for any of the Instagram/Facebook posts? And are you ready to copy these into your scheduler?"

### Step 10: Draft matching creatives in Canva (auto-filled, for review)

If the user wants creatives, draft them on real MB brand templates with the copy **already placed** — follow `post-writer-mb`'s Step 8 flow exactly (create a new design from the template → open an editing transaction → `replace_text` the copy fitted to the layout → attach a supplied image via `upload-asset-from-url` + `update_fill` where the template has an image element → render the thumbnail → `commit` → send the `edit_url` + thumbnail for review). **Never edit the brand template itself; always work on the new design created from it.**

Format → MB main-brand template: Quote - x 3 versions; Key Points List: White; Full Width Text Carousel; Image & Solid: 60/40; Layered Squares: Red; Latest News/Blogs: Shade 2; FF Awards; 5 star Google review. Avoid navy "CFA" templates unless it's Claims Funding Australia content.

Batch discipline: for a multi-post batch, first list which template each post maps to (so the user can redirect before you create several designs), and **fit each post's copy to its template — flag any that are too long to fit cleanly** and offer a shorter version or a roomier template rather than letting text overflow. Fallback if no template fits: `generate-design` → `create-design-from-candidate` (creative direction, not literal copy).

## What NOT to Do

- Don't pad with weak angles to hit a count — if the source only supports 3 strong posts, return 3.
- Don't copy the same text across channels. Each channel gets a native rewrite.
- Don't open any output with a generic AI intro — every hook comes from `viral-hooks-mb`.
- Don't return a post below 8/10 quality or any compliance failure — loop on the grader.
- Don't invent a fact, quote, or name to strengthen a post.
- Don't leave source filler ("um," "you know") in the output if repurposing a transcript.
