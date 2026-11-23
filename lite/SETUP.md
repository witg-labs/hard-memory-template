# Setup: Hard Memory Lite in Google Drive

Four steps: get the folder, put it in Drive, give your assistant access, then run the setup interview.

## 1. Get the lite folder

Download or copy the `lite` folder from the Hard Memory template. Keep its structure exactly as it is: `core/`, `rules/`, `registers/`, `people/`, and `groups/` inside one folder, with `README.md`, `SETUP.md`, and `GATES_BY_HAND.md` at the top.

## 2. Put it in your Google Drive

1. In Google Drive, create a new folder. The suggested name is **Hard Memory**.
2. Upload the whole lite folder's contents into it, so `core/`, `rules/`, `registers/`, `people/`, and `groups/` sit inside your Hard Memory folder.
3. Keep the files as plain markdown (`.md`) and CSV files, uploaded as they are. Do not convert them to Google Docs format; your assistant needs to read and edit the same text you see.
4. This folder is private. The template is public, but your filled-in copy holds your facts, and it is never shared or published (that is HR-012).

## 3. Give your assistant access

Pick whichever route your AI tool supports:

- **Upload at session start.** At the start of each session, upload or paste the five files in `core/` plus `rules/HARD_RULES.md`. That is the standing context the assistant works from. Add a person page, group page, or register whenever the conversation touches it.
- **Connect the agent to Drive.** Where your assistant or agent tool can connect to Google Drive directly, point it at your Hard Memory folder and tell it to load `core/` and `rules/` first, every session, and to write changes back into the same files.
- Either way, the habit is the same: the assistant opens each session by reading the core files and the rules, and it writes new facts, preferences, and corrections into the files during the session, not after it.

## 4. Run the setup interview

Tell your assistant: **"Run setup mode."** In Lite, that means the following, restated for Drive:

- The assistant works through the interview one topic at a time, in your words, and never fills a file with invented or example content.
- **About you** goes to `core/USER.md`: your name, what to call you, where you are based, your timezone, what you do, and what matters most right now.
- **How the assistant should work** goes to `core/AGENTS.md`: how literal it should be, what it must check before reporting done, what it must never do without asking, and how mistakes get handled.
- **Voice and persona** goes to `core/SOUL.md`: how it should sound, and words it should never use when writing for you.
- **Memory habits** goes to `core/MEMORY.md`: what is worth keeping permanently, what should never be stored, and anything sensitive that needs special handling.
- **Your world:** one page per person in `people/` and per group in `groups/`, each listed in its `INDEX.md`, and one register per thing you will look up more than once, created in `registers/` from `register-template.csv` and pointed to from `core/MEMORY.md`.
- **The rules:** the assistant walks you through `rules/HARD_RULES.md` briefly. Adopt the set as is, edit a rule in your own words, or retire one, and record the outcome in `rules/RULE_INDEX.md`.
- When the interview is done, name your first version in the change log in `rules/RULE_INDEX.md` (rules v1.0, with the date). Drive version history holds the blank template underneath, so nothing is lost.

## After setup

- Every session starts with the assistant loading `core/` and `rules/`.
- New facts are written into the files the session they are learned (HR-001).
- The checks in `GATES_BY_HAND.md` are run by hand: a secrets scan before anything is shared, a freshness pass over the FACTS register, and a read-back after every edit.
