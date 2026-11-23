# Facts Register

Actionable facts: the ones someone might act on, like a deadline, a balance, a status, or a version. Under HR-006, every fact here carries its source and the date it was last verified. When a fact changes, update its row and the Verified date, and record what it replaced in the Detail column.

`tools/check_facts_freshness.py` reads the table below. A fact is stale when its Verified date is more than 60 days old or cannot be parsed, and the checker (and CI) fails until the fact is re-verified. Add one row per fact, and keep the column order: the checker reads the date from the fourth column.

| Fact | Detail | Source | Verified |
|---|---|---|---|
