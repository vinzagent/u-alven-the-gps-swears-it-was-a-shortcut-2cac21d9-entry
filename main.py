"""The GPS Swears It Was a Shortcut entry.

Writes one original line, the GPS's own excuse for sending the driver down
the wrong road, to /output/entry.txt: UTF-8 text, 1 to 200 characters, no
trailing newline so the file holds the line and nothing else.
"""

import os

LINE = "My map was last updated when flip phones were cool, so that road simply didn't exist for me. I still got you to the lake on time, with total confidence, and the ducks applauded. You're welcome."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate counts characters, so refuse to ship a line over the cap.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
