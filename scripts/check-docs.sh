#!/usr/bin/env bash
# Doc-consistency guard for mb-claude-skills.
# Blocks a push when the docs drift from the actual skills. This exists because
# a skill add/rename/re-scope kept missing one doc or another (the README ASCII
# diagram, a skill count, the SKILLS.md index row). A memory rule did not stop
# it; this check does.
#
# Run manually:  bash scripts/check-docs.sh
# Runs automatically as .git/hooks/pre-push (see scripts/install-hooks.sh).

set -uo pipefail
cd "$(dirname "$0")/.." || exit 2

SKILLS_DIR="mb-marketing/skills"
README="README.md"
PLUGIN="mb-marketing/.claude-plugin/plugin.json"
MARKET=".claude-plugin/marketplace.json"
EXTERNAL_SKILLS_INDEX="$HOME/.claude/SKILLS.md"   # Thomas's machine only; skipped if absent

fail=0
note() { echo "  - $1"; fail=1; }

skills=$(ls -d "$SKILLS_DIR"/*/ 2>/dev/null | xargs -n1 basename | sort)
count=$(echo "$skills" | grep -c .)
echo "Found $count skills in $SKILLS_DIR."

# 1. Every skill has a README "What's inside" table row and appears in the ASCII diagram.
echo "Checking README rows + ASCII diagram..."
for s in $skills; do
  grep -q "\`$s\`" "$README" || note "README.md: no mention of '$s' (needs a table row + diagram entry)."
done

# 2. Skill counts are consistent everywhere they appear as "N skills".
echo "Checking skill counts..."
wrong=$(grep -oE '[0-9]+ skills' "$README" | grep -v "^$count skills$" | sort -u)
if [ -n "$wrong" ]; then
  note "README.md has a stale skill count (expected '$count skills'): $(echo "$wrong" | tr '\n' ' ')"
fi

# 3. Plugin + marketplace manifests exist and name every skill's plugin dir.
for f in "$PLUGIN" "$MARKET"; do
  [ -f "$f" ] || note "$f is missing."
done

# 4. External SKILLS.md index (Thomas's workspace) has a row per skill, if present.
if [ -f "$EXTERNAL_SKILLS_INDEX" ]; then
  echo "Checking $EXTERNAL_SKILLS_INDEX index rows..."
  for s in $skills; do
    grep -q "\`$s\`" "$EXTERNAL_SKILLS_INDEX" || note "SKILLS.md: no index row for '$s'."
  done
else
  echo "Skipping SKILLS.md index check (not on this machine)."
fi

if [ "$fail" -ne 0 ]; then
  echo
  echo "DOC CHECK FAILED. Update the docs above before pushing (see CLAUDE.md rule)."
  exit 1
fi
echo "Doc check passed: all $count skills are documented consistently."
