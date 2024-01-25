import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')

# cv.imshow('blank',blank)

# blank[:]= 0 , 225 , 0
# cv.imshow('green',blank)

# rect = cv.rectangle(blank,(0,0),(200,250),(0,0,225),thickness=2)
# rect = cv.rectangle(blank,(0,0),(200,250),(0,0,225),thickness=cv.FILLED)

rect = cv.rectangle(blank,(0,0),(blank.shape[0]//2, blank.shape[1]//1),(0,0,225),thickness=cv.FILLED)

rect_circ = cv.circle(rect,(rect.shape[0]//2, rect.shape[1]//2) , 60 , (0,225,0), thickness= -1)

word = cv.putText(rect_circ,'Aditya', (100,100) , cv.FONT_HERSHEY_SCRIPT_COMPLEX , 1.5 , (225,225,225) , thickness=1)

cv.imshow('image_with_words',word)

cv.waitKey(0)