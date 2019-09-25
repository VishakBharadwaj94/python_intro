import cv2
import numpy as np 		

image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)  #converts images from one color space to another
blur = cv2.GaussianBlur(gray,(5,5),0) #3rd Value is the standard deviation
cv2.imshow("input",gray)
cv2.imshow("result",blur)
cv2.waitKey(0)