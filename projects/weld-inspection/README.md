![IA Software · Cutting-Edge Technology](../../assets/ia-software-banner.png)

# Weld Inspection

Industrial application and integration

## Objective

Locate a weld seam and connect a vision detector to an existing LabVIEW system.

## Implementation

The application calculates intensity profiles within a region of interest and tracks the seam across frames. A companion implementation exchanges images and results over TCP between 32-bit LabVIEW and a YOLOv5 detector running in 64-bit Python.

Tests cover intensity profiles, region selection, presets, and weld width validation.

## Technologies

Python, OpenCV, YOLOv5, LabVIEW, TCP.

## Run the demo

```sh
python -m pip install -r requirements.txt
python demo/generate_sample.py sample.npy
python demo/seam_detection.py sample.npy
python -m unittest discover -s tests
```

The expected result is `Seam column: 113`. See [the integration diagram](docs/legacy-integration.md) for the historical system boundary.

[Back to the portfolio](../../README.md)
