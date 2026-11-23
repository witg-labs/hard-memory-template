#!/usr/bin/env python3
"""List stale facts in registers/FACTS.md.

A fact is stale when its Verified date is more than STALE_DAYS old or cannot
be parsed. Exit code 1 when any stale fact is found, so CI or a monthly sweep
can gate on it. Usage: python3 tools/check_facts_freshness.py [path]
"""
import re
import sys
from datetime import date
from pathlib import Path

STALE_DAYS = 60
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("registers/FACTS.md")
    today = date.today()
    stale = []
    checked = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "---" in line or "Verified" in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        checked += 1
        m = DATE_RE.search(cells[3])
        if not m:
            stale.append((cells[0], "no parseable Verified date"))
            continue
        verified = date.fromisoformat(m.group(0))
        age = (today - verified).days
        if age > STALE_DAYS:
            stale.append((cells[0], f"verified {verified.isoformat()}, {age} days old"))
    print(f"Checked {checked} facts in {path}")
    if stale:
        print(f"STALE ({len(stale)}):")
        for name, why in stale:
            print(f"  - {name}: {why}")
        return 1
    print("All facts fresh.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
