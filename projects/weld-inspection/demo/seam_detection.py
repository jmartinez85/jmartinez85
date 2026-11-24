"""Locate a bright seam in a grayscale NumPy image."""

import argparse
from pathlib import Path

import numpy as np


def find_seam(image):
    if image.ndim != 2 or image.size == 0:
        raise ValueError("Expected a nonempty grayscale image.")
    profile = image.astype(np.float32).mean(axis=0)
    return int(profile.argmax())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    args = parser.parse_args()
    print(f"Seam column: {find_seam(np.load(args.image, allow_pickle=False))}")


if __name__ == "__main__":
    main()
