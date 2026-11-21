# Adapters: using Hard Memory with any tool, or none

The system is plain markdown and CSV files. Anything that can read files, or accept text at the start of a session, can use it. Nothing here is locked to one product.

## Muse

Keep the folder in your workspace. Muse reads the core files at session start and searches the rest on demand. Point it at the folder once and tell it the core files are standing context.

## ChatGPT

Create a Project and upload the core files plus the people and group indexes. Paste the operating rules from `core/AGENTS.md` into the project's instructions. Re-upload a file whenever you change it. For long registers, upload the CSV and ask for lookups by row.

## Gemini

Create a Gem and paste the core operating rules and persona into its instructions. Keep the full files in a Drive folder the Gem's knowledge can draw on, or paste the relevant page into the chat when a topic comes up.

## Coding agents (Antigravity, Cursor, Copilot, and similar)

Most coding agents already read a rules file at the repo root (`AGENTS.md`, `.cursorrules`, or similar). Copy `core/AGENTS.md` to that filename. The workflow-gates module was designed for this: handoff templates and completion contracts an implementer agent can follow and a reviewer can verify.

## Local and open models

Any local model with file access, or a retrieval setup pointed at the folder, works the same way. The files are small on purpose: the core set loads whole into modest context windows.

## No AI at all

The system still works as a personal knowledge base. The core files are a briefing document about your work, the people pages are a contact book with context, and the registers are plain spreadsheets. People ran versions of this in notebooks for centuries. The AI just makes it effortless to keep current.
