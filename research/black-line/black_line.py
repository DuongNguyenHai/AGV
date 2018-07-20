#!/usr/bin/python3
import cv2 as cv

cap = cv.VideoCapture('IMG_0777.MOV')
cv.namedWindow('video', cv.WINDOW_NORMAL)
cv.resizeWindow('video', 960, 540)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        # frame = cv.flip(frame, cv.flipMode=-1)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        _, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
        cv.imshow('video', thresh)
    else:
        break
    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows()
