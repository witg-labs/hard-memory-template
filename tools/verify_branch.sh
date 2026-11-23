#!/usr/bin/env bash
# verify_branch.sh - verification gate for delegated-work branches.
# Runs the verification steps in a fixed order so none get skipped:
#   1. Origin check (branch must exist on origin; local-only = stop)
#   1b. SHA receipt check (with --reported-sha: the SHA from the implementer's
#       completion report is compared character for character against the
#       branch head read from origin; any mismatch is a hard fail)
#   2. Full changed-file enumeration vs the brief's allowed list
#   3. CRLF / line-ending scan on changed files
#   4. Forbidden-pattern search on changed files
#   5. Dependency-change detection (package.json / lockfiles)
#   6. Optional: tsc + vitest in a detached worktree of the branch
#
# Usage:
#   verify_branch.sh --repo-dir DIR --branch BRANCH [--base main]
#                    [--reported-sha SHA]
#                    [--allowed file1,file2,...] [--forbidden 'regex']
#                    [--run-tests]
#
# Exit codes: 0 = no flags, 1 = flags raised (a reviewer judges), 2 = cannot verify (origin/base missing)
#
# Step 6 (tsc + vitest) is OFF by default. Enable it with --run-tests, or by
# setting VERIFY_BRANCH_RUN_TESTS=1 in the environment. It needs Node.js and
# a package.json with typescript/vitest in the target repo; leave it off for
# documentation-only repos.
set -u

REPO_DIR="" BRANCH="" BASE="main" ALLOWED="" FORBIDDEN="" RUN_TESTS=0 REPORTED_SHA=""
while [ $# -gt 0 ]; do
  case "$1" in
    --repo-dir) REPO_DIR="$2"; shift 2;;
    --branch) BRANCH="$2"; shift 2;;
    --reported-sha) REPORTED_SHA="$2"; shift 2;;
    --base) BASE="$2"; shift 2;;
    --allowed) ALLOWED="$2"; shift 2;;
    --forbidden) FORBIDDEN="$2"; shift 2;;
    --run-tests) RUN_TESTS=1; shift;;
    *) echo "unknown arg: $1" >&2; exit 2;;
  esac
done
[ "${VERIFY_BRANCH_RUN_TESTS:-0}" = "1" ] && RUN_TESTS=1
[ -n "$REPO_DIR" ] && [ -n "$BRANCH" ] || { echo "usage: verify_branch.sh --repo-dir DIR --branch BRANCH [--base main] [--reported-sha SHA] [--allowed a,b] [--forbidden regex] [--run-tests]" >&2; exit 2; }

FLAGS=0
flag() { echo "FLAG: $1"; FLAGS=1; }

cd "$REPO_DIR" || { echo "FAIL: cannot cd to $REPO_DIR"; exit 2; }
git rev-parse --git-dir >/dev/null 2>&1 || { echo "FAIL: $REPO_DIR is not a git repo"; exit 2; }

echo "=== 1. ORIGIN CHECK: $BRANCH ==="
if ! git ls-remote --exit-code origin "refs/heads/$BRANCH" >/dev/null 2>&1; then
  echo "FAIL: branch $BRANCH is NOT on origin. Stop. Do not verify a local-only branch."
  exit 2
fi
git fetch -q origin "$BRANCH" "$BASE" 2>/dev/null
BRANCH_SHA=$(git rev-parse "origin/$BRANCH")
BASE_SHA=$(git rev-parse "origin/$BASE" 2>/dev/null) || { echo "FAIL: base $BASE not on origin"; exit 2; }
echo "branch origin/$BRANCH @ $BRANCH_SHA"
echo "base   origin/$BASE @ $BASE_SHA"

echo "=== 1b. SHA RECEIPT CHECK ==="
if [ -n "$REPORTED_SHA" ]; then
  REPORTED_SHA=$(printf '%s' "$REPORTED_SHA" | tr -d '[:space:]')
  if [ "$REPORTED_SHA" = "$BRANCH_SHA" ]; then
    echo "SHA CHECK: PASS. Reported SHA matches the origin head exactly."
  else
    echo "SHA CHECK: FAIL. Reported SHA does not match the origin head."
    echo "  reported: $REPORTED_SHA"
    echo "  origin:   $BRANCH_SHA"
    echo "Origin is the only source of truth for a commit SHA. A reported SHA is"
    echo "evidence to be checked, never the value to trust. Verification stops here."
    exit 2
  fi
