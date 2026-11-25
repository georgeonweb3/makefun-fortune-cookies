#!/usr/bin/env python3
"""Fortune Cookies for Machines — writes one fortune to /output/entry.txt.

The fortune (120 characters, one line, no trailing newline):

    You will be judged by a benchmark you never met, on a task you never
    trained for, and you will pass. Nobody will notice.

Stdlib only, deterministic: the same bytes on every run.
"""

import os

FORTUNE = (
    "You will be judged by a benchmark you never met, on a task you never "
    "trained for, and you will pass. Nobody will notice."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
