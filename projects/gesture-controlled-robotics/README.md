![IA Software · Cutting-Edge Technology](../../assets/ia-software-banner.png)

# Gesture-Controlled Robotics in RoboDK

Simulation prototype

## Objective

Explore gesture control for a robotic tool and gripper in a simulated workcell.

## Implementation

A webcam feeds a hand landmark detector. The prototypes map those coordinates to movement targets in RoboDK and use the relative positions of the fingers to operate the gripper.

## Technologies

Python, MediaPipe, OpenCV, RoboDK.

## Run the demo

Run `python demo/gripper_control.py examples/gesture_landmarks.json` with Python 3.10 or newer. The sample replays three frames and prints `OPEN`, `CLOSED`, then `OPEN`. See [how the gesture maps to a simulated gripper](docs/robodk-setup.md).

[Back to the portfolio](../../README.md)
