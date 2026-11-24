import cv2


def find_label(frame, threshold, min_area):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    candidates = [shape for shape in contours if cv2.contourArea(shape) >= min_area]
    if not candidates:
        return None
    return cv2.boundingRect(max(candidates, key=cv2.contourArea))
