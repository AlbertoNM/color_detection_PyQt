# Color detection with PyQt
Creating an interface for color detection

## Requirements:

* imutils==0.5.4
* numpy==1.25.2
* opencv-python==4.8.0.76
* PyQt5==5.15.9
* PyQt5-Qt5==5.15.2
* PyQt5-sip==12.12.2

## Ambiente virtual

Si ya tiene anaconda solo necesitará un ambiente con las librerías que se mostraron con anterioridad; de no ser así, puede iniciarlizar un ambiente virtual desde la terminal:

```Shell
python3 -m venv venv
```

Después habrá que iniciar el ambiente virtual; esto dependerá de si usas unix o windows

Unix:

```Shell
source venv/bin/activate
```

Windows:

```Shell
.\venv\Scripts\activate
```
Una vez iniciado el ambiente virtual, debería salirte en la terminal: (venv), arriba o atrás de la ruta de usuario; para instalar las librerías deberá escribir lo siguiente:

```Shell
pip install -r requirements.txt
```

Una vez instaladas las librerías, podrá iniciar la aplicación corriendo el archivo main.py del repositorio

```Shell
python main.py
```

