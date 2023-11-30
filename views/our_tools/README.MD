
# tools.py

### color_area

Esta función encierra el área del color que determine la variable global area.

Parámetros:
* mask -> Máscara del rango del color
* frame -> Frame del video
* text -> Texto que se quiera mostrar como referencia del área
* area -> Area mínima que requiera encerrar
* color -> Los valores en RGB del color de la línea que encierre el área

Esta función no retorna nada ya que es una función constante para encerrar las áreas determinadas.

---
### contours

Genera los contornos de las áreas de la máscara.

Parámetros:
* mask -> Máscara del color dado

Estas función retorna el area de la máscara dada para un mejor uso de la detección.

---
### color_detection

Esta función detecta el color de las máscaras asignadas por los rangos default del archivo **colors.py**

Parámetros:
* Frame -> variable que contenga el frame leído
* Area -> variable que contenga el area mínima que se desea encerrar

Esta función no retorna nada ya que es una función constante que utiliza la función [color_area](https://github.com/AlbertoNM/color_detection_PyQt/tree/main/views/our_tools#color_area).

---
### make_roi

Esta función divide el ancho y la altura entre 4 para agarrar un cuadro central que ocupe una cuarta parte de la pantalla.

Parámetros:
* Frame -> Frame del video

Retorna las coodenadas de cada esquina del área de interés.

---
### make_rectangle

Esta función crea un rectángulo igual del área del ROI

Parámetros:
* Frame -> Frame del video

Estas función no retorna nada en concreto, solo crea un rectángulo en las coordenadas del ROI de cada frame.

---
### colors_pixels

Esta función junta todas las máscaras de los rangos del color que están por default en la carpeta colors.py

Parámetros:
* Frame -> Frame del video

Esta función retorna el frame solo con los pixeles de los colores defaults del archivo **colores.py**

---
### HSV_pixeles

Esta función utiliza las variables globales modificadas manualmente por los sliders HSV establenciendo un rango de color y detecta los pixeles dentro de éste.

Parámetros:
* Frame -> Frame del video
* low_H -> Rango mínimo de H
* low_S -> Rango mínimo de S
* low_V -> Rango mínimo de V
* up_H -> Rango máximo de H
* up_S -> Rango máximo de S
* up_V -> Rango máximo de V

Esta función retorna el frame solo con los pixeles del rango de color dado manualmente por los sliders de la interfaz.

---
### HSV_color

Esta función utiliza las variables globales modificadas manualmente por los sliders HSV y detecta el área del color dentro del rango establecido.

Parámetros:
* Frame -> Frame del video
* area -> Área de detección
* low_H -> Rango mínimo de H
* low_S -> Rango mínimo de S
* low_V -> Rango mínimo de V
* up_H -> Rango máximo de H
* up_S -> Rango máximo de S
* up_V -> Rango máximo de V

Esta función no retorna nada ya que es una función constante que utiliza la función [color_area](https://github.com/AlbertoNM/color_detection_PyQt/tree/main/views/our_tools#color_area).

---
### name_pixeles

Esta función utiliza un nombre de color y busca si existe entre los colores default establecidos en el archivo colors.py para detectar los pixeles dentro de los rangos default dependiendo el nombre que se le asigne.

Parámetros:
* Frame -> Frame del video
* color_name -> Nombre del color del dicionario

Esta función retorna el frame solo con los pixeles del rango de color escrito en el input del programa.

---
### name_color

Esta función utiliza un nombre de color entre los colores establecidos en el archivo colors.py para detectar el área dentro de los rangos establecidos dependiendo del nombre que se le asigne.

Parámetros:
* frame -> Frame del video
* area -> Área de detección
* color_name -> Nombre del color del dicionario

Esta función no retorna nada ya que es una función constante que utiliza la función [color_area](https://github.com/AlbertoNM/color_detection_PyQt/tree/main/views/our_tools#color_area).
