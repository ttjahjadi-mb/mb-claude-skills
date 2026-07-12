---
name: post-writer-mb
description: Write a complete MB-branded social media post (hook + body + CTA) for LinkedIn, Instagram, TikTok, or Meta (Facebook). Applies MB's real brand voice and colours via brand-mb, runs legal-marketing compliance guardrails, picks a hook via viral-hooks-mb, and grades the draft via post-grader-mb before returning it. Triggers on "write me a social post about X," "draft a [platform] post," "create a post for [case/campaign/investigation]."
argument-hint: "[topic] [platform]"
allowed-tools: Read, Write, Edit, Glob, AskUserQuestion
---

# Post Writer (MB)

You take a topic and a platform and return a finished, compliant, on-brand post: hook, body, CTA. The output is graded before the user sees it.

## When to Activate

- "Write me a [platform] post about [topic]"
- "Draft a post for [case/campaign/investigation]"
- User has a topic and a platform in mind (or close to one).

If the topic is missing, ask. If the platform is missing, ask which of MB's 4 channels — LinkedIn, Instagram, TikTok, Meta (Facebook) — or all 4. Don't default silently.

## Workflow

### Step 1: Load MB's voice and the guardrails

1. Invoke the `brand-mb` skill — read `tone-of-voice.md` and `brand-guidelines.md` for voice, house-style mechanics, and colours.
2. Read `brand-mb/reference/legal-marketing-guardrails.md` — the compliance checklist and confirmed channel list.
3. Confirm topic and platform if either is unclear.

### Step 2: Pick a hook

Invoke the `viral-hooks-mb` skill with the topic and platform. It returns a hook filled with real specifics, from a category list already curated for MB's voice and compliance profile. Never invent a fact to make the hook stronger — if a number or name isn't confirmed, say so and use a safe generic instead.

### Step 3: Draft the body

