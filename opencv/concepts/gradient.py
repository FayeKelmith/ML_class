import cv2 as opcv
import matplotlib.pyplot as plt
import numpy as np
import read


img = read.rescaleFrame(opcv.imread('photos/house.jpg'), 0.2)

gray = opcv.cvtColor(img, opcv.COLOR_BGR2GRAY)

# laplacian
lap = opcv.Laplacian(gray, opcv.CV_64F)
# computes the laplacien of the pixels of the images
lap = np.uint8(np.absolute(lap))
# converts all the derivatives into positive numbers because we can't have negative pixels and type cast it as an image.

# opcv.imshow('Lapacian', lap)

# Sobel
sobelx = opcv.Sobel(gray, opcv.CV_64F, 1, 0)
sobely = opcv.Sobel(gray, opcv.CV_64F, 0, 1)

combined = opcv.bitwise_or(sobelx, sobely)

opcv.imshow('Combined', combined)
# opcv.imshow('Sobel X', sobelx)
# opcv.imshow('Sobel Y', sobely)

# CANNY
canny = opcv.Canny(gray, 150, 175)
opcv.imshow('Canny', canny)
# cleaner version. Better for most cases.canny
opcv.waitKey(0)
