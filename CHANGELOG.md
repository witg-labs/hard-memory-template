# Changelog

All notable changes to the Hard Memory Template. Versions are pinned with git tags.

## [1.0.0] - 2026-11-22

First tagged release.

- Core file set in `core/`: `AGENTS.md`, `MEMORY.md`, `SOUL.md`, `TOOLS.md`, `USER.md`.
- Generalized hard rules HR-001 to HR-015 in `rules/`, with the rule index.
- People and group pages: one page per person or group, with indexes.
- Registers in `registers/`: a CSV register template and the FACTS register (`registers/FACTS.md`).
- Modules in `modules/`: workflow gates (handoff template and completion contract) and evidence standards.
- `USE_CASE.md`: a real use case, scrubbed of names and private details.
- Setup and adoption files: `SETUP.md`, `SETUP_MODE.md`, `ADAPTERS.md`.
- Enforcement tools in `tools/`: `check_facts_freshness.py`, `check_forbidden_patterns.py`, `render_trigger_files.py`, `verify_branch.sh`, each mapped to the rule it enforces in `tools/README.md`.
- CI workflow (`.github/workflows/validate.yml`) running the forbidden-pattern gate and the facts-freshness check on push and pull request.
