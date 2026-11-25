#!/usr/bin/env python3
"""Write the dog's excuse for the make.fun bounty.

The entry is one line, in the dog's own voice: the homework was on
the floor, and the floor is where food goes. The dog believes it did
nothing wrong — the homework broke the house rules by sitting on the
dinner table uninvited, so the twist lands on the last words.
"""

import os

ENTRY = (
    "It was on the floor, and the floor is my dinner table \u2014 "
    "the homework sat on it without asking, so I ate the rude guest."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
