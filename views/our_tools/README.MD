## colors

Aquí se encuentra un diccionario con rangos de colores por default. Los colores son:

* Rojo
* Naranja
* Amarillo
* Verde
* Azul
* Morado

### Estructura

La estructura de de cada color está dada por 4 llaves.

```Python

# Los datos de los rangos están en un conjunto hecho con numpy
# Por lo que se importa numpy
import numpy as np

# Variable del diccionario de colores
colores = {
    # Color
    "verde": {
        # Nombre del color
        "nombre": "Verde",
        # RGB del color
        "referencia": np.array([0, 255, 0]),
        # Rango HSV más bajo
        "bajo": np.array([35, 45, 45]),
        # Rango HSV más alto
        "alto": np.array([60, 255, 255]),
    },
}
```

> Existen dos diccionarios del color rojo ya que éste tiene un espacio de color en ambos extremos del [espectro](https://i.stack.imgur.com/gyuw4.png).


> [(2020). *Color Filtering/Segmentation/Detection – HSV*. Blog at Wordpress.com](https://cvexplained.wordpress.com/2020/04/28/color-detection-hsv/)

### Usos

La variable `colores` contiene el diccionario de los colores; como podemos observar, cada color también es un diccionario, que contiene su nombre, una referencia en RGB y sus rangos altos y bajos del espectro HSV.

El nombre y referencia son utilizados para fines referenciales valga la redundancia, ya que el programa al hacer una detección utiliza el nombre y su color de referencia RGB para resaltar las áreas detectadas.

## tools

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
