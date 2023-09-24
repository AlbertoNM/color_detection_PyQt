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
        "bajo": np.array([0, 208, 186]),
        "alto": np.array([15, 255, 255])
    },
    "amarillo": {
        "nombre": "Amarillo",
        "referencia": np.array([0, 255, 255]),
        "bajo": np.array([25, 100, 100]),
        "alto": np.array([35, 255, 255])
    },
    "verde": {
        "nombre": "Verde",
        "referencia": np.array([0, 255, 0]),
        "bajo": np.array([50, 80, 90]),
        "alto": np.array([68, 241, 231])
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

# colores = {
#     "rojo": {
#         "nombre": "Rojo",
#         "referencia": np.array([0, 0, 255]),
#         "bajo": np.array([0, 100, 100]),  # Rango de rojos más pequeño
#         "alto": np.array([3, 255, 255])
#     },
#     "naranja": {
#         "nombre": "Naranja",
#         "referencia": np.array([0, 128, 255]),
#         "bajo": np.array([10, 100, 100]),  # Rango de naranjas más pequeño
#         "alto": np.array([20, 255, 255])
#     },
#     "amarillo": {
#         "nombre": "Amarillo",
#         "referencia": np.array([0, 255, 255]),
#         "bajo": np.array([20, 100, 100]),  # Rango de amarillos más pequeño
#         "alto": np.array([30, 255, 255])
#     },
#     "verde": {
#         "nombre": "Verde",
#         "referencia": np.array([0, 255, 0]),
#         "bajo": np.array([40, 100, 100]),  # Rango de verdes más pequeño
#         "alto": np.array([60, 255, 255])
#     },
#     "azul": {
#         "nombre": "Azul",
#         "referencia": np.array([255, 0, 0]),
#         "bajo": np.array([100, 100, 100]),  # Rango de azules más pequeño
#         "alto": np.array([130, 255, 255])
#     },
#     "morado": {
#         "nombre": "Morado",
#         "referencia": np.array([255, 0, 127]),
#         "bajo": np.array([130, 100, 100]),  # Rango de morados más pequeño
#         "alto": np.array([160, 255, 255])
#     },
# }