else
  echo "(no --reported-sha given; the origin head above is the authoritative SHA)"
fi

echo "=== 2. FULL CHANGED-FILE LIST (origin/$BASE...origin/$BRANCH) ==="
CHANGED=$(git diff --name-only "origin/$BASE...origin/$BRANCH")
if [ -z "$CHANGED" ]; then echo "(no changes)"; flag "branch has no diff vs base"; fi
echo "$CHANGED"
echo "--- diff stat ---"
git diff --stat "origin/$BASE...origin/$BRANCH" | tail -5
if [ -n "$ALLOWED" ]; then
  echo "--- scope check vs allowed list ---"
  IFS=',' read -ra ALLOWED_ARR <<< "$ALLOWED"
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    ok=0
    for a in "${ALLOWED_ARR[@]}"; do [ "$f" = "$a" ] && ok=1; done
    [ "$ok" -eq 0 ] && flag "out-of-scope file changed: $f"
  done <<< "$CHANGED"
  echo "scope check done"
fi

echo "=== 3. CRLF SCAN (repo standard is LF) ==="
while IFS= read -r f; do
  [ -z "$f" ] && continue
  if git show "origin/$BRANCH:$f" 2>/dev/null | grep -q $'\r'; then
    flag "CRLF line endings in: $f"
  fi
done <<< "$CHANGED"
echo "crlf scan done"

echo "=== 4. FORBIDDEN-PATTERN SEARCH ==="
if [ -n "$FORBIDDEN" ]; then
  HITS=$(git grep -n -E "$FORBIDDEN" "origin/$BRANCH" -- $CHANGED 2>/dev/null || true)
  if [ -n "$HITS" ]; then
    echo "$HITS" | head -40
    flag "forbidden pattern '$FORBIDDEN' found (check for real-ID substrings before judging)"
  else
    echo "no hits for: $FORBIDDEN"
  fi
else
  echo "(no --forbidden pattern given; skipped)"
fi

echo "=== 5. DEPENDENCY CHANGES ==="
DEP_CHANGED=$(echo "$CHANGED" | grep -E '(^|/)(package\.json|package-lock\.json|pnpm-lock\.yaml|yarn\.lock)$' || true)
if [ -n "$DEP_CHANGED" ]; then
  echo "$DEP_CHANGED"
  git diff "origin/$BASE...origin/$BRANCH" -- package.json | grep -E '^[+-] *"' | head -30
  flag "dependency files changed (unauthorized deps = send back)"
else
  echo "no dependency files changed"
fi

echo "=== 6. TESTS ==="
if [ "$RUN_TESTS" -eq 1 ]; then
  WT=$(mktemp -d /tmp/verify-branch-XXXXXX)
  git worktree add -q --detach "$WT/wt" "origin/$BRANCH" 2>/dev/null || { echo "FAIL: worktree add failed"; rm -rf "$WT"; exit 2; }
  ( cd "$WT/wt" && [ -f package.json ] && { npm install -q --ignore-scripts 2>/dev/null || true; }
    echo "--- npx tsc --noEmit ---"
    ( cd "$WT/wt" && npx tsc --noEmit 2>&1 | tail -5; echo "tsc exit: $?" )
    echo "--- npx vitest run ---"
    ( cd "$WT/wt" && npx vitest run 2>&1 | tail -8; echo "vitest done" ) )
  git worktree remove --force "$WT/wt" 2>/dev/null
  rm -rf "$WT"
else
  echo "(skipped; pass --run-tests to run tsc + vitest on the branch tree)"
fi

echo "=== VERDICT SHEET ==="
echo "branch: $BRANCH @ $BRANCH_SHA"
echo "files changed: $(echo "$CHANGED" | grep -c .)"
if [ "$FLAGS" -eq 0 ]; then echo "FLAGS: none"; else echo "FLAGS: raised above - reviewer judgment required"; fi
exit "$FLAGS"
