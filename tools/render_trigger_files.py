#!/usr/bin/env python3
"""Stamp the trigger files with the pinned Hard Memory rules version.

Trigger files are the files that carry standing guidance for an AI tool
(AGENTS.md, CLAUDE.md, .github/muse-instructions.md, and similar). They are
often hand-maintained copies of overlapping guidance, and copies drift. This
script writes a single version stamp line into each trigger file so any
reader (human or agent) can tell at a glance which rules version the file
belongs to, and CI can fail when a stamp does not match the pinned version.

Usage: python3 tools/render_trigger_files.py rules-v1.0
Run from the repository root. Idempotent: re-running replaces the stamp.
Configure the stamp and the file list in the SETTINGS block below.
"""
import re
import sys
from pathlib import Path

# --- SETTINGS ---------------------------------------------------------------
# The stamp line written into each trigger file. {version} is replaced with
# the version argument, e.g. "rules-v1.0".
STAMP_TEMPLATE = "<!-- hard-memory: {version} -->"
# What a valid version string looks like.
VERSION_RE = re.compile(r"rules-v\d+\.\d+")
# The pattern that finds an existing stamp, so re-running replaces it
# instead of stacking stamps.
STAMP_RE = re.compile(r"<!-- hard-memory: rules-v\d+\.\d+ -->")
# The trigger files to stamp, relative to the repository root. Add every
# file that carries standing guidance for an AI tool in your setup
# (for example "CLAUDE.md" or ".github/muse-instructions.md").
FILES = ["AGENTS.md"]
# ----------------------------------------------------------------------------


def stamp(path: Path, version: str) -> None:
    text = path.read_text(encoding="utf-8")
    line = STAMP_TEMPLATE.format(version=version)
    if STAMP_RE.search(text):
        text = STAMP_RE.sub(line, text, count=1)
    else:
        lines = text.splitlines(keepends=True)
        lines.insert(1 if lines else 0, line + "\n")
        text = "".join(lines)
    path.write_text(text, encoding="utf-8")
    print(f"stamped {path} -> {version}")


def main() -> int:
    if len(sys.argv) != 2 or not VERSION_RE.fullmatch(sys.argv[1]):
        print(__doc__)
        return 2
    for rel in FILES:
        p = Path(rel)
        if p.exists():
            stamp(p, sys.argv[1])
        else:
            print(f"skip (missing): {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
