# Tools

The enforcement scripts. The hard rules in `rules/` state what must be true; these scripts are how you check it. Each one exists to enforce a specific rule, and each reports findings without printing the values it matched.

| Script | Enforces | What it does |
|---|---|---|
| `check_facts_freshness.py` | HR-006, "Actionable facts carry a source and a date" | Reads `registers/FACTS.md` and lists every fact whose Verified date is more than 60 days old, or cannot be parsed. Exit 1 when anything is stale. Run it monthly, or let CI run it. |
| `check_forbidden_patterns.py` | HR-011, "No secrets in memory" | Scans a tree for credential-shaped strings, dump and key files by extension, and raw genotype data headers. Findings are file, line, and category only; matched values are never printed. This file is the single source for the pattern list. `--self-test` proves the gate catches a dummy credential. |
| `render_trigger_files.py` | HR-015, "Rules change deliberately, in the open" | Writes the pinned rules version as a stamp line into each trigger file (the files that carry standing guidance for an AI tool), so any session can name the rule set it ran under and drift between copies is visible. The stamp wording and the file list are settings at the top of the script. |
| `verify_branch.sh` | HR-008, "Verify before reporting done", and HR-013, "Delegated work needs a brief and a receipt" | The gate for a delegated-work branch: the branch must exist on origin, a reported commit SHA must match the origin head character for character, changed files are enumerated against the brief's allowed list, line endings and forbidden patterns are scanned, and dependency changes are flagged. The optional test step (tsc + vitest) is off by default; enable it with `--run-tests` or `VERIFY_BRANCH_RUN_TESTS=1`. |

## Running the gates in CI

`.github/workflows/validate.yml` runs the forbidden-pattern gate (self-test first, then a full scan) and the facts-freshness check on every push and pull request. The scripts have no dependencies beyond Python 3 and, for `verify_branch.sh`, git and bash.
