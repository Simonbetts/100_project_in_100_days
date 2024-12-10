# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	10/12/2024

"""
Day 11: Open CV


"""

import cv2 as cv
from time import sleep

#img = cv.imread("assets/images/diver.jpg", cv.IMREAD_GRAYSCALE)
img = cv.imread("assets/images/diver.jpg", cv.IMREAD_COLOR)
print(img.size) # the total pixels of the image
print(img.shape) # size of the image
print(img[0,0]) # first pixle in (RGB when color)

'''
while True:
	for i in range(3):
		img = img*(i+1)
		print(i)
		cv.imshow("Display window", img)
		cv.waitKey(0) # Wait for a keystroke in the window
		cv.destroyAllWindows()
		sleep(1)
	break
'''

'''
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		img[i,j] = max(254, img[i, j]*2)
'''

cv.imshow("Display window", img)
cv.waitKey(0) # Wait for a keystroke in the window
cv.destroyAllWindows()


gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imwrite("assets/images/diver_gray.jpg",gray_img)