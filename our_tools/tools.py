import cv2
import imutils
from our_tools.colors import colores

def color(mask, frame, text):
    
    for c in mask:
        area1 = cv2.contourArea(c)
        if area1 > 5000:
            cv2.drawContours(frame, [cv2.convexHull(c)], 0, (255, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, text, (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255,255,255),1)
            

def contours(face):
    cnts = cv2.findContours(face, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return imutils.grab_contours(cnts)

def roi_color(frame):
    
    # ------------make roi------------------------------------------- #
        
    roi = frame
    hn, wn, c = roi.shape
    # print("Resize roi", hn,wn)
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