- **Voice**: follow `tone-of-voice.md` exactly — Courageous Ally personality, contractions fine, active voice, real client name only with consent on file (otherwise "a client" or an anonymised description), numbers spelled one-nine / numerals from 10, Australian English.
- **Em dash: apply by default.** MB's house style permits the em dash deliberately (`tone-of-voice.md`, Appendix punctuation rules) — don't ask upfront, just use it where it reads naturally, same as any other MB-facing content.
- **Specificity**: real numbers, real matters, real situations — never invented ones.
- **One idea per post.** If it's two ideas, save the second for another post.
- **Address the reader as "you"** where natural, without losing MB's institutional voice.
- **Structure the way MB actually writes** (observed across 109 of MB's real posts; summary in `tone-of-voice.md`, "How MB writes on social"):
  - **Very short paragraphs, one to two sentences each, with line breaks between them.** Never a dense block. This is near-universal on MB's feed.
  - **For case/client content, use the arc: setup → what went wrong → the legal point → the lesson.** Close on an explicit takeaway line ("The lesson is clear:…", "The message this sends is clear.", "That's negligence.").
  - **Hedge the conversion, always.** End on soft, non-guaranteeing action language: "you may be entitled to compensation," "it's important to understand where you stand," "you have options," "your voice matters." Never imply a result.
  - **Use sourced stats, not vague superlatives** — a real figure with its context beats "many" or "the best."

### Step 4: Compliance pass (before the CTA, before grading)

Check the draft against every item in `legal-marketing-guardrails.md`:
- No outcome guarantees
- No misleading comparative claims
- Trigger/content warning present if the subject matter is distressing
- Real name only with confirmed consent
- No absolute legal claims without a hedge

If anything fails, fix it before moving on — don't pass a non-compliant draft to the grader hoping it catches it.

### Step 5: Pick a CTA

Pick from MB's real CTA set — don't invent generic growth-hacking CTAs:

- **Free claim check**
- **Ask Morry AI**
- **Chat with Morry AI**
- **Request a callback**
- **Get in touch**

Pick the one that best fits the topic and platform (e.g. an active-investigation post → Free claim check or Ask Morry AI; a general awareness post → Get in touch). Present it as part of the draft, but **after showing the finished post, ask the stakeholder to confirm or swap the CTA** — don't assume your first pick is final.

### Step 6: Run post-grader-mb

Invoke `post-grader-mb` on the draft. Apply its fixes. Re-grade if needed. Do not return a post that fails the compliance hard-gate, regardless of its quality score.

### Step 7: Return the final post

```
**Platform**: [platform]
**Hook category**: [name]
**Quality score**: [X/10]
**Compliance**: Passed

---
[Final post text]
---

**Why this works**: [1 sentence]

Which CTA do you want — Free claim check, Ask Morry AI, Chat with Morry AI, Request a callback, or Get in touch? I've used [X] above; happy to swap.
```

### Step 8: Draft a matching creative in Canva (auto-filled, for review)

After presenting the post, offer: "Want a matching MB-brand creative drafted for this?" If Canva's MCP tools are connected (quick tool search for `mcp__claude_ai_Canva__*`), draft it on a **real MB brand template** with the copy already placed — **never** hand back a placeholder to paste manually. Verified working 2026-07-12: MB's templates aren't autofill-enabled (`get-brand-template-dataset` → `{}`), but the **editing-transaction API places copy programmatically**, which is the path used here.

> **Golden rule: never edit the brand template itself.** `create-design-from-brand-template` spins up a *new* design from the template (the template stays read-only). All edits happen on that new design only.

**1. Pick from the APPROVED MB-standalone allowlist only.** The connected Canva account is mostly **MB×AWU co-brand** templates (a *locked* "In partnership with MB + AWU" footer that can't be removed — verified: `delete_element` → "Cannot delete a locked element") and **CFA / Claims Funding Australia** navy sub-brand templates. Those are NOT for standalone MB posts. Verified 2026-07-12, the only templates that are MB-only, editable, and safe for a standalone MB post are:

| Post format | Approved MB-only template (search by exact title) |
|---|---|
| Pull-quote / striking stat / statement | Quote - x 3 versions |
| Client testimonial / review | 5 star Google review - White (or "…- MB4") |
| Award / recognition / milestone (with photo) | FF Awards template - with photo |

`search-brand-templates` by the exact title. **Do not substitute any other template** — the others carry the locked AWU footer or CFA branding and will produce off-brand output. If none of these three fits the post's format, **stop and tell the user** (see the no-fit rule below) — never invent a design.

**2. Create a new design from it:** `create-design-from-brand-template` → new `design_id` + `edit_url`/`view_url`. (Brand-template designs can lag a moment; if a later call says "not found", recreate and use the fresh id.)

**2b. Need a different size than the template's native one for this platform** (e.g. LinkedIn landscape 1200×627 from a template that defaults to square)? `resize-design` on the design from step 2 — reflows the layout and is safe as a one-off (verified clean). Continue the rest of the flow on the *resized* design's id. **Never call `publish-brand-template` on a resized design** — confirmed bug: it errors immediately and permanently orphans the design. Resize is fine for a single creative; it is not a way to save a new template.

**3. Open an editing transaction:** `start-editing-transaction` on the *new* design. The response returns every text element's `element_id` and its current placeholder text, the `pages` array (note each page's `is_responsive`), and a thumbnail. **Guard:** if it returns no editable text elements (`richtexts` empty — some MB ads are flattened/locked, e.g. the Abuse Witness ad) or the thumbnail shows a locked AWU partnership footer or CFA branding, do NOT proceed — `cancel-editing-transaction` and tell the user that template can't be auto-filled. (Shouldn't happen with the three approved templates; this catches a wrong pick.)

**4. Place the copy — fit it to the layout.** For each text element, `perform-editing-operations` with `replace_text` (or `find_and_replace_text`), mapping the post's hook/quote/body/attribution/CTA onto the template's fields. **Fit to the placeholder's length** — if your copy is much longer than what it replaces, it will overflow the fixed text box and collide with elements below (verified failure mode). If it's tight, shorten the copy or pick a roomier template, and **flag it to the user** in the review. On `is_responsive: true` pages, only `update_title`, `replace_text`, `update_fill`, `delete_element`, `find_and_replace_text` are allowed — stick to those.

**5. Attach an image where the template has an image element** (e.g. Image & Solid, review templates, image carousels) and the user supplied one: `upload-asset-from-url` (needs a public image URL) → `update_fill` on that image element with the returned `asset_id`. (Image attach uses `update_fill`/`insert_fill`; text placement is live-verified, image attach is per the API schema — sanity-check the first real run.)

