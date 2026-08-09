#!/usr/bin/env bash
# Installs the doc-consistency check as a git pre-push hook.
# Run once per clone:  bash scripts/install-hooks.sh
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p .git/hooks
cat > .git/hooks/pre-push <<'HOOK'
#!/usr/bin/env bash
# Auto-installed by scripts/install-hooks.sh. Blocks a push when docs drift.
exec bash "$(git rev-parse --show-toplevel)/scripts/check-docs.sh"
HOOK
chmod +x .git/hooks/pre-push
echo "Installed .git/hooks/pre-push -> scripts/check-docs.sh"
