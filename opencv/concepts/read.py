import cv2 as opcv 


#NOTE: RESIZING AND RESCALING
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dimension = (width,height)
    
    return opcv.resize(frame,dimension,interpolation = opcv.INTER_AREA)


#NOTE: reading videos
#cap = opcv.VideoCapture('videos/cat.mp4')
# cap = opcv.VideoCapture(0)

# while True:
#     isTrue,frame = cap.read()
#     opcv.imshow('Video',frame)
    
#     frame_resized = rescaleFrame(frame)
#     opcv.imshow('Resized',frame_resized)
    
    
#     if opcv.waitKey(20) & 0xFF==ord('d'):
#         break
# cap.release()
# opcv.destroyAllWindows()

#NOTE: reading picture
# img = opcv.imread('photos/cat1.jpg')

# resized_img = rescaleFrame(img,0.25)
# opcv.imshow('Cat',resized_img)

opcv.waitKey(0)

