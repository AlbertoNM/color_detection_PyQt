import cv2
import imutils
from our_tools.colors import colores

def color_area(mask, frame, text, area, color):

	"""sumary_line

	Keyword arguments:
	argument -- description
	Return: return_description
	"""

	if area > 4999:
		tamaño = 2
		grosor = 3
	elif area > 2500 and area < 5000:
		tamaño = 1
		grosor = 2
	else:
		tamaño = 0.5
		grosor = 1

	for c in mask:
		area1 = cv2.contourArea(c)
		if area1 > area:
			cv2.drawContours(frame, [cv2.convexHull(c)], 0, (int(color[0]), int(color[1]), int(color[2])), 2)
			M = cv2.moments(c)
			cx = int(M["m10"]/M["m00"])
			cy = int(M["m01"]/M["m00"])
			cv2.circle(frame, (cx, cy), 2, (int(color[0]), int(color[1]), int(color[2])), -1)
			# - putText(image, texto, org, font, fontScale, color, thickness, cv2.LINE_AA)
			cv2.putText(frame, text, (cx-20, cy-20), cv2.FONT_ITALIC, tamaño, (int(color[0]), int(color[1]), int(color[2])), grosor)

def contours(face):

    cnts = cv2.findContours(face, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return imutils.grab_contours(cnts)

def color_detection(frame:tuple, area:int) -> None:

    """
    ### Detectar el color del frame dado
	Parámetros:
	* frame -> variable que contenga el frame leído
 	* area -> variable que contenga el area mínima que se desea encerrar
	"""

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_mask = cv2.inRange(hsv, colores["rojo"]["bajo"], colores["rojo"]["alto"])
    orange_mask = cv2.inRange(hsv, colores["naranja"]["bajo"], colores["naranja"]["alto"])
    yellow_mask = cv2.inRange(hsv, colores["amarillo"]["bajo"], colores["amarillo"]["alto"])
    green_mask = cv2.inRange(hsv, colores["verde"]["bajo"], colores["verde"]["alto"])
    blue_mask = cv2.inRange(hsv, colores["azul"]["bajo"], colores["azul"]["alto"])
    purple_mask = cv2.inRange(hsv, colores["morado"]["bajo"], colores["morado"]["alto"])

    cntsR = contours(red_mask)
    cntsN = contours(orange_mask)
    cntsA = contours(yellow_mask)
    cntsV = contours(green_mask)
    cntsAz = contours(blue_mask)
    cntsM = contours(purple_mask)

    color_area(cntsR, frame, colores["rojo"]["nombre"], area, colores["rojo"]["referencia"])
    color_area(cntsN, frame, colores["naranja"]["nombre"], area, colores["naranja"]["referencia"])
    color_area(cntsA, frame, colores["amarillo"]["nombre"], area, colores["amarillo"]["referencia"])
    color_area(cntsV, frame, colores["verde"]["nombre"], area, colores["verde"]["referencia"])
    color_area(cntsAz, frame, colores["azul"]["nombre"], area, colores["azul"]["referencia"])
    color_area(cntsM, frame, colores["morado"]["nombre"], area, colores["morado"]["referencia"])

def make_roi(frame):

    roi = frame
    hn, wn, c = roi.shape
    x1, x2, y1, y2 = int(wn/4), int((wn/4)*3), int(hn/4), int((hn/4)*3)
    roi2=roi[:]

    return roi[y1:y2, x1:x2]

def make_rectangle(frame):
    rectangle = frame
    hn, wn, c = rectangle.shape
    x1, x2, y1, y2 = int(wn/4), int((wn/4)*3), int(hn/4), int((hn/4)*3)
    cv2.rectangle(rectangle, (x1-5, y1-5), (x2+5,y2+5), (0,255,0), 2)


def colors_pixels(frame):

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_mask = cv2.inRange(hsv, colores["rojo"]["bajo"], colores["rojo"]["alto"])
    orange_mask = cv2.inRange(hsv, colores["naranja"]["bajo"], colores["naranja"]["alto"])
    yellow_mask = cv2.inRange(hsv, colores["amarillo"]["bajo"], colores["amarillo"]["alto"])
    green_mask = cv2.inRange(hsv, colores["verde"]["bajo"], colores["verde"]["alto"])
    blue_mask = cv2.inRange(hsv, colores["azul"]["bajo"], colores["azul"]["alto"])
    purple_mask = cv2.inRange(hsv, colores["morado"]["bajo"], colores["morado"]["alto"])

    colors_frame = cv2.add(red_mask, orange_mask)
    colors_frame = cv2.add(colors_frame, yellow_mask)
    colors_frame = cv2.add(colors_frame, green_mask)
    colors_frame = cv2.add(colors_frame, blue_mask)
    colors_frame = cv2.add(colors_frame, purple_mask)

    return colors_frame
