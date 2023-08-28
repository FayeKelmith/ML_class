import cv2 as opcv 
import read as rd


img = opcv.imread('photos/house.jpg')
resized = rd.rescaleFrame(img,0.2)
opcv.imshow('CAT',resized)





#Cropping
cropped = resized[20:300,50:250]
opcv.imshow('Cropped',cropped)


# #Resizing images & videos
# res = opcv.resize(resized,(500,500), interpolation=opcv.INTER_CUBIC)
# opcv.imshow('Resized',res)

#BLURING AN IMAGE
# blur = opcv.GaussianBlur(resized,(7,7),opcv.BORDER_DEFAULT)
# opcv.imshow('BLUR',blur)

# #Dilating the image
# dilated = opcv.dilate(casc,(3,3),iterations=1)
# opcv.imshow('Dilated',dilated)

# #Eroding the image

# eroded = opcv.erode(dilated,(3,3),iterations=1)
# opcv.imshow('Eroded',eroded)

# #EDGE CASCADING
# casc = opcv.Canny(resized,125,175)
# opcv.imshow('Edge Cascading',casc)
# #NOTE: you can get less edgy lines by using a blurred image. The more blurred out the images, the fainter the canny edgees


#GRAYING OUT AN IMAGE
#gray = opcv.cvtColor(resized,opcv.COLOR_BGR2GRAY)
#opcv.imshow('GRAY CAT',gray)
opcv.waitKey(0)