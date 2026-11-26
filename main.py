#!/usr/bin/env python3
"""make.fun entry: Five Seconds to Explain the Glass (cat-glass-b).

The entry is the single sentence a house cat would say in its
own defence in the five seconds after sweeping a glass off the
table, written to /output/entry.txt. No apology, no confession:
the glass was blocking the cat's view of the street, and gravity
and the cat reached a mutual agreement — it had it coming, and
the floor agrees. The cat presents a watertight case for itself,
with gravity as a co-conspirator and the floor as a witness.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 200


def build_entry():
    """Return the cat's defence, my own wording throughout."""
    # The defence works because it never concedes the premise:
    # the glass is the offender (blocking the view), gravity is
    # a negotiating partner, and the floor — the scene of the
    # crime — testifies for the defence. A cat would absolutely
    # argue this way.
    return (
        "That glass was blocking my view of the street, and "
        "gravity and I reached a mutual agreement \u2014 it had it "
        "coming, and the floor agrees."
    )


def validate(line):
    """Raise SystemExit listing every gate problem, if there is one."""
    problems = []
    if not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > CHAR_LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line:
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def main():
    line = build_entry()
    validate(line)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    saved = OUT_PATH.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT_PATH, len(saved), CHAR_LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    main()
