from PIL import Image
import pytesseract
import cv2
import numpy as np
import imutils

i=cv2.imread('example.jpg',0)
image = imutils.resize(image, height=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255)
cv2.imshow("e",edged)


# find contours in the edge map, then sort them by their
# size in descending order
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
displayCnt = None
 
# loop over the contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
 
	# if the contour has four vertices, then we have found
	# the thermostat display
	if len(approx) == 4:
		displayCnt = approx
		break
# extract the thermostat display, apply a perspective transform
# to it
warped = four_point_transform(gray, displayCnt.reshape(4, 2))
output = four_point_transform(image, displayCnt.reshape(4, 2))
kernel=np.ones((9,9),np.float32)
erosion=cv2.erode(i,kernel,iterations=2)
thres1h=cv2.inRange(erosion,0,100)
thresh=cv2.bitwise_not(thres1h)
cv2.imshow("ero",thresh)
cv2.imwrite("e.jpg",thresh)
i=Image.open("e.jpg")
t=pytesseract.image_to_string(i,config='outputbase digits')
print (t)
cv2.waitKey(0)
