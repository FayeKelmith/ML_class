import cv2 as opcv
import numpy as np
import matplotlib.pyplot as plt
import read

# INFO: masks must have thesame dimensions as the parent if they must work.
img = read.rescaleFrame(opcv.imread('photos/cat2.jpg'), 0.2)
blank = np.zeros(img.shape[:2], dtype='uint8')
mask = opcv.circle(
    blank, (img.shape[1]//2-150, img.shape[0]//2-25), 150, 255, -1)
masked = opcv.bitwise_and(img, img, mask=mask)
opcv.imshow('Mask', masked)
opcv.waitKey(0)
