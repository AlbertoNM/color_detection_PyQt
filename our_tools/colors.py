import numpy as np

colores = {
    "rojo": {
        "nombre": "Rojo",
        "referencia": np.array([0, 0, 255]),
        "bajo": np.array([0, 100, 100]),
        "alto": np.array([2, 255, 255])
    },
    "naranja": {
        "nombre": "Naranja",
        "referencia": np.array([0, 128, 255]),
        "bajo": np.array([10, 100, 100]),
        "alto": np.array([15, 255, 255])
    },
    "amarillo": {
        "nombre": "Amarillo",
        "referencia": np.array([0, 255, 255]),
        "bajo": np.array([20, 100, 100]),
        "alto": np.array([25, 255, 255])
    },
    "verde": {
        "nombre": "Verde",
        "referencia": np.array([0, 255, 0]),
        "bajo": np.array([40, 100, 100]),
        "alto": np.array([50, 255, 255])
    },
    "azul": {
        "nombre": "Azul",
        "referencia": np.array([255, 0, 0]),
        "bajo": np.array([100, 100, 100]),
        "alto": np.array([110, 255, 255])
    },
    "morado": {
        "nombre": "Morado",
        "referencia": np.array([255, 0, 127]),
        "bajo": np.array([130, 100, 100]),
        "alto": np.array([140, 255, 255])
    },
}
