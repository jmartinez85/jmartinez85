import argparse
import json
from pathlib import Path

from hand_tracking import gripper_state


def main():
    parser = argparse.ArgumentParser(description="Replay normalized hand landmarks.")
    parser.add_argument("landmarks", type=Path)
    args = parser.parse_args()
    closed = False
    for frame, points in enumerate(json.loads(args.landmarks.read_text()), start=1):
        closed = gripper_state(points["thumb"], points["index"], closed)
        print(f"Frame {frame}: {'CLOSED' if closed else 'OPEN'}")


if __name__ == "__main__":
    main()
