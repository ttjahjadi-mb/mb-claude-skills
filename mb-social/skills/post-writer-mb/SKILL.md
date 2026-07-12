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

### Step 8: Offer a matching creative (Canva, optional)

If the user asks for a visual, or after presenting the final post ask "want a matching creative for this too?"

If Canva's MCP tools are connected (check via a quick tool search — `mcp__claude_ai_Canva__generate-design` etc.), call `generate-design` with:
- `design_type`: Instagram → `instagram_post`, Meta/Facebook → `facebook_post`. LinkedIn and TikTok have no native Canva type — generate as `instagram_post` and use `resize-design` afterward (LinkedIn: 1200x627 or keep 1080x1080; TikTok/Reels: 1080x1920).
- `brand_kit_id`: MB's kit — look it up via `list-brand-kits` if not already known (as of 2026-07-12 there is exactly one MB brand kit).
- `query`: describe the post's tone, hook, and CTA as creative direction — mood, subject matter, key phrase to feature.

**Be upfront with the user about what this actually does**: `generate-design` treats your query as creative direction, not literal copy to place on the image — tested 2026-07-12 on a real post, it produced an on-brand design (correct MB colours, warm human photography) but with its own headline text, not the post's exact hook/CTA. Present it as a strong on-brand starting point to open and adjust in Canva (share the `edit_url`), not a finished, publish-ready asset. Don't claim it placed the exact post copy unless you've verified it did.

After `generate-design` returns a candidate, call `create-design-from-candidate` to save it to a real, editable design and get `edit_url`/`view_url` — give the user both.

If Canva isn't connected, say so plainly and suggest asking Cowork directly to mock up a creative as a fallback, or noting it for manual creation later.

## Platform Constraints

- **LinkedIn**: hook in first ~140 characters (before "…see more"). Sweet spot 1,200-1,500 characters. No external links in the body. 3-5 hashtags optional at the end.
- **Instagram**: hook in first 125 characters. Requires media. 3-5 niche hashtags at the end. One CTA.
- **TikTok caption**: under 150 characters for most posts. 5 hashtags max. Keyword in the first 30 characters. If the request is for a video script, format as HOOK / BODY / CTA with [on-screen text] and [b-roll] cues, spoken length under 45 seconds.
- **Meta (Facebook)**: 40-80 characters optimal for the hook. No hashtags. No engagement bait ("comment YES").

When a post is for multiple channels, write the longer-platform version first, then ask if a shortened version is needed for the others.

## What NOT to Do

- Don't skip the compliance pass to save a step — it comes before the CTA and before grading, every time.
- Don't invent a client name, number, or outcome to strengthen a hook or body.
- Don't ask upfront whether to use em dashes — apply MB's default style, and only the CTA choice gets a follow-up question.
- Don't pile on hashtags where they hurt (LinkedIn, Facebook, TikTok beyond 5).
- Don't write 3 versions and ask the user to pick. Pick one strong version; they can ask for an alternate.
- Don't include the hook category name or grading details inside the actual post text — those are for the meta-output only.
- Don't claim a Canva-generated creative shows the post's exact wording unless you've actually checked the design — it's a creative starting point, not guaranteed verbatim text placement.
