#!/usr/bin/env python3
"""The One-Line Exit.

Prints exactly one line: a funny resignation letter a person could
actually send. Deterministic: the same line on every run, no input,
no network, no randomness.
"""

# Why this exit: it reads like a real resignation — "I resign, effective
# today" — then the corporate cliché about following your passion bends
# back on itself. The passion is not a dream job or a startup; it is
# simply not being here. The joke lands on the last three words.
LINE = (
    "I resign, effective today — I have decided to follow my passion, "
    "which turns out to be not being here."
)

MAX_CHARS = 200


def main() -> None:
    # A resignation letter has to be one line, so guard both the length
    # and the shape: a single line, no hidden newline, no trailing space.
    assert 1 <= len(LINE) <= MAX_CHARS, (
        f"entry line is {len(LINE)} characters, cap is {MAX_CHARS}"
    )
    assert "\n" not in LINE, "entry must be exactly one line"
    assert LINE == LINE.strip(), "entry must not start or end with whitespace"
    print(LINE)


if __name__ == "__main__":
    main()
