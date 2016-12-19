import numpy as np
import cv2
import random
 
# load the image
print random.random()
view_arr = [651, 174, 186, 651, 1018, 280, 528, 1633, 2117, 2224, 1253, 615, 350, 410, 380, 554, 803, 2722, 960, 186, 174, 14429, 188, 382, 231, 192, 201, 385, 807, 581, 581, 807]
view_arr_sorted = list(view_arr)
view_arr_sorted.sort()
print view_arr
image = cv2.imread('./imgs/frame0.png')
height, width, channel = image.shape
alpha = 0.6
for i in xrange(0,32):
	file_name='./imgs/frame'+str(i+1)+'.jpg'
	image = cv2.imread(file_name)
	overlay = image.copy()
	output = image.copy()
 	h = height - int(height*(view_arr_sorted.index(view_arr[i])*(0.99/32) ))

	# draw a red rectangle surrounding Adrian in the image
	# along with the text "PyImageSearch" at the top-left
	# corner
	cv2.rectangle(overlay, (0, h), (width, height), (255, 255, 0), -1)
	
	# apply the overlay
	cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
	cv2.putText(output, str(view_arr[i]), (width/2 - 100, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 3.0, (255, 255, 255), 3)	
	#cv2.putText(output,str(view_arr), (width/2,height/2), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
	cv2.imwrite("frame"+str(i)+".png", output)
	cv2.waitKey(0)
