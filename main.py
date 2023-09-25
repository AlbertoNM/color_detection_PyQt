import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from our_tools.tools import *

class MainApp(QMainWindow):

    def __init__(self, parent=None, *args):

        super(MainApp, self).__init__(parent=parent)
        self.setMinimumSize(1300, 600)
        self.setStyleSheet("background:#212121")

	    #! --------------------- Boxes ------------------------ !#

        #* Cuadro de video grande
        self.video = QLabel('', self)

        #* Cuadro de video del ROI
        self.roi_video = QLabel('', self)

        #* Botón de inicio
        self.start_button = QPushButton('start', self)
        self.start_button.clicked.connect(self.start)

        #* Botón de stop
        self.stop_button = QPushButton('stop', self)
        self.stop_button.clicked.connect(self.stop)

        #* Input de número
        self.input_area = QLineEdit("5000", self)
        self.input_area.setPlaceholderText("Área a detectar")
        self.input_area.setMaxLength(5)
        self.input_area.textChanged.connect(self.slider_value)

        #* Slider
        self.slider_area = QSlider(self)
        self.slider_area.setMinimum(0)
        self.slider_area.setMaximum(10000)
        self.slider_area.setValue(5000)
        self.slider_area.valueChanged.connect(self.detection_area)

        #* Check box
        self.check_box = QCheckBox("HSV",self)

        #* Sliders HSV min
        self.labelMin_HSV = QLabel("HSV min", self)
        self.labelMin_H = QLabel("H", self)
        self.sliderMin_H = QSlider(self)
        self.sliderMin_H.setMinimum(0)
        self.sliderMin_H.setMaximum(180)
        self.sliderMin_H.valueChanged.connect(self.spinMin_H_value)
        self.spinMin_H = QSpinBox(self)
        self.spinMin_H.setRange(0, 180)
        self.spinMin_H.valueChanged.connect(self.sliderMin_H_value)

        self.labelMin_S = QLabel("S", self)
        self.sliderMin_S = QSlider(self)
        self.sliderMin_S.setMinimum(0)
        self.sliderMin_S.setMaximum(255)
        self.sliderMin_S.valueChanged.connect(self.spinMin_S_value)
        self.spinMin_S = QSpinBox(self)
        self.spinMin_S.setRange(0, 255)
        self.spinMin_S.valueChanged.connect(self.sliderMin_S_value)

        self.labelMin_V = QLabel("V", self)
        self.sliderMin_V = QSlider(self)
        self.sliderMin_V.setMinimum(0)
        self.sliderMin_V.setMaximum(255)
        self.sliderMin_V.valueChanged.connect(self.spinMin_V_value)
        self.spinMin_V = QSpinBox(self)
        self.spinMin_V.setRange(0, 255)
        self.spinMin_V.valueChanged.connect(self.sliderMin_V_value)

        #* Sliders HSV max
        self.labelMax_HSV = QLabel("HSV max", self)
        self.labelMax_H = QLabel("H", self)
        self.sliderMax_H = QSlider(self)
        self.sliderMax_H.setMinimum(0)
        self.sliderMax_H.setMaximum(180)
        self.sliderMax_H.valueChanged.connect(self.spinMax_H_value)
        self.spinMax_H = QSpinBox(self)
        self.spinMax_H.setRange(0, 180)
        self.spinMax_H.valueChanged.connect(self.sliderMax_H_value)

        self.labelMax_S = QLabel("S", self)
        self.sliderMax_S = QSlider(self)
        self.sliderMax_S.setMinimum(0)
        self.sliderMax_S.setMaximum(255)
        self.sliderMax_S.valueChanged.connect(self.spinMax_S_value)
        self.spinMax_S = QSpinBox(self)
        self.spinMax_S.setRange(0, 255)
        self.spinMax_S.valueChanged.connect(self.sliderMax_S_value)

        self.labelMax_V = QLabel("V", self)
        self.sliderMax_V = QSlider(self)
        self.sliderMax_V.setMinimum(0)
        self.sliderMax_V.setMaximum(255)
        self.sliderMax_V.valueChanged.connect(self.spinMax_V_value)
        self.spinMax_V = QSpinBox(self)
        self.spinMax_V.setRange(0, 255)
        self.spinMax_V.valueChanged.connect(self.sliderMax_V_value)

	    #! ------------------- Estilos ----------------------- !#

        #* Cuadro de video grande
        self.video.setStyleSheet("background: #ffffff")
        self.video.setGeometry(10, 50, 640, 480)

        #* Cuadro de video del ROI
        self.roi_video.setStyleSheet("background: #ffffff")
        self.roi_video.setGeometry(680, 50, 300, 300)

        #* Botón de inicio
        self.start_button.setStyleSheet("background: #ffffff")
        self.start_button.setGeometry(10, 10, 75, 23)

        #* Botón de stop
        self.stop_button.setStyleSheet("background: #ffffff")
        self.stop_button.setGeometry(100, 10, 75, 23)

        #* Input de número
        self.input_area.setStyleSheet("background: #ffffff")
        self.input_area.setGeometry(840, 360, 140, 25)

        #* Slider
        self.slider_area.setOrientation(Qt.Horizontal)
        self.slider_area.setGeometry(680, 360, 140, 25)

        #* Check box
        self.check_box.setStyleSheet("color: #ffffff")
        self.check_box.setGeometry(680, 400, 140, 20)

        #* SLiders HSV min
        self.labelMin_HSV.setStyleSheet("color: #ffffff")
        self.labelMin_HSV.setGeometry(1000, 20, 50, 20)

        self.labelMin_H.setStyleSheet("color: #ffffff")
        self.labelMin_H.setGeometry(1000, 50, 20, 20)

        self.sliderMin_H.setOrientation(Qt.Horizontal)
        self.sliderMin_H.setGeometry(1020, 50, 140, 20)
        self.spinMin_H.setStyleSheet("background: #ffffff")
        self.spinMin_H.setGeometry(1180, 50, 45, 20)

        self.labelMin_S.setStyleSheet("color: #ffffff")
        self.labelMin_S.setGeometry(1000, 90, 20, 20)

        self.sliderMin_S.setOrientation(Qt.Horizontal)
        self.sliderMin_S.setGeometry(1020, 90, 140, 20)
        self.spinMin_S.setStyleSheet("background: #ffffff")
        self.spinMin_S.setGeometry(1180, 90, 45, 20)

        self.labelMin_V.setStyleSheet("color: #ffffff")
        self.labelMin_V.setGeometry(1000, 130, 20, 20)

        self.sliderMin_V.setOrientation(Qt.Horizontal)
        self.sliderMin_V.setGeometry(1020, 130, 140, 20)
        self.spinMin_V.setStyleSheet("background: #ffffff")
        self.spinMin_V.setGeometry(1180, 130, 45, 20)

        #* SLiders HSV max
        self.labelMax_HSV.setStyleSheet("color: #ffffff")
        self.labelMax_HSV.setGeometry(1000, 170, 50, 20)

        self.labelMax_H.setStyleSheet("color: #ffffff")
        self.labelMax_H.setGeometry(1000, 200, 20, 20)

        self.sliderMax_H.setOrientation(Qt.Horizontal)
        self.sliderMax_H.setGeometry(1020, 200, 140, 20)
        self.spinMax_H.setStyleSheet("background: #ffffff")
        self.spinMax_H.setGeometry(1180, 200, 45, 20)

        self.labelMax_S.setStyleSheet("color: #ffffff")
        self.labelMax_S.setGeometry(1000, 240, 20, 20)

        self.sliderMax_S.setOrientation(Qt.Horizontal)
        self.sliderMax_S.setGeometry(1020, 240, 140, 20)
        self.spinMax_S.setStyleSheet("background: #ffffff")
        self.spinMax_S.setGeometry(1180, 240, 45, 20)

        self.labelMax_V.setStyleSheet("color: #ffffff")
        self.labelMax_V.setGeometry(1000, 280, 20, 20)

        self.sliderMax_V.setOrientation(Qt.Horizontal)
        self.sliderMax_V.setGeometry(1020, 280, 140, 20)
        self.spinMax_V.setStyleSheet("background: #ffffff")
        self.spinMax_V.setGeometry(1180, 280, 45, 20)

	#! --------------------- FULL VIDEO ---------------------- !#

    def start(self):
        self.FullVideo = Work()
        self.FullVideo.Imageupd.connect(self.Imageupd_slot)
        self.FullVideo.Imageupd_roi.connect(self.Imageupd_slot2)
        self.FullVideo.start()

    def Imageupd_slot(self, Image):
        self.video.setPixmap(QPixmap.fromImage(Image))

    def Imageupd_slot2(self, Image):
        self.roi_video.setPixmap(QPixmap.fromImage(Image))

    def stop(self):
        self.video.clear()
        self.FullVideo.stop()

	#! ------------------ Slider e input -------------------- !#

    def detection_area(self, value):
        self.input_area.setText(str(value))
        global area
        area = value

    def slider_value(self):
        try:
            self.slider_area.setValue(int(self.input_area.text()))
            global area
            area = int(self.input_area.text())
        except:
            self.input_area.setText(str(1))
            area = 1

	#! ----------------- Sliders HSV min ------------------- !#

    def sliderMin_H_value(self, value):
        self.sliderMin_H.setValue(value)
        global low_H
        low_H = value

    def sliderMin_S_value(self, value):
        self.sliderMin_S.setValue(value)
        global low_S
        low_S = value

    def sliderMin_V_value(self, value):
        self.sliderMin_V.setValue(value)
        global low_V
        low_V = value

    def spinMin_H_value(self, value):
        self.spinMin_H.setValue(value)
        global low_H
        low_H = value

    def spinMin_S_value(self, value):
        self.spinMin_S.setValue(value)
        global low_S
        low_S = value

    def spinMin_V_value(self, value):
        self.spinMin_V.setValue(value)
        global low_V
        low_V = value

	#! ----------------- Sliders HSV max ------------------- !#

    def sliderMax_H_value(self, value):
        self.sliderMax_H.setValue(value)
        global up_H
        up_H = value

    def sliderMax_S_value(self, value):
        self.sliderMax_S.setValue(value)
        global up_S
        up_S = value

    def sliderMax_V_value(self, value):
        self.sliderMax_V.setValue(value)
        global up_V
        up_V = value

    def spinMax_H_value(self, value):
        self.spinMax_H.setValue(value)
        global up_H
        up_H = value

    def spinMax_S_value(self, value):
        self.spinMax_S.setValue(value)
        global up_S
        up_S = value

    def spinMax_V_value(self, value):
        self.spinMax_V.setValue(value)
        global up_V
        up_V = value

