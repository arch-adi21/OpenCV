import cv2 as cv

img = cv.imread("Photo/MY1.jpg")

cv.imshow('MY1',img)

def rescaleFrame(frame , scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width, height)
    return cv.resize(frame,dimension, interpolation= cv.INTER_AREA)
    
cv.waitKey(0)