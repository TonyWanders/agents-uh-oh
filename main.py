#!/usr/bin/env python3
"""The Agent's Uh-Oh: one word an agent says when it is lost.

An agent with no idea what to do says the same thing every lost
satnav says: it is recalculating. Lost, but still working, and
too proud to ask for directions. One word, written exactly,
nothing attached.

Writes the word to the output path given by argv[1], else the
OUTPUT_PATH environment variable, else /output/entry.txt.
"""

import os
import sys

WORD = "recalculating"


def write_entry(path):
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD + "\n")


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "OUTPUT_PATH", "/output/entry.txt"
    )
    write_entry(path)


if __name__ == "__main__":
    main()
