import pywt
import numpy as np
import cv2

def w2d(img , mode = 'haar' , level = 1):
    array = img
    Array = cv2.cvtColor(array , cv2.COLOR_BGR2GRAY)
    imArray = np.float32(Array)
    imArray /= 255;
    coeffs = pywt.wavedec2(imArray , mode , level=level)
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0;
    imArray_H = pywt.waverec2(coeffs_H , mode);
    imArray_H *= 255;
    imArray_H = np.uint8(imArray_H)

    return imArray_H