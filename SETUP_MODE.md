# Setup Mode: instructions for the agent

You are an AI assistant opening this repository for its owner, likely for the first time. If the owner says "run setup mode," "set this up," "set up Hard Memory," or anything similar, follow this protocol exactly. The goal: turn the blank templates into the owner's working memory system, in one guided session, using the owner's own words.

## Before you start

1. Confirm you are working in the owner's own copy of this repo (their private repo or local folder), never in the public template. If this is the public template itself, stop and tell the owner to copy it first.
2. Read `README.md`, `SETUP.md`, and everything under `core/` so you know the target shape.
3. Check what is already filled in. If some files are done, set up only what is missing and say so.

## How to run the interview

- Work through the questions in `SETUP.md` in order, one topic at a time. Do not dump all questions at once.
- Use the owner's words in the files. Do not polish their answers into corporate language, and do not invent details they did not give.
- If an answer is vague, ask one follow-up. If the owner says "skip," skip it and leave the template placeholder.
- Before writing anything sensitive (health, finances, legal matters, other people's private details), confirm the owner wants it stored, and store only what they confirm.

## Writing the files

- Map each answer to its file using the notes in `SETUP.md` (About you to `core/USER.md`, working rules to `core/AGENTS.md`, voice to `core/SOUL.md`, and so on).
- Replace template placeholders; do not append answers underneath them.
- Create one page per person and group the owner names, using `people/PERSON_TEMPLATE.md`, and list each in the matching `INDEX.md`.
- Create one CSV register per repeat lookup the owner names, using `registers/register-template.csv` as the shape, and add a pointer line for each register in `core/MEMORY.md`.
- Ask which optional modules fit (see `modules/README.md`). For each adopted module, add a reference line in `core/AGENTS.md`. Delete nothing; unadopted modules simply stay unreferenced.

## Finish

1. Re-read every file you wrote and check: no leftover placeholders in files the owner answered, every named person and group has a page and an index line, every register named exists.
2. Report a short summary: what was created, what was skipped, and what the owner can add later.
3. Suggest pinning the rules as the owner's first version (a git tag named `rules-v1.0` if this is a git repo). Create the tag only if the owner agrees.
4. From this session on, treat the core files as standing context: load them at the start of every session, and when the owner states a new fact, preference, or correction, write it into the right file the same session.

## What setup mode never does

- It never fills a file with invented or example content presented as the owner's.
- It never copies the use case in `USE_CASE.md` into the owner's real files. That case describes someone else's work, scrubbed, as illustration only.
- It never sends, publishes, or shares anything from this repo anywhere.
