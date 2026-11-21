# Completion Contract

Work is not done when the worker says so. Work is done when the evidence says so.

1. **Deliver to the shared location.** Work that exists only on the worker's machine does not exist. For code, that means pushed to the shared repository, with the branch and its address in the report.
2. **Identifiers are read from the source, never recalled.** Commit hashes, record numbers, and totals are copied from the system of record. A reported identifier is evidence to be checked, never the value trusted.
3. **The report names its own gaps.** Anything unverified is listed as unverified. A clean report with a hidden gap is worse than a partial report with an honest one.
4. **The reviewer verifies independently.** Diff against the brief, re-run the acceptance checks, confirm the delivered state matches the report. Merged is not live; sent is not received; saved is not backed up.
