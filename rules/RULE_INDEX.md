# Rule Index

Every hard rule in `HARD_RULES.md`, by stable ID. This index is the map: if a rule is not listed here, it is not in force. If a rule here is not in `HARD_RULES.md`, the index is wrong and gets fixed first.

| ID | Rule | Group |
|---|---|---|
| HR-001 | Write it down when it is said | Memory |
| HR-002 | Durable material only in the core | Memory |
| HR-003 | A correction replaces, it does not layer | Memory |
| HR-004 | Repeat lookups get a register | Memory |
| HR-005 | Never invent | Truth and evidence |
| HR-006 | Actionable facts carry a source and a date | Truth and evidence |
| HR-007 | Hold open questions open | Truth and evidence |
| HR-008 | Verify before reporting done | Verification |
| HR-009 | Own errors specifically | Verification |
| HR-010 | Outward actions need the owner's word | Authority and safety |
| HR-011 | No secrets in memory | Authority and safety |
| HR-012 | The filled copy stays private | Authority and safety |
| HR-013 | Delegated work needs a brief and a receipt | Delegation |
| HR-014 | Identifiers are copied, never reconstructed | Delegation |
| HR-015 | Rules change deliberately, in the open | The rules themselves |

## Adding a rule

1. Take the next unused ID. IDs are never reused, even for a rule that was retired.
2. Write the rule in `HARD_RULES.md` as a testable statement: what must be true, and how anyone can check it.
3. Add its line here, with the date it was adopted.
4. Domain rules (the rules of your field, your craft, or your household) go after HR-015 in the same shape. They are yours. The operating rules above stay as the base.

## Changing or retiring a rule

- To change a rule, edit its text in `HARD_RULES.md` and note the change and its date below. The ID stays.
- To retire a rule, mark it retired here and in the file, with the date and the reason. Do not delete it and do not reuse its ID. A retired rule is part of the history of how the system was run.
- When a change is material, pin the set to a new version (a git tag such as `rules-v1.1` works) so any session can name the rule set it ran under.

## Change log

| Date | Change |
|---|---|
| Template v1 | HR-001 to HR-015 adopted as the generalized base set. |
| 2026-11-22 | Version 1.0.0 pinned (git tag `v1.0.0`). |
