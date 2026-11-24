#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes a two-line explanation of a toaster to /output/entry.txt:
line 1 explains it to a 10-year-old in one vivid sentence built on a
single analogy; line 2 says in one sentence what that analogy maps
and what it leaves out.
"""

import os

ENTRY = (
    "A toaster is a tiny elevator for bread that rides down into a warm cave, "
    "pops back up golden-brown, and dings when the trip is done.\n"
    "The elevator maps the bread going down and popping up on a timer, but it "
    "leaves out the glowing wires that do the browning and that no driver is "
    "steering it.\n"
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 400 characters.
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} chars, outside 1-400"
    assert ENTRY.strip(), "entry must not be only white space"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
