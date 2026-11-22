# Hard Memory Template

A modular, file-based memory system for working with AI assistants over months and years without starting over every session.

Built from the architecture behind [Written In The Genome](https://writteninthegenome.blog/)'s Hard Memory system, generalized so anyone can adopt it: a researcher, a writer, a developer, a small business owner, or anyone whose AI keeps forgetting what matters.

## The idea in one paragraph

Chat history is not memory. Hard Memory is a set of plain markdown files that hold what an assistant needs to know about you, your people, your rules, and your work. The files load at the start of every session, so the assistant opens the conversation already knowing. When something changes, the file changes, not just the chat. Corrections are written down once and never need to be repeated.

## What is in the box

| Piece | What it does |
|---|---|
| `core/` | The five core files: who you are, what is durably true, how the assistant should operate, its persona, and local tool notes. |
| `rules/` | The hard rules: a generalized standing rule set with stable IDs and an index, covering memory, evidence, verification, authority, and delegation. Adopt as is, then add your own domain rules under it. |
| `people/` and `groups/` | One page per person or group that matters, with an index. Facts and relationships, stated by you, never guessed. |
| `registers/` | Structured tables (CSV) for anything you will look up twice: assets, inventory, contacts, content, accounts. Recall becomes a lookup, not a re-audit. |
| `modules/` | Optional rule packs you adopt or delete: workflow gates for delegated work, evidence standards for research, voice rules for writing, and more. |
| `USE_CASE.md` | A real use case, scrubbed of names and private details: how this system runs two long projects at once, and how to map it to your own work. |
| `SETUP.md` | The interview. Answer the questions and your core files are drafted. |
| `ADAPTERS.md` | How to point different AI tools at these files: Muse, ChatGPT, Gemini, coding agents, or no AI at all. |

## The five rules that make it work

1. **Durable facts only in the core memory.** Day-to-day detail lives in dated logs and case files. The core file stays small enough to load whole, every time.
2. **Write it down when it is said.** A fact, preference, or correction is saved the moment it is learned, with its date and source.
3. **Registers for repeat lookups.** If a question will be asked twice, it gets a table, not a memory.
4. **Rules are versioned.** Standing rules live in one place and get pinned to version tags, so updates are deliberate, never drift.
5. **Nothing personal is ever published from your private copy.** This template is the architecture. Your filled-in copy is yours alone.

## Quick start

1. Copy this repo (or use it as a template) into a private repo or a local folder of your own.
2. Open it with your AI assistant and say: **"Run setup mode."** The repo ships with `SETUP_MODE.md`, a protocol your agent follows to interview you and fill in every file from your answers. No manual editing required.
3. Prefer to do it by hand? Work through `SETUP.md` and fill in `core/` yourself. Read `USE_CASE.md` first to see how the finished system behaves in real use.
4. Point your AI tool at the folder using `ADAPTERS.md`.
5. Adopt only the `modules/` you need. The rest stay dormant.

## License

MIT. Use it, adapt it, build on it. A credit line back to Written In The Genome is appreciated, not required.
