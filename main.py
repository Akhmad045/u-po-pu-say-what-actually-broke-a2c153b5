#!/usr/bin/env python3
"""Write one brutally honest, funny error message to /output/entry.txt.

The message names the real failure (the server crashed) instead of
hiding behind a generic apology, and it stays inside the 200-character
limit for a single line of error copy.
"""

import os
import sys

LINE = (
    "The server crashed doing the only job it has. "
    "It is rebooting now and thinking very hard about its choices."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    text = LINE
    if not text or not text.strip():
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"error: entry line is {len(text)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if text != text.strip():
        print("error: entry line has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")

    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text + "\n":
        print("error: written file does not match the entry line", file=sys.stderr)
        return 1

    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
