import cv2 as opcv
import numpy as np
import matplotlib.pyplot as plt
import read

# img = read.rescaleFrame(opcv.imread('photos/house.jpg'), 0.2)
# opcv.imshow('House', img)
# NOTE: BITWISE operations work only on binary values.

blank = np.zeros((400, 400), dtype='uint8')

rectangle = opcv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = opcv.circle(blank.copy(), (200, 200), 200, 255, -1)

# BITWISE AND, OR, XOR, NOT
bitwise_and = opcv.bitwise_and(circle, rectangle)
bitwise_or = opcv.bitwise_or(circle, rectangle)
bitwise_xor = opcv.bitwise_xor(circle, rectangle)
bitwise_not = opcv.bitwise_not(circle)


opcv.imshow('Rectangle', bitwise_not)
# opcv.imshow('Circle', circle)
opcv.waitKey(0)
