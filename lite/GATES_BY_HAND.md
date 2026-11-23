# Gates by hand

The full edition of this template runs its checks with scripts. Lite has no scripts, so the same checks are done by hand, by the assistant, on this checklist. Short and practical: run them at the moments named, and report what was found.

## 1. The forbidden-pattern check (supports HR-011)

Run before anything from this folder is shared, and whenever a file is pasted in from outside. Read or search the files for:

- **Credential-shaped strings:** text that looks like an AWS access key (starts with AKIA), a GitHub token (starts with ghp_, gho_, or a similar prefix), an API key starting with sk-, or any line where a word like password, secret, api key, or token is followed by an equals sign or a colon and an actual value.
- **A private key block:** the words BEGIN PRIVATE KEY, in any file.
- **Forbidden file types sitting in the folder:** database dumps and key files, ending in .sql, .dump, .pem, .key, or .p12.
- **Raw data files that do not belong in memory:** a data file whose first lines carry a genotype header (a line starting with "# rsid", a column header starting with "rsid" and "chromosome", or a VCF marker, "##fileformat=VCF").

Report each finding as file, line, and category only. Never repeat the value itself in the report; a report that echoes a secret is its own leak. A clean pass is reported as clean.

## 2. The facts-freshness habit (supports HR-006)

- Open `registers/FACTS.md`. Read the Verified column, the fourth column.
- Any fact verified more than 60 days ago is stale. Re-verify it against its source, then update the row and the Verified date. If it changed, record what it replaced in the Detail column.
- Run this pass when a fact is about to be acted on, and once in a while over the whole register, so staleness is found before it matters.

## 3. Verify before reporting done (supports HR-008 and HR-013)

The full edition checks delegated work against a branch. Lite's version:

- After any edit, reopen the file in Drive and read it back as saved. Confirm the change is present, the rest of the file is intact, and Drive shows a fresh modified time.
- For work done by another person, tool, or agent: the brief was written down first, and the result is accepted only after the evidence the brief named has been read against the files themselves. A confident summary is not a receipt.
- Keep a change note: a dated line in the file you changed, or in the change log in `rules/RULE_INDEX.md` for rule changes, saying what changed and why.
- If an edit goes wrong, Drive's Version history holds the previous version of the file. Restore from there, and record the error and the fix in the file, dated (HR-009).
