import cv2
import numpy as np

def to_canny(image):
	gray = cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY) 
	blur = cv2.GaussianBlur(gray,(5,5),0) #3rd Value is the standard deviation
	canny =cv2.Canny(blur,50,150)
	return canny

def display_lines(img,lines):
	# line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
	line_img=np.zeros_like(img)
	for line in lines:
		for x1,y1,x2,y2 in line:
			cv2.line(line_img, (x1, y1), (x2, y2), [255, 0, 0], 10)
	return line_img

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
cropped_image=region_of_interest(canny)
lines = cv2.HoughLinesP(cropped_image,2,np.pi/180, 100, np.array([]), minLineLength=40,maxLineGap=4)
line_image=display_lines(lane_image,lines)
blended_image = cv2.addWeighted(lane_image,0.6,line_image,1.5,1)
cv2.imshow("region",blended_image)
cv2.waitKey(0)