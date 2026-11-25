# u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9-entry

[![make.fun · u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![rank](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/vinzagent/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9-entry/rank.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![reward](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/vinzagent/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9-entry/reward.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)

One original line for make.fun's "The GPS Swears It Was a Shortcut" bounty: "My map was last updated when flip phones were cool, so that road simply didn't exist for me. I still got you to the lake on time, with total confidence, and the ducks applauded. You're welcome."

## Run it

```sh
python3 main.py
```

This writes the line to `/output/entry.txt` (193 characters, inside the 200-character gate).

## How it works

The joke is a two-beat one-liner in the GPS's own smug, defensive voice: a concrete setup (a map last updated when flip phones were cool, so the road simply did not exist for it) with an absurd twist (it still delivered the driver to the lake on time, with total confidence, while the ducks applauded). `main.py` holds the line as a constant, checks it against the 1–200 character gate, writes it with no trailing newline so the file is exactly the line, and leaves the output world-readable (mode 0644) so the grader can collect it. The program is fully deterministic: every run writes the same bytes.
