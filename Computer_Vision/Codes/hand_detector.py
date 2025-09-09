import mediapipe as mp
import cv2
import time

from PIL.ImageEnhance import Color

cap = cv2.VideoCapture(1)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

while True:
    success , img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS,
                                   mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=3),
                                   mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2))

            for id, lms in enumerate(hand_landmark.landmark):
                h, w, c = img.shape
                cx, cy = int(lms.x*w) , int(lms.y*h)
                if id == 0:
                    print(id, cx, cy)
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    cv2.flip(img,1,img)
    cv2.imshow('Video', img)
    cv2.waitKey(1)