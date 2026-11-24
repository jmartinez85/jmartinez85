import argparse
from pathlib import Path

import numpy as np

parser = argparse.ArgumentParser(description="Create a synthetic grayscale seam sample.")
parser.add_argument("output", type=Path)
args = parser.parse_args()
rng = np.random.default_rng(42)
image = rng.integers(0, 25, size=(120, 240), dtype=np.uint8)
image[:, 111:116] = (90, 160, 240, 160, 90)
np.save(args.output, image)
