import cv2
import numpy as np
from matplotlib import pyplot as plt
cap = cv2.VideoCapture('vid.mp4')
frame_count = 0
img = cv2.imread('home.jpg')
hist_prev = cv2.calcHist([img], [0, 1, 2], None, [32, 32, 32],
	[0, 256, 0, 256, 0, 256])
cv2.normalize(hist_prev, hist_prev)
hist_prev = hist_prev.flatten()

frame_arr = []
d_arr = []

while(frame_count < 2576):

	#img = cv2.imread('home.jpg')
	ret, img = cap.read()
	#hsv = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	hist = cv2.calcHist([img], [0, 1, 2], None, [32, 32, 32],[0, 256, 0, 256, 0, 256])
	cv2.normalize(hist, hist)
	hist = hist.flatten()

	#hist = hist.flatten()
	frame_count = frame_count+1
	frame_arr.append(frame_count);
	
	d = cv2.compareHist(hist_prev,hist,1)
	d_arr.append(d)

	print str(frame_count) + "-->"+ str(d)
	hist_prev = hist
	#hist = cv2.calcHist([hsv],[0,1],None, [180,256], [0,180,0,256])
	#plt.imshow(hist, interpolation = 'nearest')
	#plt.show()
	#print hist
	cv2.imshow('frame',img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
            break

plt.plot(frame_arr,d_arr)
plt.show()
cap.release()
cv2.destroyAllWindows()