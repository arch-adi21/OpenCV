import cv2 as cv

img = cv.imread('Photo/MY1.jpg')

# Coverting to gray-scale

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#Blurring the image using gaussian blurr
blur = cv.GaussianBlur(img , (3,3), cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

# Edge cascade
canny = cv.Canny(img,125,175)
cv.imshow('canny',canny)

# Dialating the canny image
dil = cv.dilate(canny , (7,7) , iterations=3 )
cv.imshow('dil',dil)

# Eroding back the dilated image 
erd = cv.erode(dil , (3,3) , iterations=1)
cv.imshow('erd',erd)

#resizing the image

resize = cv.resize(img , (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize',resize)

# Croping of image
cropped = img[20:100, 300:250]
cv.imshow('crop',cropped)

cv.waitKey(0)
