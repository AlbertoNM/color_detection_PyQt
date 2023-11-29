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


