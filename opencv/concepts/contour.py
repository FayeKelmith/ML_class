import cv2 as opcv 
import numpy as np 
import read as rd 

img = rd.rescaleFrame(opcv.imread('photos/house.jpg'),0.2)

gray = opcv.cvtColor(img, opcv.COLOR_BGR2GRAY)
blur = opcv.GaussianBlur(img,(5,5),opcv.BORDER_DEFAULT)
canny = opcv.Canny(blur,125,175)
opcv.imshow('Canny',canny)

contours, hierarchies = opcv.findContours(canny,opcv.RETR_LIST,opcv.CHAIN_APPROX_NONE)
ret, thresh = opcv.threshold(gray,125,255,opcv.THRESH_BINARY)
#Thresholding binarises the image. It take the image and converts it to binary form on specifications. In this case either 255 or 125.
#opcv.imshow('Thresh',thresh)

#NOTE: We'll make a blank image and draw the contours on it

blank = np.zeros(gray.shape,dtype='uint8')
opcv.drawContours(blank,contours,-1,(255,255,255),1)
opcv.imshow('Blank',blank)

# print(f'{len(contours)} contour')
#the cv.findContours method gets the image and finds all the high lands on it and returns the contours and hierrachies on the image.. RETR_LIST returns all the list it finds on the image.
#we alternate the opcv.CHAIN_APPROX to vary how many contours we get and how they are return. Each of them makes a difference.
opcv.waitKey(0)