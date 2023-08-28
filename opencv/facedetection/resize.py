import cv2 as opcv


# NOTE: RESIZING AND RESCALING
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimension = (width, height)

    return opcv.resize(frame, dimension, interpolation=opcv.INTER_AREA)
