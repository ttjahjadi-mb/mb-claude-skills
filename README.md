# MB Claude Skills

Free Claude skills for the Maurice Blackburn marketing team — brand reference and brand-vs-competitor comparison, ready to use in any Claude conversation.

## Install (claude.ai / Cowork)

1. Open the **Directory** panel and go to **Plugins**.
2. Click **+** → **Add marketplace**.
3. Paste `ttjahjadi-mb/mb-claude-skills` into the URL field and click **Sync**.
4. Find the **mb-brand** plugin in the list and install/enable it.

That's it — no downloading, no manual file uploads. Because it's synced from this GitHub repo, updates here reach you automatically; you don't need to redo this setup when the brand tokens, tone of voice, or history change.

## Install (Claude Code)

```
/plugin marketplace add ttjahjadi-mb/mb-claude-skills
/plugin install mb-brand@mb-claude-skills
```

Then just mention brand-related work in conversation — the skills trigger automatically when relevant. To update later: `/plugin update`.

## What's inside

| Skill | When it kicks in |
| --- | --- |
| `brand-mb` | Building anything MB-branded (site component, deck, dashboard, document) that needs exact colours/fonts/logo, or writing content that needs to sound like MB rather than a generic assistant |
| `brand-analyst-mb` | Asking "how does our brand compare to [competitor]" — a quick, conversational brand-vs-competitor read |

## Try it — example prompts

**brand-mb** (triggers automatically, no need to ask for it by name):

- "Build me a one-pager in our brand colours for the new claims process."
- "Draft an EDM about the BRCA1 gene patent case." — writes in the Courageous Ally voice, uses the real case history.
- "Write social copy for a class action update." — applies the audience split (familiar vs. not familiar with the law), uses the person's name instead of "our client"/"the plaintiff."
- "What's MB's brand personality?"
- "When was MB founded?" — sourced facts, not a guess.

**brand-analyst-mb** (ask for a brand comparison directly):

- "How does our brand compare to Slater and Gordon?" — live research on their site/positioning, scored against MB's documented voice/colours.
- "What's Shine Lawyers doing differently on their homepage?"

Good live demo: pick a real competitor name in the room and run `brand-analyst-mb` on the spot — it researches fresh each time rather than relying on memory of what a firm's brand used to look like.

## What's *not* in this public repo

Two things are deliberately left out of `brand-mb` here, both for licensing/sensitivity reasons:

- **Reader Pro**, MB's licensed display font — not ours to redistribute publicly. Headings fall back to a serif system font instead. If you're working from inside MB's internal Claude workspace, the full font files are bundled there.
- **The internal "Brand guidelines" writing-guide PDF** — the source document behind `tone-of-voice.md`. The distilled summary in this skill is safe to share publicly; the original internal PDF isn't.

Everything else (colours, type scale, logo, the full tone-of-voice and brand-history summaries) is complete and accurate here.
