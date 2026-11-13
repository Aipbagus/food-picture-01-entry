#!/usr/bin/env python3
"""Entry for make.fun food-picture-01: writes a food picture to /output/entry.png.

The image ships with the repository; the program simply copies it to the
required output path. No network, no randomness: two runs write identical bytes.
"""
import shutil
import os

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")


def main() -> None:
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
