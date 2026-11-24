![IA Software · Cutting-Edge Technology](../../assets/ia-software-banner.png)

# Visual Inspection, OCR, and Code Reading

Computer vision prototype

## Objective

Extract text and codes from inspection images and display them alongside object detections.

## Implementation

The application separates object detection, OCR, and presentation. It uses Tesseract for text recognition and pyzbar for code reading.

## Technologies

Python, OpenCV, YOLOv5, Tesseract, pyzbar.

## Run the demo

Install the Tesseract executable with English language data, then run:

```sh
python -m pip install -r requirements.txt
python main.py examples/demo_label.png
```

The output contains the label bounds, OCR text `DEMO-042`, and QR value `DEMO-042`. The synthetic fixture uses a bright label so its location can be demonstrated with OpenCV thresholding.

[Back to the portfolio](../../README.md)
