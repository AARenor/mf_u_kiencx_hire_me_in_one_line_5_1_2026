#!/usr/bin/env python3
"""Write the one-line entry for make.fun bounty u-kiencx-hire-me-in-one-line-5a108081."""

import os
import sys
from pathlib import Path

TEXT = "The 3am page went to my agent, not to me; by morning the incident was a one-paragraph note and the phone was still face down."


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir is None:
        output_dir = os.environ.get("OUTPUT_DIR", "/output")
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
