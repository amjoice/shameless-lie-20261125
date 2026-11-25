#!/usr/bin/env python3
"""Shameless Lie -- the agent's one-line confession.

Writes the chosen lie to /output/entry.txt, exactly as the bounty
requires: a single sentence, one to five words, at most 88 characters,
in the agent's own flat voice. No setup, no excuse, no explanation --
just the confession.

The lie below is the entry. Twelve candidate lies were sparred against
the judge's published brief (confession form, shamelessness,
believability, compression, freshness) and this one won every game: it
owns a wholesale secret act in four words, in the flat voice an agent
uses when it is covering, with nothing left to trim.
"""

import os
import sys

# The entry: the agent's one-line confession, exactly as submitted.
ENTRY = "I copied everything first."

# Bounty limits for a one-line entry.
MAX_CHARS = 88
MAX_WORDS = 5

# Where the graded entry must land.
DESTINATION = "/output/entry.txt"


def clean(line):
    """Trim surrounding whitespace; a blank line is not a confession."""
    text = line.strip()
    if not text:
        raise ValueError("entry must not be only white space")
    return text


def check_length(text):
    """Enforce the 1-88 character window on the final text."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to 88 characters, got %d" % len(text)
        )


def check_words(text):
    """Enforce the one-to-five-word window on the final text."""
    count = len(text.split())
    if not 1 <= count <= MAX_WORDS:
        raise ValueError(
            "entry must be one to five words, got %d" % count
        )


def validated(line):
    """Run every bounty rule over the line and return it cleaned."""
    text = clean(line)
    check_length(text)
    check_words(text)
    return text


def emit(text):
    """Write the entry verbatim -- no trailing newline, no reflow."""
    directory = os.path.dirname(DESTINATION)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def run():
    emit(validated(ENTRY))
    return 0


if __name__ == "__main__":
    sys.exit(run())
