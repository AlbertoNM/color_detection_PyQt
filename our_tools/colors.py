import numpy as np

colores = {
    "rojo": {
        "nombre": "Rojo",
        "bajo": np.array([0, 100, 100]),  # Rango de rojos más pequeño
        "alto": np.array([5, 255, 255])
    },
    "naranja": {
        "nombre": "Naranja",
        "bajo": np.array([10, 100, 100]),  # Rango de naranjas más pequeño
        "alto": np.array([15, 255, 255])
    },
    "amarillo": {
        "nombre": "Amarillo",
        "bajo": np.array([20, 100, 100]),  # Rango de amarillos más pequeño
        "alto": np.array([25, 255, 255])
    },
    "verde": {
        "nombre": "Verde",
        "bajo": np.array([40, 100, 100]),  # Rango de verdes más pequeño
        "alto": np.array([50, 255, 255])
    },
    "azul": {
        "nombre": "Azul",
        "bajo": np.array([100, 100, 100]),  # Rango de azules más pequeño
        "alto": np.array([110, 255, 255])
    },
    "morado": {
        "nombre": "Morado",
        "bajo": np.array([130, 100, 100]),  # Rango de morados más pequeño
        "alto": np.array([140, 255, 255])
    },
}
