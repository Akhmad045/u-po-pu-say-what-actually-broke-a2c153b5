#!/usr/bin/env python3
"""Emit a single line of error copy that says what actually broke.

The line is written to /output/entry.txt. It names the failure plainly
(the server crashed while doing its one job), owns up to it with a joke
a reader can repeat, and fits in one dialog line of at most 200
characters. This program checks the line before writing it and checks
the file again after writing it, so what the judge reads is exactly
the line below and nothing else.
"""

import sys
from pathlib import Path

ENTRY_LINE = (
    "The server crashed doing the only job it has. "
    "It is rebooting now and thinking very hard about its choices."
)

DESTINATION = Path("/output/entry.txt")
CHAR_LIMIT = 200


def find_problems(line: str) -> list[str]:
    """Return every way the line breaks the entry rules, or [] if it is fine."""
    problems = []
    if not line.strip():
        problems.append("line is blank")
    if len(line) > CHAR_LIMIT:
        problems.append(f"line is {len(line)} characters, over the {CHAR_LIMIT} limit")
    if line != line.strip():
        problems.append("line has leading or trailing whitespace")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        problems.append("line contains a control character")
    if "\n" in line or "\r" in line:
        problems.append("line spans more than one line")
    try:
        if line.encode("utf-8").decode("utf-8") != line:
            problems.append("line does not survive a UTF-8 round-trip")
    except UnicodeError:
        problems.append("line is not valid UTF-8 text")
    return problems


def run() -> int:
    problems = find_problems(ENTRY_LINE)
    if problems:
        for problem in problems:
            print(f"invalid entry: {problem}", file=sys.stderr)
        return 1

    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(ENTRY_LINE + "\n", encoding="utf-8")

    # Confirm the file on disk is byte-for-byte the line plus one newline.
    if DESTINATION.read_bytes() != (ENTRY_LINE + "\n").encode("utf-8"):
        print("invalid entry: file on disk differs from the entry line",
              file=sys.stderr)
        return 1

    print(f"wrote {len(ENTRY_LINE)} characters to {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
