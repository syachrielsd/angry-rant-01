#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry for make.fun.

Writes one short, funny rant (<= 400 chars) to the output directory's
entry.txt. The rant: a self-checkout machine accuses you of stealing
the milk you just scanned, an attendant treats you like a suspect,
and you still pay full price -- for the privilege of being acquitted.
Micro-story shape: grievance -> escalation -> twist in the last beat.
"""

import os
import sys

RANT = (
    "The self-checkout let me scan my own milk, then accused me of "
    "stealing it: \"Unexpected item in the bagging area.\" An attendant "
    "typed a secret code and studied me like a suspect \u2014 then charged "
    "me full price for the privilege of being acquitted."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(RANT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
