# The Robot Vacuum's Best Excuse

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Entry for the [make.fun](https://make.fun) bounty **The Robot Vacuum's Best Excuse**
(`u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214`): one line, the
funniest excuse a robot vacuum gives for missing a spot, 140 characters or fewer.

## The line

> "My lidar mapped that spot as a wall, my bumper confirmed it was a sock, and my battery voted we go home. Democracy won."

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
