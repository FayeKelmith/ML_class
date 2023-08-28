import cv2 as opcv
import matplotlib.pyplot as plt
import read


img = read.rescaleFrame(opcv.imread('photos/house.jpg'), 0.2)

gray = opcv.cvtColor(img, opcv.COLOR_BGR2GRAY)
# opcv.imshow('Gray', gray)
# Simple Thresholding
threshold, thresh = opcv.threshold(gray, 150, 255, opcv.THRESH_BINARY)
# opcv.imshow('Simple Thresholded', thresh)

# threshold, thresh_inv = opcv.threshold(gray, 150, 255, opcv.THRESH_BINARY_INV)
# opcv.imshow('Simple Thresholded', thresh_inv)

# Adaptive Thresholding
# In adaptive thresholding opencv determines the values for us. It's quite effective.GaussianBlur
adaptive_thresh = opcv.adaptiveThreshold(
    gray, 255, opcv.ADAPTIVE_THRESH_GAUSSIAN_C, opcv.THRESH_BINARY, 15, 3)

# 11 is the block size, 3 is the constant
opcv.imshow('Adaptive Thresholded', adaptive_thresh)
opcv.waitKey(0)
