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

## What's *not* in this public repo

Two things are deliberately left out of `brand-mb` here, both for licensing/sensitivity reasons:

- **Reader Pro**, MB's licensed display font — not ours to redistribute publicly. Headings fall back to a serif system font instead. If you're working from inside MB's internal Claude workspace, the full font files are bundled there.
- **The internal "Brand guidelines" writing-guide PDF** — the source document behind `tone-of-voice.md`. The distilled summary in this skill is safe to share publicly; the original internal PDF isn't.

Everything else (colours, type scale, logo, the full tone-of-voice and brand-history summaries) is complete and accurate here.
