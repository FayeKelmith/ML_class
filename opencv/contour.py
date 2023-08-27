import cv2 as opcv 
import numpy as np 
import read as rd 

img = rd.rescaleFrame(opcv.imread('photos/house.jpg'),0.2)

gray = opcv.cvtColor(img, opcv.COLOR_BGR2GRAY)

canny = opcv.Canny(gray,125,175)
opcv.imshow('Contour',canny)

contours, hierarchies = opcv.findContours(canny,opcv.RETR_LIST,opcv.CHAIN_APPROX_NONE)

#the cv.findContours method gets the image and finds all the high lands on it and returns the contours and hierrachies on the image.. RETR_LIST returns all the list it finds on the image.
#
opcv.waitKey(0)