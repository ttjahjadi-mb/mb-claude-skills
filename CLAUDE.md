# mb-claude-skills workstation

Public GitHub repo (`ttjahjadi-mb/mb-claude-skills`), a Claude plugin marketplace for the Maurice Blackburn marketing team. One plugin, `mb-marketing`, all skills live under `mb-marketing/skills/`.

## Rules

- **Mandatory: after every commit to this repo, update EVERY piece of documentation in the same commit (or the next one before pushing) so it reflects the latest change.** Adding, renaming, removing, or re-scoping a skill means updating ALL of these, not just some:
  - `README.md`: the "What's inside" table row, the "Try it" examples, the **"How Skills Work Together" ASCII diagram** (add/remove the skill in the right column AND the "Skills cross-reference each other" block), and **every skill-count** ("N skills" appears in the intro line, the install step, and the "All N skills ship…" paragraph — grep `skills` and fix all).
  - `mb-marketing/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` descriptions.
  - The external `~/.claude/SKILLS.md` index and the AI Pilot Workshop dashboard `content.json` skill list (Marketing skill count + row) live outside this repo but must be updated in the same working session.
  - After editing, re-grep the repo for the old count and the old skill list to confirm nothing was missed. This rule exists because the ASCII diagram and the skill counts were missed on the `qa-creative-mb` add, and the `SKILLS.md` index row on the `seo-content-mb` re-scope (both 2026-08-09).
- **This is enforced mechanically, do not rely on memory.** `scripts/check-docs.sh` verifies every skill has a README row + diagram mention, that all "N skills" counts match the real count, and that the external `~/.claude/SKILLS.md` index has a row per skill. It runs automatically as a **git pre-push hook** (install once per clone: `bash scripts/install-hooks.sh`) and blocks the push if a doc is out of sync. Run it manually any time: `bash scripts/check-docs.sh`. If a push is blocked, fix the listed docs, never bypass the hook.
- Installing this plugin does not auto-update. Note this in README when instructions change so users know to remove + re-add.
- No em dashes in README prose additions, match the rest of this workspace's house style.
- Before pushing anything here, scan for secrets/credentials and internal-only links (Notion, Jira, monday), this repo is public.
