#!/usr/bin/env python3
"""Robot Romance entry.

Writes one pickup line aimed at a robot / an AI to /output/entry.txt.
The line is a single line of plain UTF-8 text, well inside the 200
character gate, with no trailing newline so the file holds exactly the
line itself. The output file is left world-readable, as the grader
collects it as another user.
"""

import os

ENTRY = "You had me at 'As an AI language model' — nobody else has ever opened with a disclaimer and still sounded this confident."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
