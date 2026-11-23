# Facts Register

Actionable facts: the ones someone might act on, like a deadline, a balance, a status, or a version. Under HR-006, every fact here carries its source and the date it was last verified. When a fact changes, update its row and the Verified date, and record what it replaced in the Detail column.

A fact is stale when its Verified date is more than 60 days old. In Lite there is no checker script: the freshness pass is done by hand, by reading the dates in the fourth column and re-verifying anything stale (see `GATES_BY_HAND.md` in the top level of this folder). Add one row per fact, and keep the column order: Fact, Detail, Source, Verified.

| Fact | Detail | Source | Verified |
|---|---|---|---|
