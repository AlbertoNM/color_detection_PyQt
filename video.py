import cv2
from our_tools.tools import *
from our_tools.colors import *

cap = cv2.VideoCapture(0)

while True:

	ret, frame = cap.read()
	frame = cv2.resize(frame, (640, 480))

	# ---------------------------- ROI ------------------------------ #

	roi = make_roi(frame)

	# --------------------------------------------------------------- #

	roi_color(roi)

	cv2.imshow("Video", frame)
	cv2.imshow("Roi Video", roi)

	if cv2.waitKey(1) & 0xFF == ord('q'): break
