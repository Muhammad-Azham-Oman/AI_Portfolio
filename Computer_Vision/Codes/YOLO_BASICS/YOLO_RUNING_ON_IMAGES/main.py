from ultralytics import YOLO
import cv2
from pathlib import Path

path = Path(__file__).parent / "images" / "image1.jpg"

model = YOLO("yolov8n.pt")

results = model(path)

for r in results:
    img = r.plot()
    cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()