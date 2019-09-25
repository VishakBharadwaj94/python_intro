#make the canny image show only region of interest

import cv2
import numpy as np
	

def to_canny(image):
	gray = cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY) 
	blur = cv2.GaussianBlur(gray,(5,5),0) #3rd Value is the standard deviation
	canny =cv2.Canny(blur,50,150)
	return canny

def region_of_interest(image):
	height=image.shape[0] 
	triangle=[np.array([[200,height],[1100,height],[550,250]],dtype=np.int32)]
	mask = np.zeros_like(image) #same shape for mask and image #mask is a black image
	cv2.fillPoly(mask,triangle,255) #that triangle will be white
	masked_image = cv2.bitwise_and(image,mask)
	return masked_image


image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny = to_canny(lane_image)
cv2.imshow("region",region_of_interest(canny))
cv2.waitKey(0)