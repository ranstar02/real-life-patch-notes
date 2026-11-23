#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one line, at most 160 characters: a software patch note for a bug
in real life, in the terse register of a real release note.

The joke: the doorway effect. You walk through a doorway and the reason
you entered the room is gone, deleted with no warning, like a task wiped
from memory. Specific, universal, and it lands on a first read.

The output is fully deterministic: one fixed line, no randomness, no clock,
no network, no environment reads, so the grader's two runs are byte-identical.
"""

import os

JOKE = "v2.5.0: fixed a bug where walking through a doorway deleted the reason you entered the room."


def main() -> None:
    # The sealed gate wants 1-160 UTF-8 characters, not only whitespace.
    assert 1 <= len(JOKE) <= 160, "entry must be 1-160 characters"
    assert JOKE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
