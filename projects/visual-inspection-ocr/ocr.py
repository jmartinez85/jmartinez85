import cv2
import pytesseract


def read_label(frame, bounds):
    x, y, width, height = bounds
    crop = frame[y:y + height, x:x + width]
    return " ".join(pytesseract.image_to_string(crop, config="--psm 7").split())


def read_code(frame):
    value, _, _ = cv2.QRCodeDetector().detectAndDecode(frame)
    return value
