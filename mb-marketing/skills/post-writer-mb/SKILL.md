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

After presenting the post, offer: "Want a matching MB-brand creative drafted for this?" If Canva's MCP tools are connected (quick tool search for `mcp__claude_ai_Canva__*`), draft it on a **real MB brand template** with the copy already placed — **never** hand back a placeholder to paste manually. MB's templates aren't autofill-enabled (`get-brand-template-dataset` → `{}`), but you place copy programmatically via the design-editing API, which is the path used here.

> **Canva tool set (verified 2026-08-09):** the editing flow is `create-design-from-brand-template` → **`read-design`** (with `open_transaction: true`) to see elements + get a `transaction_id` → **`edit-design`** (pass `operations`, then call again with `finalize: "commit"` or `"cancel"`) → `upload-asset-from-url` for images. This replaced the older `start-editing-transaction`/`perform-editing-operations`/`commit-editing-transaction`/`cancel-editing-transaction` tools named below. Canva renames these periodically — if a named tool 404s, search `mcp__claude_ai_Canva__*` and use the current equivalent; the *sequence* (create → read+open transaction → edit → commit) is what matters. `edit-design` operations include `update_title`, `replace_text`, `find_and_replace_text`, `update_fill`/`insert_fill` (images), `delete_element`.

> **Golden rule: never edit the brand template itself.** `create-design-from-brand-template` spins up a *new* design from the template (the template stays read-only). All edits happen on that new design only.

**1. Pick by the `MB -` title-prefix rule (not a frozen ID list).** MB's Canva account uses a **three-way naming convention** (verified 2026-08-08): every brand template is prefixed by its brand identity.

- **`MB -`** → standalone Maurice Blackburn brand. **These are the only ones this skill uses by default.**
- **`Union -`** → MB×AWU co-brand, carries a *locked* "In partnership with Maurice Blackburn + AWU" footer that can't be removed (verified: `delete_element` → "Cannot delete a locked element"). Correct **only** when the post is genuinely an MB+AWU union / EBA / organised-workplace matter — and only after you **confirm with the user** ("This is a union co-branded template with a fixed AWU footer — use it, or a standalone MB one?"). Never for a generic MB post.
- **`CFA`** → Claims Funding Australia, a **separate brand** (navy). Never use for an MB social post.

**How to select:** call `search-brand-templates` (broad query, or by the specific title), then **filter the results to titles that start with `MB - `**. Ignore anything titled `Union -`, `CFA`, or with no MB prefix. Route by the request's **topic first**, then format:

- **Witness ad / witness appeal request** → offer these four MB witness templates (present all four so the user chooses — see 1b):
  - `MB - Video Witness Ad` (1080×1920, 9:16 video/story)
  - `MB - Witness Ad_129x188mm_PRINT` (129×188mm print flyer)
  - `MB - Witness Ad_134x188mm_PRINT` (134×188mm print flyer)
  - `MB - Abuse Witness Ad_1920x1080px` (1920×1080 video, for abuse-investigation appeals)
- **Class action post** → three MB class-action templates (present all three, let the user pick — see 1b):
  - `MB - Class Action Template - Image - Instagram` (1080×1350, **image-capable**) — 2 text fields (a short headline + a "link in bio" CTA line) and 2 replaceable image slots (full-page background + an inner image). Use when a banner/image is supplied (e.g. the campaign banner goes in the background slot). The detailed copy lives in the caption, not on the card.
  - `MB - Class Action Template - No Image - Instagram` (1080×1350, text-only) — class-action layout without an image slot.
  - `MB - Quote - x 3 versions` (text-only) — pull-quote / statement style.
- **Anything else MB** → pick the best-fit `MB -` template for the content, by format:

| Post format | MB template title (starts with `MB - `) |
|---|---|
| Pull-quote / striking stat / statement (square) | MB - Quote - x 3 versions |
| Pull-quote (LinkedIn landscape) | MB - Quote - LinkedIn Landscape 1200x627 |
| Client testimonial / review (feed, square) | MB - 5 star Google review - White |
| Client testimonial / review (story / reel, 4:5–9:16) | MB - 5 star Google review - White (the 450×800 one) |
| Award / recognition / milestone (with photo) | MB - FF Awards template - with photo |
| Event promo | MB - Name of Event |

**It is not a hard allowlist** — you filter live by the `MB -` prefix each run, so any new `MB -` template MB publishes is picked up automatically; match the content to the closest one. **Connector-visibility caveat:** the Connect API only returns a subset of MB's Canva Brand Templates. Some listed here (verified 2026-08-08: `MB - Witness Ad_134x188mm_PRINT`, `MB - Abuse Witness Ad_1920x1080px`, `MB - Name of Event`) may not come back from `search-brand-templates` yet, and the Abuse ad is a flattened design with no editable text. Handle that gracefully per 1b — never substitute a `Union -`/`CFA` template to compensate. If no `MB -` template fits at all, **stop and tell the user** (no-fit rule below) — never invent a design.

**1b. Confirm the template with the user before building — always ask, don't just pick.** After routing, present the shortlist and let the user choose *before* you create any design. Always ask when more than one template fits:
- **Witness ad** → present all four (`MB - Video Witness Ad` 9:16 video; `MB - Witness Ad_129x188mm_PRINT` print; `MB - Witness Ad_134x188mm_PRINT` print; `MB - Abuse Witness Ad_1920x1080px` 16:9 video for abuse appeals). Ask which.
- **Pull-quote** → `MB - Quote - x 3 versions` (square feed) vs `MB - Quote - LinkedIn Landscape 1200x627`.
- **Class action** → the three class-action templates: `MB - Class Action Template - Image - Instagram` (image-capable — pick when a banner/photo is supplied), `MB - Class Action Template - No Image - Instagram` (text-only), `MB - Quote - x 3 versions` (pull-quote style). Ask which; if the post needs an image on the card, steer to the Image one.
- **Testimonial / review** → `MB - 5 star Google review - White` square feed vs the 450×800 story.

