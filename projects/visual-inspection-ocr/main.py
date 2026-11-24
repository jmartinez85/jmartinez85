import argparse
import json
from pathlib import Path

import cv2

from detection import find_label
from ocr import read_code, read_label


def main():
    parser = argparse.ArgumentParser(description="Read a printed label and any visible QR code.")
    parser.add_argument("image", type=Path)
    parser.add_argument("--config", type=Path, default=Path("examples/config.example.json"))
    args = parser.parse_args()
    frame = cv2.imread(str(args.image))
    if frame is None:
        parser.error(f"Cannot open image: {args.image}")
    config = json.loads(args.config.read_text())
    bounds = find_label(frame, config["label_threshold"], config["min_area"])
    if bounds is None:
        parser.error("No label was detected.")
    print(json.dumps({"bounds": bounds, "text": read_label(frame, bounds), "qr": read_code(frame)}))


if __name__ == "__main__":
    main()
