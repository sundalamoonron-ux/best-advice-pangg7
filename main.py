#!/usr/bin/env python3
"""The Best Advice I Ever Got — entry program.

Writes one sentence (the best advice the writer ever received) to
/output/entry.txt. Gate: UTF-8 text, 1-200 characters, exactly one
sentence, not only whitespace. The entry is validated before anything
is written; an invalid entry fails loudly instead of producing a
bad output file.
"""

import os
import sys

ENTRY = "My father told me, 'Never borrow money to look rich,' and twenty years later I still check my bank balance before my ego."

OUTPUT_PATH = "/output/entry.txt"

MIN_LENGTH = 1
MAX_LENGTH = 200


def validate(entry: str) -> None:
    """Check the entry against the competition gate; exit on failure."""
    if not entry.strip():
        sys.exit("error: entry is empty or only whitespace")

    if not (MIN_LENGTH <= len(entry) <= MAX_LENGTH):
        sys.exit(
            f"error: entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(entry)}"
        )

    stripped = entry.strip()
    # Exactly one sentence: one final period, and no other sentence
    # terminator anywhere in the text (a comma inside quotes, as in
    # '...to look rich,' is fine — only . ! ? count as terminators).
    terminators = sum(stripped.count(mark) for mark in (".", "!", "?"))
    if terminators != 1:
        sys.exit(
            f"error: entry must be exactly one sentence, "
            f"found {terminators} sentence terminators"
        )
    if not stripped.endswith("."):
        sys.exit("error: entry must end with a single final period")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