Show it as a short pick-list with a one-line "what it is" per option. When exactly one fits, name it and proceed unless the user redirects. Only build the design the user confirmed.

**Graceful fallback when the confirmed template can't be built.** Two failure modes, both expected for some witness options: (a) `search-brand-templates` doesn't return the chosen title (not yet exposed to the connector — e.g. the 134mm and Abuse ads today), or (b) `create-design-from-brand-template` + `start-editing-transaction` succeeds but returns **no editable text** (`richtexts` empty — the Abuse ad is a flattened design). In either case do NOT silently swap or invent — tell the user plainly: *"`MB - Abuse Witness Ad_1920x1080px` isn't reachable through Canva's API yet (or has no editable text I can fill). Options: I open it for you to edit manually in Canva, or build one of the reachable witness templates (`MB - Video Witness Ad` / `MB - Witness Ad_129x188mm_PRINT`) instead."* Give the template's `create_url`/`view_url` for the manual route. Only proceed on the user's choice.

**2. Create a new design from the confirmed template:** `create-design-from-brand-template` → new `design_id` + `edit_url`/`view_url`. (Brand-template designs can lag a moment; if a later call says "not found", recreate and use the fresh id.)

**2b. Need a different size than the template's native one for this platform** (e.g. LinkedIn landscape 1200×627 from a template that defaults to square)? `resize-design` on the design from step 2 — reflows the layout and is safe as a one-off (verified clean). Continue the rest of the flow on the *resized* design's id. **Never call `publish-brand-template` on a resized design** — confirmed bug: it errors immediately and permanently orphans the design. Resize is fine for a single creative; it is not a way to save a new template.

**2c. Name the design uniquely per request** (do this every time a creative is created). The design title must follow **`PRACTICE AREA - REQUEST - DDMMYYYY`** (spaces around the hyphens; date is today, `DDMMYYYY`, no separators). Example: `Class Actions - Allianz Social Post - 08082026`.
- **PRACTICE AREA**: derive from the post's subject — Class Actions, Abuse, Workplace Injury, Superannuation & Insurance, Road Injury, Medical Negligence, Public Liability, Wills & Estates, etc.
- **REQUEST**: a short human label for this specific piece (e.g. `Allianz Social Post`, `Bairnsdale West Witness Ad`, `TPD Review`).
- **DDMMYYYY**: today's date. Get it reliably (don't guess) — e.g. `TZ="Australia/Sydney" date "+%d%m%Y"`.

**Show the user the proposed filename and let them confirm or tweak it before applying.** Then set it with `update_title` inside the editing transaction (step 4; `update_title` is allowed even on `is_responsive: true` pages). Never leave the default "Copy of …" title.

**3. Open an editing transaction:** `start-editing-transaction` on the *new* design. The response returns every text element's `element_id` and its current placeholder text, the `pages` array (note each page's `is_responsive`), and a thumbnail. **Guard:** if it returns no editable text elements (`richtexts` empty — some MB ads are flattened/locked, e.g. the old Abuse Witness ad) or the thumbnail shows a locked AWU partnership footer or CFA branding, do NOT proceed — `cancel-editing-transaction` and tell the user that template can't be auto-filled. (Shouldn't happen if you filtered to the `MB -` prefix; this catches a wrong pick or a flattened MB template.)

**4. Place the copy — fit it to the layout.** For each text element, `perform-editing-operations` with `replace_text` (or `find_and_replace_text`), mapping the post's hook/quote/body/attribution/CTA onto the template's fields. **Fit to the placeholder's length** — if your copy is much longer than what it replaces, it will overflow the fixed text box and collide with elements below (verified failure mode). If it's tight, shorten the copy or pick a roomier template, and **flag it to the user** in the review. On `is_responsive: true` pages, only `update_title`, `replace_text`, `update_fill`, `delete_element`, `find_and_replace_text` are allowed — stick to those.

**5. Attach an image where the template has an image element** (e.g. Image & Solid, review templates, image carousels) and the user supplied one: `upload-asset-from-url` (needs a public image URL) → `update_fill` on that image element with the returned `asset_id`. (Image attach uses `update_fill`/`insert_fill`; text placement is live-verified, image attach is per the API schema — sanity-check the first real run.)

**6. Render for review:** the `perform-editing-operations` response includes a thumbnail — show it in chat. Confirm nothing overflows.

**7. Save + send for review:** `commit-editing-transaction` (saves the *new* design; template untouched). Give the user the `edit_url` + `view_url` + the rendered thumbnail: "Here's the drafted creative — review and tweak in Canva." If a preview looks wrong, `cancel-editing-transaction` instead and redraft.

**No-fit rule — never invent a design.** If no `MB -` template fits the post's format, do NOT fall back to `generate-design`, an AI-generated layout, or a `Union -`/`CFA` template. Tell the user plainly: "None of the standalone `MB -` templates fits this post — want me to use the closest one anyway, use a `Union -` co-brand template (fixed AWU footer), or make this creative manually / add a new MB template?" `generate-design` is off by default because it produces a non-template, off-brand design — the exact thing to avoid. Only use it if the user explicitly asks for an AI-generated creative this time, and then be clear it's not a brand template.

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
