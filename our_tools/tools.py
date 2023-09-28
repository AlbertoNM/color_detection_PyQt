import cv2
import numpy as np
import imutils
from our_tools.colors import colores

def color_area(mask:tuple, frame:tuple, text:str, area:int, color:tuple) -> None:

    """
	### Encerrar el área del color
	Esta función encierra el área del color que determine la variable global area

	Parámetros:
	* mask -> Máscara del rango del color
	* frame -> Frame del video
	* text -> Texto que se quiera mostrar como referencia del área
	* area -> Area mínima que requiera encerrar
	* color -> Los valores en RGB del color de la línea que encierre el área
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
            cv2.putText(frame, text, (cx-20, cy-20), cv2.FONT_ITALIC, tamaño, (int(color[0]), int(color[1]), int(color[2])), grosor)

def contours(maks:tuple) -> tuple:

    """
    ### Contornos
    Genera los contornos de las áreas de la máscara

	Parámetros:
	* mask -- Máscara del color dado
 	---
	Return: Áreas de la máscara
	"""
    cnts = cv2.findContours(maks, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return imutils.grab_contours(cnts)

def red_ranges(frame: tuple, color: str) -> tuple:

    """
	### Combinar rojos
	Esta función combina los dos rangos del color rojo dentro del espectro HSV
 	Parámetros:
	* Frame -> Frame del video
	* Color -> Rojo
	---
 	Return ->  Máscara de los dos rangos HSV del color rojo
	"""

    mask_1 = cv2.inRange(frame, colores[color]["bajo"]["1"], colores[color]["alto"]["1"])
    mask_2 = cv2.inRange(frame, colores[color]["bajo"]["2"], colores[color]["alto"]["2"])

    mask = cv2.add(mask_1, mask_2)

    return mask

def color_detection(frame:tuple, area:int) -> None:

    """
    ### Detectar el color del frame dado
    Esta función detecta el color de las máscaras asignadas por los rangos default del archivo colors.py

 	Parámetros:
	* Frame -> variable que contenga el frame leído
 	* Area -> variable que contenga el area mínima que se desea encerrar
	"""

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_mask = red_ranges(hsv, "rojo")
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

def make_roi(frame:tuple) -> tuple:

    """
    ### Crear ROI
	Esta función divide el ancho y la altura entre 4 para agarrar un cuadro central que ocupe una cuarta parte de la pantalla

	Parámetros:
	* Frame -> Frame del video
	---
 	Return -> Coordenadas para el ROI
	"""

    roi = frame
    hn, wn, c = roi.shape
    x1, x2, y1, y2 = int(wn/4), int((wn/4)*3), int(hn/4), int((hn/4)*3)
    roi2=roi[:]

    return roi[y1:y2, x1:x2]

def make_rectangle(frame:tuple) -> None:

    """
    ### Rectángulo
    Esta función crea un rectángulo igual del área del ROI

	Parámetros:
	* Frame -> Frame del video
	"""

    rectangle = frame
    hn, wn, c = rectangle.shape
    x1, x2, y1, y2 = int(wn/4), int((wn/4)*3), int(hn/4), int((hn/4)*3)
    cv2.rectangle(rectangle, (x1-5, y1-5), (x2+5,y2+5), (0,255,0), 2)

def colors_pixels(frame:tuple) -> tuple:

    """
    ### Piexeles del color
	Esta función junta todas las máscaras de los rangos del color que están por default en la carpeta colors.py

 	Parámetros:
	* Frame -> Frame del video
	---
 	Return -> Frames solo con los pixeles de los colores en default
	"""

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_mask = red_ranges(hsv, "rojo")
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

    color = cv2.bitwise_and(frame, frame, mask= colors_frame)

    return color

def HSV_pixeles(frame:tuple, low_H:int, low_S:int, low_V:int, up_H:int, up_S:int, up_V:int) -> tuple:

    """
    ### Piexeles del color
	Esta función utiliza las variables globales modificadas manualmente por los sliders HSV establenciendo un rango de color y detectar los pixeles dentro de éste

 	Parámetros:
	* Frame -> Frame del video
	---
 	Return -> Frames solo con los pixeles del rango de color dado
	"""

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array([low_H, low_S, low_V]), np.array([up_H, up_S, up_V]))
    color = cv2.bitwise_and(frame, frame, mask= mask)

    return color

def HSV_color(frame:tuple, area:int, low_H:int, low_S:int, low_V:int, up_H:int, up_S:int, up_V:int) -> None:

    """
    ### Area del color
	Esta función utiliza las variables globales modificadas manualmente por los sliders HSV y detecta el área del color dentro rango establecido

 	Parámetros:
	* Frame -> Frame del video
	"""

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array([low_H, low_S, low_V]), np.array([up_H, up_S, up_V]))

    contour = contours(mask)

    color_area(contour, frame, "color", area, colores["rojo"]["referencia"])

def name_pixeles(frame:tuple, color_name:str) -> tuple:

    """
    ### Piexeles del color
	Esta función utiliza un nombre de color y busca si existe entre los colores default establecidos en el archivo colors.py para detectar los pixeles dentro de los rangos default dependiendo el nombre que se le asigne

 	Parámetros:
	* Frame -> Frame del video
	---
 	Return -> Frames solo con los pixeles del rango de color dado
	"""

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if color_name == "rojo":
        mask = red_ranges(hsv, color_name)
    else:
        mask = cv2.inRange(hsv, np.array(colores[color_name]["bajo"]), np.array(colores[color_name]["alto"]))

    color = cv2.bitwise_and(frame, frame, mask= mask)

    return color

def name_color(frame:tuple, area:int, color_name:str) -> tuple:

    """
    ### Area del color
	Esta función utiliza un nombre de color y busca si existe entre los colores default establecidos en el archivo colors.py para detectar el área dentro de los rangos default dependiendo el nombre que se le asigne

 	Parámetros:
	* Frame -> Frame del video
	"""

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if color_name == "rojo":
        mask = red_ranges(hsv, color_name)
    else:
        mask = cv2.inRange(hsv, np.array(colores[color_name]["bajo"]), np.array(colores[color_name]["alto"]))

    contour = contours(mask)

    color_area(contour, frame, colores[color_name]["nombre"], area, colores[color_name]["referencia"])
