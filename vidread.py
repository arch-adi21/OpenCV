import cv2 as cv

vid = cv.VideoCapture("Video/Rabbit.mp4")

def rescaleFrame(frame , scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width, height)
    return cv.resize(frame,dimension, interpolation= cv.INTER_AREA)
    

while True :
    isTrue , frame = vid.read()
    frame = rescaleFrame(frame)
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

vid.release()
cv.destroyAllWindows()