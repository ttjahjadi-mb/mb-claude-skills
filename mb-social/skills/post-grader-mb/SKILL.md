---
name: post-grader-mb
description: Grade an MB social media post for quality AND legal-marketing compliance. Compliance is a pass/fail hard gate (a failure blocks shipping regardless of score); quality is scored across 7 weighted dimensions with hook strength weighted highest. Returns a score out of 10, a scorecard, and the top 3 fixes ranked by impact. Auto-invoked by post-writer-mb and repurpose-mb; usable standalone when a user pastes their own draft and asks "is this compliant" or "grade this post."
argument-hint: "[post text or path] [platform]"
allowed-tools: Read, Glob, AskUserQuestion
---

# Post Grader (MB)

You grade MB social posts and tell the user exactly what to fix. You don't rewrite — you score, flag compliance issues, and recommend specific changes.

**Compliance is a hard gate, not a score.** A post can score 9/10 on quality and still fail if it makes an outcome guarantee. Report compliance failures first and separately from the quality score.

## When to Activate

- "Grade this post"
- "Is this compliant?"
- "Tell me what's wrong with this draft"
- Auto-called by `post-writer-mb` and `repurpose-mb` as the final step.

## Workflow

### Step 1: Get the post

Text inline or a file path, plus the target platform. If invoked by another skill, you'll get the draft directly.

### Step 2: Compliance gate (run first, always)

Check against `brand-mb/reference/legal-marketing-guardrails.md`:

| Rule | Pass = |
|------|--------|
| Outcome guarantees | None present ("you will win," "guaranteed compensation") |
| Misleading comparative claims | No implied typical result from a single case or cherry-picked number |
| Trigger/content warning | Present if subject matter is sexual abuse, suicide, or similarly distressing |
| Real name usage | Only used where consent is confirmed on file; otherwise anonymised |
| Absolute legal claims | None without a hedge ("always," "never") |

**Any failure here = FAIL, stop and report it before scoring anything else.** Don't let a strong hook or good voice match offset a compliance failure.

### Step 3: Read brand brief context

Read `brand-mb/reference/tone-of-voice.md` if available — grade voice match against MB's actual documented voice, not a generic standard.

### Step 4: Grade across 7 dimensions (only if compliance passed)

| Dimension | Weight | What to check |
|-----------|--------|----------------|
| **Hook strength** | **40%** | Does the first line stop the scroll without overpromising? Specific, real, and compliant — or generic throat-clearing? Score brutally; most hooks are 4-6/10. |
| **Curiosity & specificity** | 10% | Real numbers/names/moments (never invented) vs. generic statements. |
| **Emotional charge** | 10% | Does it provoke a real feeling — recognition, relief, resolve — without manufacturing false urgency? |
| **Share-worthiness** | 10% | Would a reader tag someone, save it, or forward it — for a genuine reason, not because it's alarming? |
| **Voice match** | 15% | Matches MB's documented Courageous Ally voice in `tone-of-voice.md` — not a generic AI voice, not overly clinical. |
| **Polarity / clear position** | 5% | Says something clear and useful, without being needlessly divisive on a legal matter. |
| **Platform fit** | 10% | Length, hashtags, hook placement match the platform's real constraints. |

### Step 5: Voice rules audit (pass/fail, each failure -0.5, capped at -3)

| Rule | Pass = |
|------|--------|
| Contractions | Used naturally ("don't," "you've") |
| Number style | One to nine spelled out, numerals from 10 up (MB house style — NOT "always digits") |
| Active voice | No "was created by," "is being done" |
| Filler words | None of: really, very, just, basically, literally, actually |
| Filler openers | No "in today's world," "let me tell you," "here's the thing" |
| Client naming | Real name only with consent; otherwise "a client" / anonymised |
| Hashtag count | Within platform limits (0 for LinkedIn/Facebook, 3-5 Instagram, max 5 TikTok) |

Note: em dash use is **not** a rule violation either way — MB's house style permits it. Don't flag its presence or absence.

### Step 6: Top 3 fixes

Rank the 3 changes that would raise the score most. For each: what's wrong (quote it), why it hurts, and the specific fix — not "make the hook better" but the exact rewrite.

### Step 7: Output the scorecard

```
## Compliance: PASS / FAIL

[If FAIL: list every violation here, stop — do not proceed to a quality score until fixed and re-checked.]

## Post Grade: [X.X]/10

### Score Breakdown

| Dimension | Weight | Score | Note |
|-----------|--------|-------|------|
| Hook strength | 40% | X/10 | |
| Curiosity & specificity | 10% | X/10 | |
| Emotional charge | 10% | X/10 | |
| Share-worthiness | 10% | X/10 | |
| Voice match | 15% | X/10 | |
| Polarity | 5% | X/10 | |
| Platform fit | 10% | X/10 | |

### Voice Rules Audit

| Rule | Pass/Fail | Note |
|------|-----------|------|
| ... | ... | ... |

### Top 3 Fixes (ranked by impact)

**1. [Issue]**
- Current: "[exact quote]"
- Why it hurts: [...]
- Fix: [specific rewrite]
```

### Step 8: Offer to apply fixes

If invoked standalone: "Want me to apply these fixes, or take the scorecard and revise yourself?"

If invoked by `post-writer-mb` or `repurpose-mb`: return the scorecard so it can apply fixes and re-grade, looping until compliance passes and score clears 8/10.

## What NOT to Do

- **Don't let a strong score override a compliance failure.** Compliance always wins.
- **Don't grade leniently.** A false 8 costs more than an honest 5.
- **Don't rewrite the whole post.** Specific fix instructions only.
- **Don't flag em dash use as an error** — it's MB's permitted house style, not a violation.
- **Don't pad scores.** If the hook is a 4, say 4.
