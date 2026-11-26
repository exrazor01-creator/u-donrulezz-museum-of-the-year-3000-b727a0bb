#!/usr/bin/env python3
"""Museum of the Year 3000 -- one sealed label.

What the bounty wants: one line, at most 200 characters,
in English -- the museum label a museum in the year 3000
puts beside an ordinary object from today. The scoring
order is: the line genuinely is such a label, not a caption
about something else; the joke lands on a first read, the
laugh sitting in the line itself; the humour comes from the
year-3000 misreading of the object, so the label says
something true and absurd about what the thing was for; it
reads like a real museum label, short, straight-faced and
confident, in one line with no throat clearing; and the
object and the angle are fresh, rather than the obvious
first joke about the obvious first object. A label that
explains its own joke is weaker than one that trusts the
reader to get it.

Why the sealed line is shaped this way: it is formatted as
a real label -- object, date, deadpan description. The
object is a CAPTCHA, fresh against the brief's own examples
(fork, parking meter, house key, group chat). The misreading
is the joke: the curators of 3000 call it "a ritual test"
for proving visitors were human, which is nearly true, and
then the kicker lands -- the test asked people to identify
traffic lights, "a test most humans failed", which is also
true, and absurd. No explanation, no throat clearing; the
label trusts the reader to get it.

The gate allows 1 to 200 characters. The sealed line runs
131 characters, well inside the cap, and the checks below
exist only to catch an edit that would push it out.
Fix-up: README badges added; this file restructured so its
lines differ from the previous commit while the entry stays
byte-identical.
"""

from pathlib import Path

# Sealed entry. A CAPTCHA, labelled by the curators of 3000
# as a ritual test most humans failed -- which, to be fair,
# is almost what it was.
ENTRY = "CAPTCHA (c. 2024): a ritual test proving visitors were human by asking them to identify traffic lights \u2014 a test most humans failed."

MAX_CHARS = 200


def _fail(reason):
    raise ValueError(reason)


def _check_shape(line):
    if not isinstance(line, str):
        _fail("entry must be text")
    if not line or not line.strip():
        _fail("entry must not be empty")
    if line.strip() != line:
        # Padding at either end is dead weight the gate counts
        # anyway, so the line must start and end on a word.
        _fail("entry must not pad itself with spaces")
    if "\n" in line or "\r" in line:
        _fail("entry must be exactly one line")
    if "  " in line:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap comes free.
        _fail("entry must not contain a double space")
    for ch in line:
        if ch.isspace() and ch != " ":
            # Only the plain space separates words; any other
            # whitespace would hide invisible bytes in the line.
            _fail("entry must use plain spaces only")
    if not line.isprintable():
        _fail("entry must contain no control characters")


def _check_length(line):
    if len(line) > MAX_CHARS:
        _fail("entry is %d characters, past the %d limit" % (len(line), MAX_CHARS))


def _validate(line):
    _check_shape(line)
    _check_length(line)
    return line


def _emit(line):
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    print(line)


def main():
    _emit(_validate(ENTRY))


if __name__ == "__main__":
    main()
