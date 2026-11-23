#!/usr/bin/env python3
"""Forbidden-pattern gate for a Hard Memory repository.

Scans a directory tree and fails (exit 1) if it finds anything that must
never be committed here:

  * credential-shaped strings: AWS access keys, GitHub tokens, sk- API
    keys, private-key blocks, generic api_key / password assignments
    that carry a value;
  * dump / key files by extension: .sql, .dump, .pem, .key, .p12;
  * raw genotype data signatures: a data file whose header lines carry
    a "# rsid" comment header, an "rsid<TAB>chromosome" column header,
    or a VCF "##fileformat=VCF" marker.

Findings are reported as file + line number + pattern CATEGORY only.
Matched values are never printed: a gate that echoes secrets into logs
would be worse than no gate.

This file is the single source for the forbidden-pattern list.
verify_branch.sh (in this same tools/ folder) and the CI workflow
(.github/workflows/validate.yml) share this list BY REFERENCE to this
file: when a pattern is added or changed, change it here.

Usage:
    python3 tools/check_forbidden_patterns.py [ROOT]
    python3 tools/check_forbidden_patterns.py --self-test

Exit codes: 0 clean, 1 findings, 2 usage error.
"""

import os
import re
import sys
import tempfile

# --- The pattern list (single source; see header note) ---------------------

CREDENTIAL_PATTERNS = [
    ("aws-access-key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("github-token", re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}")),
    ("api-key-sk", re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}")),
    (
        "private-key-block",
        re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----"),
    ),
    (
        "generic-credential-assignment",
        re.compile(
            r"(?i)\b(?:api[_-]?key|apikey|password|passwd|secret|access[_-]?token|auth[_-]?token)\b"
            r"\s*[:=]\s*[\"']?[^\s\"']{8,}"
        ),
    ),
]

FORBIDDEN_EXTENSIONS = {".sql", ".dump", ".pem", ".key", ".p12"}

GENOTYPE_HEADER_LINES = 50  # header signatures live at the top of data files


def is_genotype_header(lines):
    """True if the first lines of a file carry a raw genotype signature."""
    for line in lines[:GENOTYPE_HEADER_LINES]:
        if line.startswith("# rsid"):
            return True
        if line.startswith("rsid\tchromosome"):
            return True
        if line.startswith("##fileformat=VCF"):
            return True
    return False


def scan(root):
    """Return a list of (relpath, lineno, category) findings under root."""
    findings = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for name in sorted(filenames):
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, root)
            ext = os.path.splitext(name)[1].lower()
            if ext in FORBIDDEN_EXTENSIONS:
                findings.append((rel, 0, "forbidden-file-extension:" + ext))
                continue
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                    lines = fh.readlines()
            except OSError:
                continue
            if is_genotype_header(lines):
                findings.append((rel, 1, "raw-genotype-data"))
            for lineno, line in enumerate(lines, start=1):
                for category, pattern in CREDENTIAL_PATTERNS:
                    if pattern.search(line):
                        findings.append((rel, lineno, category))
    return findings


def run(root):
    if not os.path.isdir(root):
        print(f"error: not a directory: {root}")
        return 2
    findings = scan(root)
    if not findings:
        print(f"OK: no forbidden patterns found under {root}")
        return 0
    print(f"FORBIDDEN PATTERNS: {len(findings)} finding(s) under {root}")
    for rel, lineno, category in findings:
        where = f"{rel}:{lineno}" if lineno else rel
        print(f"  {where}  [{category}]")
    return 1


def self_test():
    failures = []
    with tempfile.TemporaryDirectory() as td:
        bad = os.path.join(td, "bad.txt")
        with open(bad, "w", encoding="utf-8") as fh:
            # Dummy credential-shaped string, built at runtime so this
            # script's own source never contains a matching literal.
            fh.write("dummy = " + "AKIA" + "Q" * 16 + "\n")
        clean = os.path.join(td, "clean.md")
        with open(clean, "w", encoding="utf-8") as fh:
            fh.write("# Notes\n\nNothing sensitive in this file.\n")
        findings = scan(td)
        if not any(rel.endswith("bad.txt") for rel, _, _ in findings):
            failures.append("dummy credential-shaped string was NOT caught")
        if any(rel.endswith("clean.md") for rel, _, _ in findings):
            failures.append("clean file was incorrectly flagged")
    if failures:
        for failure in failures:
            print("SELF-TEST FAIL:", failure)
        return 1
    print("SELF-TEST PASS: dummy credential caught, clean file passed.")
    return 0


def main(argv):
    args = [a for a in argv[1:] if a != "--self-test"]
    if "--self-test" in argv[1:]:
        return self_test()
    root = args[0] if args else "."
    return run(root)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
