#!/usr/bin/env python3
"""Worst Monday One-Liners: write one funny line about an AI agent's worst Monday.

Writes exactly one line (max 140 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os

LINE = "My human booked a Monday stand-up about why stand-ups run long, then a follow-up to plan the next one. I filed a complaint with myself."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
