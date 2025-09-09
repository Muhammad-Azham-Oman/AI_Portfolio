import cv2
import numpy as np
import mediapipe as mp
import time
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cap = cv2.VideoCapture(1)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

range_vol = volume.GetVolumeRange()

min_vol = range_vol[0]
max_vol = range_vol[1]

prev_length = None
prev_vol = None
stable_start_time = None
lock_duration = 1
volume_locked = False

while True:
    success , img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS,
                                   mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=3),
                                   mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2))

            empty_list=[]
            for id, lms in enumerate(hand_landmark.landmark):
                h, w, c = img.shape
                cx, cy = int(lms.x*w) , int(lms.y*h)
                empty_list.append([id, cx, cy])
                if id == 4 or id == 8:
                    if len(empty_list) > 8:

                        x1 , y1 = empty_list[4][1], empty_list[4][2]
                        x2, y2 = empty_list[8][1], empty_list[8][2]
                        lcx, lcy = (x1+x2)//2, (y1+y2)//2

                        length = math.hypot(x2-x1, y2-y1)
                        vol = np.interp(length, [25,180] , [min_vol, max_vol])

                        if not volume_locked:
                            if prev_length is not None and abs(length - prev_length) <= 5:
                                if stable_start_time is None:
                                    stable_start_time = time.time()
                                elif time.time() - stable_start_time >= lock_duration:
                                    vol = prev_vol
                                    volume_locked = True
                            else:
                                stable_start_time = None

                            volume.SetMasterVolumeLevel(vol, None)
                            prev_vol = vol

                        prev_length = length

                        cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
                        cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
                        cv2.line(img, (x1,y1), (x2,y2), (255, 0, 0), 2)
                        cv2.circle(img, (lcx, lcy), 10, (255, 0, 0), cv2.FILLED)

                        if length<=25:
                            cv2.circle(img, (lcx, lcy), 10, (0, 255, 0), cv2.FILLED)
                        if length>=180:
                            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    else:
        volume_locked = False
        prev_length = None
        stable_start_time = None

    cv2.flip(img,1,img)
    cv2.imshow('Video', img)
    cv2.waitKey(1)
