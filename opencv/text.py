import cv2 as opcv 
import numpy as np 

#defining a blank page
blank = np.zeros((500,500,3),dtype='uint8')
#setting it to a greyish color
blank[:] = 200,200,200
#img = opcv.imread('photos/cat1.jpg')

#def: drawing a rectangle on blankpage
# opcv.rectangle(blank,(100,100),(400,400),(0,0,0),thickness=-1)
#opcv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,0,0),thickness=-1)


#opcv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),50,(0,0,0),thickness=-1)
#opcv.line(blank,(0,0),(500,500),(0,0,0),thickness=5)
opcv.putText(blank,'Faye?',(200,250),opcv.FONT_HERSHEY_SIMPLEX,1.2,(10,10,10),thickness=3)
opcv.imshow('Blank',blank)
opcv.waitKey(0)