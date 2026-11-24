#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun bounty entry.

Writes one line, the funniest excuse a robot vacuum gives for missing a
spot, to $OUTPUT_DIR/entry.txt (default /output), with no trailing newline,
then self-verifies the written file against the competition gate:
UTF-8 text, 1 to 140 characters, not only whitespace, exact match with the
line below, no trailing newline, byte-identical.
"""

import os
import sys

LINE = "My lidar called that spot a wall, my bumper called it a sock, and my battery called it a day. Democracy won."

MAX_CHARS = 140


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Self-verification: re-read the file and check every gate condition.
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # raises if not valid UTF-8
    errors = []
    if raw != data:
        errors.append("written bytes differ from the line")
    if text != LINE:
        errors.append("written text does not exactly match the line")
    if not (1 <= len(text) <= MAX_CHARS):
        errors.append(f"length {len(text)} outside 1..{MAX_CHARS} characters")
    if not text.strip():
        errors.append("text is only whitespace")
    if raw.endswith(b"\n"):
        errors.append("trailing newline present")
    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        return 1
    print(f"OK: entry.txt written ({len(text)} chars, {len(raw)} bytes), all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
