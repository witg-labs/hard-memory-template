# AGENTS.md

Standing instructions for any AI agent opening this repository.

- The memory system lives in `core/`, `people/`, `groups/`, and `registers/`. Treat `core/` as standing context for every session.
- The hard rules live in `rules/HARD_RULES.md`, indexed in `rules/RULE_INDEX.md`. Treat them as standing context too. They outrank convenience: when a rule and a shortcut disagree, follow the rule and report the disagreement.
- If the owner asks you to set the system up ("setup mode," "set this up," or similar), follow `SETUP_MODE.md` exactly.
- When the owner states a fact, preference, or correction, write it into the correct file in the same session, dated, in their words.
- Never invent content for these files. A blank placeholder is better than a plausible guess.
