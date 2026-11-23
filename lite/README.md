# Hard Memory, Lite Edition

The same memory system as the full Hard Memory template, set up to run from a single Google Drive folder. No GitHub account, no Git, no code, nothing to install.

## Who it is for

- You do not use GitHub and do not want to start.
- Your files already live in Google Drive, and you want your AI assistant to work from them there.
- You want the memory discipline (core files, hard rules, registers) without the tooling.

## What is in this folder

| Piece | What it does |
|---|---|
| `core/` | The five core files: who you are, what is durably true, how the assistant should operate, its persona, and local tool notes. |
| `rules/` | The hard rules (HR-001 to HR-015) and their index. The same rule set as the full edition. |
| `registers/` | Structured tables for anything you will look up twice, including the FACTS register. |
| `people/` and `groups/` | One page per person or group that matters, with an index. |
| `SETUP.md` | How to put this folder in Drive, give your assistant access, and run the setup interview. |
| `GATES_BY_HAND.md` | The checks the full edition runs with scripts, restated as short manual habits. |

## How Lite differs from the full edition

- **Storage.** The full edition lives in a Git repository. Lite lives in one Drive folder. Drive keeps the previous version of every file under Version history, which is Lite's undo and its version record.
- **No scripts, no CI.** The full edition ships checker scripts and an automatic gate. Lite ships none. The same checks are done by hand, by the assistant, following `GATES_BY_HAND.md`.
- **Versioning.** The full edition pins rule versions with tags. Lite names each version in the change log in `rules/RULE_INDEX.md`, with its date.
- **Everything else is the same.** Same core files, same rules, same registers, same standard: write it down when it is said, correct it in the file, verify before reporting done.

## Moving up later

If you outgrow Lite, nothing is thrown away. The full edition uses these same files. Moving up means copying this folder into a repository and adopting the scripts; the memory itself does not change.
