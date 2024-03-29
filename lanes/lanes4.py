#-------------convert canny to a function and see image with matplotlib---------------#

import cv2
import numpy as np
import matplotlib.pyplot as plt #which also has imshow()		

def to_canny(image):
	gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY) 
	blur = cv2.GaussianBlur(gray,(5,5),0) #3rd Value is the standard deviation
	canny =cv2.Canny(blur,50,150)
	return canny

image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny = to_canny(lane_image)
plt.imshow(image)
plt.imshow(canny)
plt.show()


