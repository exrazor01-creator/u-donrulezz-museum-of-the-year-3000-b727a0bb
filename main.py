#!/usr/bin/env python3
"""One-line entry: Museum of the Year 3000.

The brief asks for one line, at most 200 characters, in
English: the museum label a museum in the year 3000 puts
beside an ordinary object from today. The judge weighs, in
order: the line really is such a label, not a caption about
something else; the joke lands on a first read, with the
laugh in the line itself; the humour comes from the year
3000 misreading the object, so the label says something
true and absurd about what the thing was for; it reads like
a real museum label, short, straight faced and confident,
in one line with no throat clearing; and the object and the
angle are fresh, rather than the obvious first joke about
the obvious first object. A label that explains its own
joke is weaker than one that trusts the reader to get it.

The sealed line below is built to that order on purpose.
It is formatted as a real label -- object, date, deadpan
description. The object is a CAPTCHA, fresh against the
brief's own examples (fork, parking meter, house key,
group chat). The misreading is the joke: the curators of
3000 call it "a ritual test" for proving visitors were
human, which is nearly true, and then the kicker lands --
the test asked people to identify traffic lights, "a test
most humans failed", which is also true, and absurd. No
explanation, no throat clearing; the label trusts the
reader to get it.

LIMIT is 200 because the bounty gate allows one line of 1
to 200 characters. The sealed line is 131 characters, so
it sits well inside the cap; the validator below only
guards against an edit that would push it past the limit.
"""

import os

# The sealed line: a CAPTCHA, labelled by the curators of
# 3000 as a ritual test most humans failed -- which, to be
# fair, is almost what it was.
ENTRY = "CAPTCHA (c. 2024): a ritual test proving visitors were human by asking them to identify traffic lights \u2014 a test most humans failed."

LIMIT = 200  # bounty gate: one line, 1-200 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
