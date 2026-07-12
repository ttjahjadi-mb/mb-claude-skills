# MB Claude Skills

Free Claude skills for the Maurice Blackburn marketing team — brand reference, brand-vs-competitor comparison, and on-brand social content creation, ready to use in any Claude conversation.

## Install (claude.ai / Cowork)

1. Open **Extensions** → **Browse extensions**.
2. Go to the **Plugins** tab.
3. Click **Add GitHub**.
4. Paste `ttjahjadi-mb/mb-claude-skills` into the URL field and click **Sync**.
5. Find **mb-brand** and **mb-social** in the list and install/enable both. (`mb-social` reads MB's brand voice from `mb-brand`, so install both together.)

That's it — no downloading, no manual file uploads. Because it's synced from this GitHub repo, updates here reach you automatically; you don't need to redo this setup when the brand tokens, tone of voice, or skill logic change.

## Install (Claude Code)

```
/plugin marketplace add ttjahjadi-mb/mb-claude-skills
/plugin install mb-brand@mb-claude-skills
/plugin install mb-social@mb-claude-skills
```

Then just mention brand or social-content work in conversation — the skills trigger automatically when relevant. To update later: `/plugin update`.

## What's inside

| Skill | When it kicks in |
| --- | --- |
| `brand-mb` | Building anything MB-branded (site component, deck, dashboard, document) that needs exact colours/fonts/logo, or writing content that needs to sound like MB rather than a generic assistant |
| `brand-analyst-mb` | Asking "how does our brand compare to [competitor]" — a quick, conversational brand-vs-competitor read |
| `post-writer-mb` | "Write me a post about X for [platform]" — produces a hook + body + CTA, on-brand, compliance-checked, and graded before you see it |
| `post-grader-mb` | "Is this post compliant/any good?" — scores a draft and lists the top 3 fixes; checks legal-marketing compliance as a hard pass/fail gate before anything else |
| `viral-hooks-mb` | Needs a strong opening line — a curated hook library filtered for a law firm's voice and compliance obligations (no fake urgency, no fabricated confessions) |
| `repurpose-mb` | "Turn this case update into a week of content" — one long input becomes a batch of platform-native posts across LinkedIn, Instagram, TikTok, and Meta |

`post-writer-mb`, `post-grader-mb`, `viral-hooks-mb`, and `repurpose-mb` are all in the **mb-social** plugin, and all read `mb-brand`'s tone-of-voice, brand guidelines, and a shared legal-marketing guardrails file — install `mb-brand` alongside `mb-social` for these to work.

## Try it — example prompts

**brand-mb** (triggers automatically, no need to ask for it by name):

- "Build me a one-pager in our brand colours for the new claims process."
- "Draft an EDM about the Dr Simon Gordon gynaecological investigation." — writes in the Courageous Ally voice, uses the real case history.
- "Write social copy for a class action update." — applies the audience split (familiar vs. not familiar with the law), uses the person's name instead of "our client"/"the plaintiff."
- "What's MB's brand personality?"
- "When was MB founded?" — sourced facts, not a guess.

**brand-analyst-mb** (ask for a brand comparison directly):

- "How does our brand compare to Slater and Gordon?" — live research on their site/positioning, scored against MB's documented voice/colours.
- "What's Shine Lawyers doing differently on their homepage?"

Good live demo: pick a real competitor name in the room and run `brand-analyst-mb` on the spot — it researches fresh each time rather than relying on memory of what a firm's brand used to look like.

**mb-social** (post-writer-mb, post-grader-mb, viral-hooks-mb, repurpose-mb):

- "Write me a LinkedIn post about the Dr Simon Gordon investigation."
- "Give me a hook for a post about workplace injury claims."
- "Is this post compliant?" (paste a draft) — checks for outcome guarantees, misleading claims, and consent issues before it even scores the writing.
- "Turn this case update into posts for our channels." — produces a batch across LinkedIn, Instagram, TikTok, and Meta.

Compliance is a hard gate on every one of these — a post that scores well but makes an outcome guarantee or skips a required trigger warning will not be returned as-is. MB's house style permits the em dash and these skills apply it by default; the only thing they'll ask you to confirm is the CTA (Free claim check, Ask Morry AI, Chat with Morry AI, Request a callback, or Get in touch).

## What's *not* in this public repo

Two things are deliberately left out of `brand-mb` here, both for licensing/sensitivity reasons:

- **Reader Pro**, MB's licensed display font — not ours to redistribute publicly. Headings fall back to a serif system font instead. If you're working from inside MB's internal Claude workspace, the full font files are bundled there.
- **The internal "Brand guidelines" writing-guide PDF** — the source document behind `tone-of-voice.md`. The distilled summary in this skill is safe to share publicly; the original internal PDF isn't.

Everything else (colours, type scale, logo, the full tone-of-voice and brand-history summaries) is complete and accurate here.
