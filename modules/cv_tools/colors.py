import numpy as np

colores = {
    "rojo": {
        "nombre": "Rojo",
        "referencia": np.array([0, 0, 255]),
        "bajo": {"1": np.array([0, 100, 100]),"2": np.array([175, 100, 100])},
        "alto": {"1": np.array([3, 255, 255]),"2": np.array([180, 255, 255])},
    },
    "naranja": {
        "nombre": "Naranja",
        "referencia": np.array([0, 128, 255]),
        "bajo": np.array([4, 170, 110]),
        "alto": np.array([15, 255, 255]),
    },
    "amarillo": {
        "nombre": "Amarillo",
        "referencia": np.array([0, 255, 255]),
        "bajo": np.array([25, 45, 45]),
        "alto": np.array([35, 255, 255]),
    },
    "verde": {
        "nombre": "Verde",
        "referencia": np.array([0, 255, 0]),
        "bajo": np.array([35, 45, 45]),
        "alto": np.array([60, 255, 255]),
    },
    "azul": {
        "nombre": "Azul",
        "referencia": np.array([255, 0, 0]),
        "bajo": np.array([80, 50, 0]),
        "alto": np.array([125, 255, 255]),
    },
    "morado": {
        "nombre": "Morado",
        "referencia": np.array([255, 0, 127]),
        "bajo": np.array([130, 100, 100]),
        "alto": np.array([140, 255, 255]),
		}
}
