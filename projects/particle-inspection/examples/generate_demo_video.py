import argparse
from pathlib import Path

import cv2
import numpy as np

parser = argparse.ArgumentParser(description="Generate a deterministic inspection video.")
parser.add_argument("output", type=Path)
args = parser.parse_args()
writer = cv2.VideoWriter(str(args.output), cv2.VideoWriter_fourcc(*"MJPG"), 15, (320, 180))
if not writer.isOpened():
    raise SystemExit("The MJPG video writer could not be opened.")
try:
    for frame_number in range(60):
        frame = np.zeros((180, 320, 3), dtype=np.uint8)
        cv2.circle(frame, (35 + 3 * frame_number, 52), 7, (255, 255, 255), -1)
        cv2.circle(frame, (280 - 2 * frame_number, 130), 11, (230, 230, 230), -1)
        writer.write(frame)
finally:
    writer.release()
