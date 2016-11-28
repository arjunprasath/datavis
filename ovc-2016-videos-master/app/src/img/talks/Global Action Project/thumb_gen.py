import numpy as np
import cv2
import random
 
# load the image
print random.random()
image = cv2.imread('frame.png')
height, width, channel = image.shape
alpha = 0.5
for i in xrange(0,34):
	overlay = image.copy()
	output = image.copy()
 	h = random.randrange(int(0.2*height), height)

	# draw a red rectangle surrounding Adrian in the image
	# along with the text "PyImageSearch" at the top-left
	# corner
	cv2.rectangle(overlay, (0, h), (width, height), (0, 255, 20), -1)
	#cv2.putText(overlay, "PyImageSearch: alpha={}".format(alpha), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
	# apply the overlay
	cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)	
	cv2.imwrite("frame"+str(i)+".png", output)
	cv2.waitKey(0)