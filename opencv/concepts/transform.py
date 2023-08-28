import cv2 as opcv 
import numpy as np
import read as rd 



img = opcv.imread('photos/house.jpg')

resized = rd.rescaleFrame(img,0.2)
#NOTE: Image Transformation

# #Flipp
# flip = opcv.flip(resized,0)
# opcv.imshow('Fliped',flip)

# #ROTATION
# def rotate(img,angle,rotPoint = None):
#     (height,width)=img.shape[:2]
    
#     if rotPoint is None:
#         rotPoint = (width//2,height//2)
#     rotMat = opcv.getRotationMatrix2D(rotPoint,angle,1.0)
#     dimensions = (width,height)
    
#     return opcv.warpAffine(img,rotMat,dimensions)

# rotated = rotate(resized,-45)
# opcv.imshow('slanted',rotated)

# opcv.putText(resized,'Faye\'s Residence',(200,200),opcv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,0),thickness=3)

# #Translation
# def translate(img,x,y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1],img.shape[0])
#     # -x --> left
#     # -y -->up
#     # x -->right
#     # y -->Down
#     return opcv.warpAffine(img,transMat,dimensions)

# translated = translate(resized,-100,100)

#opcv.imshow('Crib',translated)

opcv.waitKey(0)