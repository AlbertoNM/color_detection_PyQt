import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from our_tools.tools import *

class MainApp(QMainWindow):

    def __init__(self, parent=None, *args):

        super(MainApp, self).__init__(parent=parent)
        self.setMinimumSize(990, 600)
        self.setStyleSheet("background:#212121")

	    # --------------------- Boxes ------------------------ #

        # Cuadro de video grande
        self.video = QLabel('', self)

        # Cuadro de video del ROI
        self.roi_video = QLabel('', self)

        # Botón de inicio
        self.start_button = QPushButton('start', self)
        self.start_button.clicked.connect(self.start)

        # Botón de stop
        self.stop_button = QPushButton('stop', self)
        self.stop_button.clicked.connect(self.stop)

        # Input de número
        self.input_area = QLineEdit("5000", self)
        self.input_area.setPlaceholderText("Área a detectar")
        self.input_area.setMaxLength(5)
        self.input_area.textChanged.connect(self.slider_value)

        # Slider
        self.slider_area = QSlider(self)
        self.slider_area.setMinimum(0)
        self.slider_area.setMaximum(10000)
        self.slider_area.setValue(5000)
        self.slider_area.valueChanged.connect(self.detection_area)

	    # ------------------- Estilos ----------------------- #

        # Cuadro de video grande
        self.video.setStyleSheet("background: #ffffff")
        self.video.setGeometry(10, 50, 640, 480)

        # Cuadro de video del ROI
        self.roi_video.setStyleSheet("background: #ffffff")
        self.roi_video.setGeometry(680, 50, 300, 300)

        # Botón de inicio
        self.start_button.setStyleSheet("background: #ffffff")
        self.start_button.setGeometry(10, 10, 75, 23)

        # Botón de stop
        self.stop_button.setStyleSheet("background: #ffffff")
        self.stop_button.setGeometry(100, 10, 75, 23)

        # Input de número
        self.input_area.setStyleSheet("background: #ffffff")
        self.input_area.setGeometry(680, 385, 100, 25)

        # Slider
        self.slider_area.setOrientation(Qt.Horizontal)
        self.slider_area.setGeometry(680, 360, 100, 20)

	# --------------------- FULL VIDEO ---------------------- #

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

class Work(QThread):

    Imageupd = pyqtSignal(QImage)
    Imageupd_roi = pyqtSignal(QImage)

    def run(self):

        global area
        area = 5000

        self.hilo = True

        cap = cv2.VideoCapture(0)

        while self.hilo:

            # Frame ventana grande

            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            make_rectangle(frame)
            roi = make_roi(frame)
            color_detection(roi, area)
            Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertir_QT = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
            pic = convertir_QT.scaled(640, 480, Qt.KeepAspectRatio)

            # Frame ventana chica (pixeles blancos del color)

            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            roi = make_roi(frame)
            Image_roi = colors_pixels(roi)
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
