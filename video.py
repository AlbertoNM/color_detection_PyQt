import cv2
from our_tools.tools import *
from our_tools.colors import *
    
cap = cv2.VideoCapture(0)

def roi_color(cap):
    
    while True:
        
        ret, frame = cap.read()
        frame = cv2.resize(frame, (640, 480))
        
        # --------------------------------------------------------------- #
        
        roi = frame
        hn, wn, c = roi.shape
        # print("Resize roi", hn,wn)
        # ------------make roi--------------------
        x1, x2, y1, y2 = int(wn/3), int((wn/3)*2), int(hn/3)*2-50, hn
        # print(x1, x2, y1, y2)
        cv2.rectangle(roi, (x1-5, y1-5), (x2+5,y2), (0,255,0), 3)
        roi2=roi[:]
        roi = roi[y1:y2, x1:x2]
        
        # --------------------------------------------------------------- #
        
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        
        face1 = cv2.inRange(hsv, colores["rojo"]["bajo"], colores["rojo"]["alto"])
        face2 = cv2.inRange(hsv, colores["naranja"]["bajo"], colores["naranja"]["alto"])
        face3 = cv2.inRange(hsv, colores["amarillo"]["bajo"], colores["amarillo"]["alto"])
        face4 = cv2.inRange(hsv, colores["verde"]["bajo"], colores["verde"]["alto"])
        face5 = cv2.inRange(hsv, colores["azul"]["bajo"], colores["azul"]["alto"])
        face6 = cv2.inRange(hsv, colores["morado"]["bajo"], colores["morado"]["alto"])

        cntsR = contours(face1)
        cntsN = contours(face2)
        cntsA = contours(face3)
        cntsV = contours(face4)
        cntsAz = contours(face5)
        cntsM = contours(face6)

        color(cntsR, roi, colores["rojo"]["nombre"])
        color(cntsN, roi, colores["naranja"]["nombre"])
        color(cntsA, roi, colores["amarillo"]["nombre"])
        color(cntsV, roi, colores["verde"]["nombre"])
        color(cntsAz, roi, colores["azul"]["nombre"])
        color(cntsM, roi, colores["morado"]["nombre"])

        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
roi_color(cap)
