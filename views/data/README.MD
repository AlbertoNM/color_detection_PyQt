### area

Valor default

```Python
area = 5000
```

Area es la variable que se utiliza para determinar el área de detección del color establecido, supongamos que tenemos una imagen de 10 x 10 pixeles, y solo queremos detectar un color que tenga un área de 4, el algorítmo solo detectará los 4 pixeles que estén juntos con el color o rango de color dado.

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
