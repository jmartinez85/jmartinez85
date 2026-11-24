![IA Software · Cutting-Edge Technology](../../assets/ia-software-banner.png)

# Particle and Bubble Inspection

Inspection application

## Objective

Inspect particles and bubbles in images, recorded video, and live camera feeds using settings that can be reproduced across sessions.

## Implementation

The pipeline separates image acquisition, preprocessing, segmentation, and tracking. A live preview lets operators adjust masks and regions of interest. The same inspection profiles can be used for batch processing.

The local test suite covers parts of the pipeline, including tracking.

## Technologies

Python, OpenCV, NumPy, YOLO11.

## Run the demo

This independent demo uses synthetic video and a simple centroid tracker. It illustrates the offline workflow with a deterministic input.

```sh
python -m pip install .
python examples/generate_demo_video.py demo.avi
python -m particle_v2.batch_runner demo.avi --profile examples/profile.example.json --output tracks.csv
python -m unittest discover -s tests
```

The CSV contains 120 detections across 60 frames. The two particles retain their track IDs.

[Back to the portfolio](../../README.md)
