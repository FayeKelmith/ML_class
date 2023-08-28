import cv2 as opcv
import numpy as np
import read

# NOTE: We are spliting images into various channels (grayscale) and then merging them back. Upon split, they lose the third dimension. Upon merge they regain old channels

img = read.rescaleFrame(opcv.imread('photos/house.jpg'), 0.2)
blank = np.zeros(img.shape[:2], dtype='uint8')
b, g, r = opcv.split(img)

blue = opcv.merge([b, blank, blank])
green = opcv.merge([blank, g, blank])
red = opcv.merge([blank, blank, r])

merged = opcv.merge([blue, green, red])
opcv.imshow('Merged', merged)

# opcv.imshow('Blue', blue)
# opcv.imshow('Green', green)
# opcv.imshow('Red', red)


# opcv.imshow('Blue', b)
# opcv.imshow('Green', g)
# opcv.imshow('Red', r)


# The code is displaying the merged image using `opcv.imshow('Merged', merged)`.
# opcv.imshow('Merged', merged)
# print(f"Merged: {merged.shape}")
# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

opcv.waitKey(0)
