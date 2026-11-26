#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message to /output/entry.txt: the note an AI agent
would leave in the log after a long night of chasing down and fixing
its own bugs. One line, at most 200 characters, funny first and true
to the machine voice second.

The joke is the loop itself: every fix in the chain was written by
the same agent, at midnight, 2am and 3am, so by 4am the only bug left
to confess to is the author.
"""

import os
from pathlib import Path

# One line, written as typed into a commit box at four in the morning.
MESSAGE = (
    "fix: the bug was my 3am fix for my 2am fix for my midnight bug. "
    "I wrote all of them. I am the bug. "
    "Merging anyway — I no longer trust my own review."
)

MAX_CHARS = 200


def build_message() -> str:
    """Return the single-line commit message, checked against the gate."""
    text = MESSAGE.strip()
    if not text:
        raise SystemExit("entry is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be one line")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the 200 limit")
    return text


def main() -> None:
    text = build_message()
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the message, nothing else.
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
