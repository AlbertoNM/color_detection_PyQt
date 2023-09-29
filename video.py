import cv2
from our_tools.tools import *
from our_tools.colors import *

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    frame = cv2.resize(frame, (640, 480))

    rojoBajo = np.array([0, 50, 50])
    rojoAlto = np.array([3, 255, 255])
    maskRed = cv2.inRange(hsv, rojoBajo,rojoAlto)

    # mask = cv2.bitwise_and(frame, frame, mask= maskRed)
    # colors_frame = colors_pixels(frame)

    # cv2.imshow("Mask", mask)
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): break
