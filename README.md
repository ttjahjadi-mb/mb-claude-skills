# MB Claude Skills

Free Claude skills for the Maurice Blackburn marketing team — brand reference and brand-vs-competitor comparison, ready to use in any Claude conversation.

## Install (claude.ai web or Cowork — no tech setup needed)

This is the easiest path if you're not using Claude Code:

1. Download this repo as a zip: click the green **Code** button above → **Download ZIP**.
2. Unzip it.
3. In Claude, open **Settings → Capabilities → Skills** (the exact menu name may vary slightly depending on your Claude plan/app).
4. Upload the skill folder for `mb-brand/skills/brand-mb` and `mb-brand/skills/brand-analyst-mb` — each one needs its `SKILL.md` plus any `reference/` and `assets/` files alongside it.

If you get stuck, ask Thomas (Cowork/Claude Code) or check Anthropic's own help docs for uploading custom skills — the upload step is an Anthropic product feature, not something specific to this repo.

## Install (Claude Code — for anyone comfortable with a terminal)

```
/plugin marketplace add ttjahjadi-mb/mb-claude-skills
/plugin install mb-brand@mb-claude-skills
```

Then just mention brand-related work in conversation (or run `/mb-brand` if your Claude Code version surfaces it as a command) — the skills trigger automatically when relevant. To update later: `/plugin update`.

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

## Keeping this updated

This repo is a mirror of the internal working copy at `Tony 2.0/.claude/skills/` in Thomas's Claude workspace. If brand tokens, tone of voice, or history change, that internal copy gets updated first, then re-mirrored here (with the font/PDF stripped again). Don't expect hand-edits made only in this repo to persist — flag any needed change to Thomas instead.
