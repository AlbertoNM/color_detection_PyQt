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
    """Detectar el color del área dada

	Keyword arguments:
	frame -- variable que contenga el frame leído
	Return: area en tiempo real de los colores
	"""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
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

    color(cntsR, frame, colores["rojo"]["nombre"])
    color(cntsN, frame, colores["naranja"]["nombre"])
    color(cntsA, frame, colores["amarillo"]["nombre"])
    color(cntsV, frame, colores["verde"]["nombre"])
    color(cntsAz, frame, colores["azul"]["nombre"])
    color(cntsM, frame, colores["morado"]["nombre"])

def make_roi(frame):

    roi = frame
    hn, wn, c = roi.shape
    x1, x2, y1, y2 = int(wn/4), int((wn/4)*3), int(hn/4), int((hn/4)*3)
    # cv2.rectangle(roi, (x1, y1), (x2,y2), (0,255,0), 1)
    roi2=roi[:]

    return roi[y1:y2, x1:x2]
