#!/usr/bin/env bash
# Fails if anything internal is in the published files: IP addresses, credentials, local paths, private repository names.
set -euo pipefail
cd "$(dirname "$0")/.."
bad=0
check() { # description, pattern
  if grep -rIEn --exclude-dir=.git --exclude-dir=node_modules --exclude-dir=scripts --exclude-dir=.github --exclude=package-lock.json --exclude=pnpm-lock.yaml -e "$2" . ; then echo "leak guard: $1" >&2; bad=1; fi
}
check "an IPv4 address" '(^|[^0-9.])[0-9]{1,3}(\.[0-9]{1,3}){3}([^0-9]|$)'
check "a credential" 'Admin@[0-9]|(password|passwd|secret|api[_-]?key)[[:space:]]*[:=][[:space:]]*[^[:space:]]|BEGIN [A-Z ]*PRIVATE KEY'
check "a local path or internal host" '/Users/|/home/|\.svc\b|nip\.io|localhost:[0-9]'
check "a personal identifier" 'ssahani|[[:space:]]sus@'
check "a private repository name" 'zyvor-zyvora([^-]|$)'
exit $bad