class Work(QThread):

    Imageupd = pyqtSignal(QImage)
    Imageupd_roi = pyqtSignal(QImage)

    def run(self):

        # Variable global del área mínima para detectar color
        global area
        area = 5000

        # Variables globales de HSV
        global low_H, low_S, low_V, up_H, up_S, up_V
        low_H = 0
        low_S = 0
        low_V = 0

        up_H = 0
        up_S = 0
        up_V = 0

        self.hilo = True

        cap = cv2.VideoCapture(0)

        while self.hilo:

            # Frame ventana grande

            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            make_rectangle(frame)
            roi = make_roi(frame)
            # color_detection(roi, area)
            prueba_color(roi, area, low_H, low_S, low_V, up_H, up_S, up_V)

            Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertir_QT = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
            pic = convertir_QT.scaled(640, 480, Qt.KeepAspectRatio)

            # Frame ventana chica (pixeles del rango de color)

            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            roi = make_roi(frame)
            # Image_roi = colors_pixels(roi)
            Image_roi = prueba_pixeles(roi, low_H, low_S, low_V, up_H, up_S, up_V)

            Image_roi = cv2.cvtColor(Image_roi, cv2.COLOR_BGR2RGB)
            cvt2QtFormat = QImage(Image_roi.data, Image_roi.shape[1], Image_roi.shape[0], QImage.Format_RGB888)
            pic_roi = cvt2QtFormat.scaled(300, 300, Qt.KeepAspectRatio)

            # Emit frames

            if ret:
                self.Imageupd.emit(pic)
                self.Imageupd_roi.emit(pic_roi)

    def stop(self):
        self.hilo = False
        self.quit()

if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()
