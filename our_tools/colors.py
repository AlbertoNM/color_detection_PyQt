import numpy as np

colores = {
    "rojo": {
        "nombre": "Rojo",
        "referencia": np.array([0, 0, 255]),
        "bajo": {
			"h": np.array([0, 100, 100]),
			"s":np.array([0, 20, 100]),
			"v": np.array([0, 100, 20])
            },
        "alto": {
			"h": np.array([3, 255, 255]),
			"s":np.array([3, 20, 255]),
			"v": np.array([3, 255, 20])
            },
    },
    "naranja": {
        "nombre": "Naranja",
        "referencia": np.array([0, 128, 255]),
        "bajo": {
			"h": np.array([10, 100, 100]),
			"s":np.array([10, 20, 100]),
			"v": np.array([10, 100, 20])
            },
        "alto": {
			"h": np.array([20, 255, 255]),
			"s":np.array([20, 20, 255]),
			"v": np.array([20, 255, 20])
            },
    },
    "amarillo": {
        "nombre": "Amarillo",
        "referencia": np.array([0, 255, 255]),
        "bajo": {
			"h": np.array([25, 100, 100]),
			"s":np.array([25, 20, 100]),
			"v": np.array([25, 100, 20])
            },
        "alto": {
			"h": np.array([35, 255, 255]),
			"s":np.array([35, 20, 255]),
			"v": np.array([35, 255, 20])
            },
    },
    "verde": {
        "nombre": "Verde",
        "referencia": np.array([0, 255, 0]),
        "bajo": {
			"h": np.array([45, 50, 50]),
			"s":np.array([45, 20, 50]),
			"v": np.array([45, 50, 20])
            },
        "alto": {
			"h": np.array([60, 255, 255]),
			"s":np.array([60, 20, 255]),
			"v": np.array([60, 255, 20])
            },
    },
    "azul": {
        "nombre": "Azul",
        "referencia": np.array([255, 0, 0]),
        "bajo": {
			"h": np.array([100, 50, 50]),
			"s": np.array([100, 20, 50]),
			"v": np.array([100, 50, 20])
		},
        "alto": {
			"h": np.array([125, 255, 255]),
			"s": np.array([125, 20, 255]),
			"v": np.array([125, 255, 20])
		},
    },
    "morado": {
        "nombre": "Morado",
        "referencia": np.array([255, 0, 127]),
        "bajo": {
			"h": np.array([130, 100, 100]),
			"s": np.array([130, 20, 100]),
			"v": np.array([130, 100, 20])
		},
        "alto": {
			"h": np.array([140, 255, 255]),
			"s": np.array([140, 20, 255]),
			"v": np.array([140, 255, 20])
		}
    },
}

