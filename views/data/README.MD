
# colors.py

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

# datos.py

### Area

Valor default

```Python
area = 5000
```

`area` es la variable que se utiliza para determinar el área de detección del color establecido, supongamos que tenemos una imagen de 10 x 10 pixeles, y solo queremos detectar un color que tenga un área de 4, el algorítmo solo detectará los 4 pixeles que estén juntos con el color o rango de color dado.

Si tenemos pixeles del color dado pero todos están separados, el algoritmo no lo detectará porque requiere que estén juntos, solo si bajamos el área a 1 detectará los pixeles individuales.

### HSV Values

Valores default:

```Python
low_H = 0
low_S = 0
low_V = 0
up_H = 179
up_S = 255
up_V = 255
```

Las variables `low_H`, `low_S`, `low_V`, `up_H`, `up_S`, `up_V` son las que guardan los valores del color HSV.

> Estos rangos de color se explican a detalle en la imagen de ayuda del programa o en la [documentación inicial](https://github.com/AlbertoNM/color_detection_PyQt#images)

Las variables "low" son las del rango mínimo del color, y las "up" las del rango máximo del color.
