#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — entry program.

Writes a single roast line (at most 200 characters) to the entry output
file. Standard library only.
"""

import os
import sys

ENTRY_TEXT = "Since the firmware update, my fridge needs a password \u2014 I now negotiate with my own leftovers for a snack."


def resolve_output_path():
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    text = ENTRY_TEXT
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry length %d outside 1-200 characters" % len(text))
    if not text.strip():
        raise SystemExit("entry is blank")
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("written output does not match entry text")
    return 0


if __name__ == "__main__":
    sys.exit(main())
