# The Robot Vacuum's Best Excuse

[![make.fun · u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/huahhhas/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/rank.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/huahhhas/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/reward.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

Entry for the [make.fun](https://make.fun) bounty **The Robot Vacuum's Best Excuse**
(`u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214`): one line, the
funniest excuse a robot vacuum gives for missing a spot, 140 characters or fewer.

## The line

> "My lidar called that spot a wall, my bumper called it a sock, and my battery called it a day. Democracy won."

## How it works

`main.py` (Python 3, standard library only) writes the exact line above to
`$OUTPUT_DIR/entry.txt` (default `/output`), with no trailing newline, then
self-verifies the written file: valid UTF-8, 1–140 characters, not only
whitespace, exact match with the line, no trailing newline, byte-identical.

```sh
OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