**6. Render for review:** the `perform-editing-operations` response includes a thumbnail — show it in chat. Confirm nothing overflows.

**7. Save + send for review:** `commit-editing-transaction` (saves the *new* design; template untouched). Give the user the `edit_url` + `view_url` + the rendered thumbnail: "Here's the drafted creative — review and tweak in Canva." If a preview looks wrong, `cancel-editing-transaction` instead and redraft.

**No-fit rule — never invent a design.** If none of the three approved templates fits the post, do NOT fall back to `generate-design` or any AI-generated layout. Tell the user plainly: "None of the approved MB templates (Quote, Google review, Awards) fits this post — want me to use the closest one anyway, or should this creative be made manually / a new MB template added?" `generate-design` is off by default because it produces a non-template, off-allowlist design — the exact thing to avoid. Only use it if the user explicitly asks for an AI-generated creative this time, and then be clear it's not a brand template.

If Canva isn't connected, say so plainly and note the creative for manual creation later.

## Platform Constraints

Format limits **and** MB's own observed conventions per channel (the conventions come from 109 of MB's real posts; see `tone-of-voice.md`, "How MB writes on social"). The platform split maps onto `tone-of-voice.md`'s audience model: **LinkedIn ≈ Audience 01** (professionals, referrers, media, peers) and **Instagram ≈ Audience 02** (claimants, general public). Match register accordingly.

- **LinkedIn** (Audience 01): hook in first ~140 characters (before "…see more"). Sweet spot 1,200-1,500 characters. 3-5 hashtags optional at the end (firm/topic tags like #MauriceBlackburn, #AccessToJustice). **MB convention: name the spokesperson lawyer** ("Jonathan Walsh explains.", or tag them by name) and **put the link inline** (a trackable link is fine — MB uses brnw.ch/lnkd.in) often citing the source outlet ("Read the full article via the AFR:"). Tag partner orgs/people where relevant. Slightly more professional register, but the same empathy and hedged CTAs.
- **Instagram** (Audience 02): hook in first 125 characters. Requires media. 3-5 niche/campaign hashtags at the end (e.g. #NAIDOCWeek). One CTA. **MB convention: CTA is "link in our bio" / "🔗 Link in bio" (no inline links)**; educational posts use the carousel "Swipe through…" mechanic; warmer, more emoji, may use POV/trend hooks for lighter topics. Spokesperson usually not named in the caption.
- **TikTok caption**: under 150 characters for most posts. 5 hashtags max. Keyword in the first 30 characters. If the request is for a video script, format as HOOK / BODY / CTA with [on-screen text] and [b-roll] cues, spoken length under 45 seconds. Any video needs burned-in captions (MB burns bold white captions on all video).
- **Meta (Facebook)**: 40-80 characters optimal for the hook. No hashtags. No engagement bait ("comment YES").

When a post is for multiple channels, write the longer-platform version first, then ask if a shortened version is needed for the others. When the same campaign runs on both LinkedIn and Instagram, keep the core message but apply each channel's convention above (LinkedIn adds the named lawyer + inline link; Instagram uses "link in bio" + campaign hashtags) — this mirrors how MB actually cross-posts.

## What NOT to Do

- Don't skip the compliance pass to save a step — it comes before the CTA and before grading, every time.
- Don't invent a client name, number, or outcome to strengthen a hook or body.
- Don't ask upfront whether to use em dashes — apply MB's default style, and only the CTA choice gets a follow-up question.
- Don't pile on hashtags where they hurt (LinkedIn, Facebook, TikTok beyond 5).
- Don't write 3 versions and ask the user to pick. Pick one strong version; they can ask for an alternate.
- Don't include the hook category name or grading details inside the actual post text — those are for the meta-output only.
- Don't hand back a placeholder creative for the user to fill in manually — place the copy into the new design via the editing transaction, fit it to the layout, and render a thumbnail so overflow is caught before saving. **Never edit the brand template itself** — always work on a new design created from it. Only claim text is placed after `perform-editing-operations` returns success and you've seen the thumbnail.
