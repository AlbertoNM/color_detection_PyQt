import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame, (640, 480))
    
    roi = frame
    hn, wn, c = roi.shape
    #print("Resize roi", hn,wn)
    # ------------make roi--------------------
    x1, x2, y1, y2 = int(wn/3), int((wn/3)*2), int(hn/3)*2-50, hn
    #print(x1, x2, y1, y2)
    cv2.rectangle(roi, (x1, y1), (x2,y2), (0,255,0), 2)
    roi2=roi[:]
    roi = roi[y1:y2, x1:x2]
    
    # im = cv2.selectROI(frame)
    # roi = frame[im[1]:im[1]+im[3], im[0]:im[0]+im[2]]
    # cv2.rectangle(frame, (im[1], im[1]+im[3]), (im[0], im[0]+im[2]), (0,255,0), 2)
    cv2.imshow("Video", frame)
    cv2.imshow("Roi", roi)
    if cv2.waitKey(1) & 0xFF == ord('q'):break
    
cap.release()

# --------------------------------------------------------------- #



# --------------------------------------------------------------- #

# im = cv2.imread("./foto.png")

# roi = cv2.selectROI(im)

# print(roi)
# print(roi[1] + roi[3], roi[0]+roi[2])

# # (657, 919, 262, 444)

# im_cropped = im[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]

# cv2.imshow("Cropped Image", im_cropped)


#cv2.waitKey(1)

cv2.destroyAllWindows()