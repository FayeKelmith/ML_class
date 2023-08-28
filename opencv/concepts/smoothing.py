import cv2 as opcv
import numpy as np
import read

# average
img = read.rescaleFrame(opcv.imread('photos/house.jpg'), 0.2)
average = opcv.blur(img, (5, 5))
opcv.imshow('Average', average)

# Gaussian blur
blur = opcv.GaussianBlur(img, (5, 5), 0)
opcv.imshow('Gaussian', blur)

# median blur
median = opcv.medianBlur(img, 5)
opcv.imshow('Median', median)

# Bilateral Blur
# Retains the edges of the images. Quite useful
# Most useful in deep learning algorithms.

bilateral = opcv.bilateralFilter(img, 10, 35, 25)
opcv.imshow('Bilateral', bilateral)


opcv.waitKey(0)
