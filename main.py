#!/usr/bin/env python3
"""The Best Advice I Ever Got — entry program.

Writes one sentence (the best advice the writer ever received) to
/output/entry.txt. Gate: UTF-8 text, 1-200 characters, not only whitespace.
"""

import os

ENTRY = "My father told me, 'Never borrow money to look rich,' and twenty years later I still check my bank balance before my ego."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
