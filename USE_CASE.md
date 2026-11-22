# Use Case: A Long Project That Outlasts Any Chat

This template was not designed in theory. It was extracted from a working system that runs two long projects at once for one person: a family history research archive built from primary records, and a software product built and maintained with the help of several AI agents.

Names, people, and private details have been removed. What is left is the shape of the work, because the shape is what transfers.

## The problem

Both projects run for months. Both involve facts that cannot be guessed: names and dates in historical records on one side, version numbers, identifiers, and build states on the other. Both involve many people, some living collaborators, some research subjects who died a century ago. And both are worked on in short bursts, across different AI tools, with weeks sometimes passing between sessions on the same thread.

Chat history failed at this in predictable ways:

- The assistant re-asked questions that had been answered months earlier.
- A correction made in one session was lost in the next, and the same mistake had to be fixed twice.
- Work delegated to another agent came back described as done when it had only been attempted.
- A fact that had changed kept being quoted in its old form, because nothing marked the old form as replaced.

None of that is a model problem. It is a storage problem. The answers existed, but they lived in old chats that no session could reliably find again.

## The setup

The owner moved the answers into plain files that load at the start of every session:

- **Core files.** Who the owner is, how the assistant should work, how it should sound, and what is durably true. Five files, kept small on purpose.
- **People pages.** One page per person the work touches, with an index. Each page records only what the owner stated or what a cited record shows, never a guessed relationship.
- **Registers.** Structured tables for anything looked up twice: facts that need re-checking on a schedule, records pulled, items tracked across sessions. A lookup became a table read, not a fresh audit.
- **Rules with an index and a version.** Standing rules live in one place, each with a stable ID, and the set is pinned to a version tag. When a rule changes, the change is reviewed and recorded, and the version makes it possible to name exactly which rule set a session ran under.
- **Case files.** A live matter with day-to-day detail gets its own file. The core memory keeps only the current state and a pointer. When the matter closes, its file is archived whole.

One rule governs the size of the core: durable material only, under a set budget. When the core file hit its budget, the fix was not a bigger file. Detail moved out to case files, and the core shrank back down with nothing deleted.

## A normal week in the system

**Remembering.** A new fact is stated in conversation on Monday. It is written into the right file the same session, with its source and date, before the conversation moves on. On Friday, in a new session, the assistant opens already knowing it.

**Correcting.** The owner narrows a rule that the assistant had recorded too broadly. The file is edited to the owner's exact words that day, not a wider version of them. The old wording does not survive anywhere as the current rule, so it is never applied again by accident.

**Looking up.** A question comes back that was answered before: what is the current state of a tracked item, what did a record actually say, which version is live. The assistant reads the register or the cited file and answers from it, instead of reconstructing an answer from memory of a memory.

**Delegating.** Work is handed to a second agent with a written brief: what done means, what to check, and what evidence to bring back. The returning report is verified against the actual files and the live state before anyone calls it done. A summary is treated as a claim, not as proof.

## The moment it proved itself

Two small events, not one big one.

First, a key product identifier turned out to be stale in an older project profile. It was corrected once in the facts register, with the old value recorded as superseded. Every later session used the corrected value. Nobody had to catch the stale one again, because the file, not the chat, was now the source.

Second, the owner ran a deliberate improvement pass over the whole memory system: an audit list of 19 items covering stale copies, dead links, secret scanning, lifespan rules, and proof standards. Each item was worked, checked, and closed on evidence, and the list ended at 19 of 19. A memory system that can be audited like that is a system you can trust when it matters, because its state is written down where anyone can inspect it.

## What changed

- Corrections are made once. The repeated fix, the repeated explanation, and the repeated question mostly stopped.
- Sessions start warm. The first ten minutes of re-briefing disappeared.
- Delegated work comes back checkable. Done means verified against files and live state, with a receipt, not just reported.
- Uncertainty stays visible. Where a record cannot decide between two possibilities, the file says so and waits. The system holds an open question open instead of filling it with a plausible answer.

## Make it yours

The projects above are specific. The mapping is not:

| In this use case | In your work it might be |
|---|---|
| A research archive | A business, a degree, a book, a home renovation, a job search |
| People pages for research subjects and collaborators | Clients, patients in your care notes (with permission), students, family members, team members |
| A facts register | Prices, dates, account states, specifications, anything you will re-check |
| Versioned standing rules | Your editorial standards, your shop procedures, your household agreements |
| Workflow gates for delegated agents | Checklists for an assistant, an employee, a contractor, or a second AI tool |
| A case file for a live matter | Any single matter that is active now and will close later |

Start with the core files and one register. Add people pages when you notice yourself explaining the same person for the third time. Add a rule when you correct the same behavior for the second time. The system grows at the exact points where forgetting costs you something.

## Limits, stated plainly

- It does not store itself. Someone, you or your assistant, has to write the fact down when it is said. The habit is the system.
- It is not a place for secrets. Passwords, ID numbers, and other people's private details do not belong in these files.
- It needs a short review now and then. Facts change, and a file that is never pruned becomes the same problem as a chat that is never cleared.
- It will not make a bad source good. It records what your evidence supports and marks what it does not. That honesty is a feature, not a gap.

Upkeep in this case runs to a few minutes in the session where something changes, plus a periodic review. In exchange, the work stopped depending on any single chat, tool, or session remembering everything.
