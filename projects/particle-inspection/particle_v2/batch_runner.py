import argparse
import csv
import json
from pathlib import Path

import cv2

from .tracker import CentroidTracker


def inspect(video, profile):
    capture = cv2.VideoCapture(str(video))
    if not capture.isOpened():
        raise ValueError(f"Cannot open video: {video}")
    tracker = CentroidTracker(profile["max_distance"])
    try:
        frame_number = 0
        while True:
            success, frame = capture.read()
            if not success:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(gray, profile["threshold"], 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            points = []
            for contour in contours:
                moments = cv2.moments(contour)
                area = moments["m00"]
                if area >= profile["min_area"]:
                    points.append((round(moments["m10"] / area), round(moments["m01"] / area)))
            for track_id, (x, y) in sorted(tracker.update(sorted(points)).items()):
                yield video.name, frame_number, track_id, x, y
            frame_number += 1
    finally:
        capture.release()


def main():
    parser = argparse.ArgumentParser(description="Track bright particles in recorded video.")
    parser.add_argument("videos", type=Path, nargs="+")
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    profile = json.loads(args.profile.read_text())
    rows = [row for video in args.videos for row in inspect(video, profile)]
    with args.output.open("w", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["video", "frame", "track_id", "x", "y"])
        writer.writerows(rows)
    print(f"Wrote {len(rows)} detections to {args.output}")


if __name__ == "__main__":
    main()
