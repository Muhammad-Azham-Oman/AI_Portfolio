from ultralytics import YOLO
import cv2
import numpy as np
import cvzone
from sort import *

coco_classes = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat',
    'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat',
    'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack',
    'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
    'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair',
    'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse',
    'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator',
    'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]


tracker = Sort(max_age=20 , min_hits=3 , iou_threshold=0.4)

limits = [400,297,673,297]

cap = cv2.VideoCapture("cars.mp4")
mask = cv2.imread("mask.png")
graphics = cv2.imread("graphics.png",cv2.IMREAD_UNCHANGED)

model = YOLO("yolov8n.pt")

count = []

while True:
    success, img = cap.read()
    img_region = cv2.bitwise_and(img , mask)
    results = model(img_region,stream=True)

    detections = np.empty((0,5))

    for r in results:
        boxes = r.boxes
        for box in boxes:

            conf = (round(float(box.conf[0]), 2))
            cls = coco_classes[int(box.cls[0])]

            if (cls in ['car', 'truck', 'motorcycle', 'bus']) and conf > 0.35:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # another method for mask
                # cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                # if mask[cy, cx] > 0:

                CurrentArray = np.array([x1,y1,x2,y2,conf])
                detections = np.vstack((detections, CurrentArray))

    img = cvzone.overlayPNG(img , graphics , (0,0))
    results = tracker.update(detections)
    cv2.line(img , (limits[0],limits[1]), (limits[2],limits[3]), (0,0,255),3)

    for result in results:
        x1 , y1 , x2 , y2 , Id = result
        x1, y1, x2, y2, Id = int(x1), int(y1), int(x2), int(y2), int(Id)
        w , h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1 , w ,h), l=9 , rt=2 , colorR=(0,0,255))


        cx, cy = x1 + w // 2, y1 + h // 2
        cv2.circle(img, (cx, cy), 5, (0,0,255), cv2.FILLED)

        if limits[0]<cx<limits[2] and limits[1]-20<cy<limits[3]+20:
            if count.count(Id)==0:
                count.append(Id)
                cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 3)

    cv2.putText(img, str(len(count)), (255, 100),cv2.FONT_HERSHEY_PLAIN, 5, (50,50,255),8)
    cv2.imshow('Webcam YOLO', img)
    cv2.waitKey(1)
