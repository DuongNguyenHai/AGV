#!/usr/bin/python3
import cv2 as cv

cv.namedWindow('test', cv.WINDOW_NORMAL)
cv.resizeWindow('test', 960, 540)
test1 = cv.imread('test1.png')

gray = cv.cvtColor(test1, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)


cv.imshow('test', thresh)

cv.waitKey(0)
cv.destroyAllWindows()