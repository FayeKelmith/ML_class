import cv2 as opcv 
import matplotlib.pyplot as plt
import read

#OPENCV reads colors in BGR not RGB. A way to demonstrate this is by placing thesame image on matplotlib and getting the RBG version which has reversed colors since images are read in opencv using the RGB code color

#NOTE: to convert a BGR image to an RGB, we do the following

img = read.rescaleFrame(opcv.imread('photos/house.jpg'),0.2)

#BGR to RGB
rgb = opcv.cvtColor(img,opcv.COLOR_BGR2RGB)
# plt.imshow(rgb)
# plt.show()

#BGR to Grayscale
gray = opcv.cvtColor(img,opcv.COLOR_BGR2GRAY)

#BGR to HSV
hsv = opcv.cvtColor(img,opcv.COLOR_BGR2HSV)

#HSV to BGR
hsv_bgr = opcv.cvtColor(hsv,opcv.COLOR_HSV2BGR)
#BGR to LAB
lab = opcv.cvtColor(img,opcv.COLOR_BGR2LAB)
#LAB to bgr
lab_bgr = opcv.cvtColor(lab,opcv.COLOR_LAB2BGR)
opcv.imshow('House',lab_bgr)

opcv.waitKey(0)