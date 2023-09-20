import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from our_tools.tools import *

class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp, self).__init__(parent=parent)
        self.setMinimumSize(1200, 600)
        self.setStyleSheet("background:#212121")

        # boxes #
        self.video = QLabel('', self)
        self.roi_video = QLabel('', self)
        self.start_button = QPushButton('start', self)
        self.start_button.clicked.connect(self.start)
        self.stop_button = QPushButton('stop', self)
        self.stop_button.clicked.connect(self.stop)

        # estilos #
        self.video.setStyleSheet("background: #ffffff")
        self.video.setGeometry(10, 10, 640, 480)
        self.roi_video.setStyleSheet("background: #ffffff")
        self.roi_video.setGeometry(680, 10, 300, 300)
        self.start_button.setStyleSheet("background: #ffffff")
        self.start_button.setGeometry(10, 500, 75, 23)
        self.roi_video.setGeometry(680, 10, 300, 300)
        self.stop_button.setStyleSheet("background: #ffffff")
        self.stop_button.setGeometry(100, 500, 75, 23)

	# ----------------------FULL VIDEO----------------------- #

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

class Work(QThread):

    Imageupd = pyqtSignal(QImage)
    Imageupd_roi = pyqtSignal(QImage)

    def run(self):

        self.hilo = True

        cap = cv2.VideoCapture(0)

        while self.hilo:

            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            make_rectangle(frame)
            roi = make_roi(frame)
            color_detection(roi)
            Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertir_QT = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
            pic = convertir_QT.scaled(640, 480, Qt.KeepAspectRatio)

            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            roi = make_roi(frame)
            Image_roi = colors_pixels(roi)
            Image_roi = cv2.cvtColor(Image_roi, cv2.COLOR_BGR2RGB)
            # flip_roi = cv2.flip(Image_roi, 1)
            cvt2QtFormat = QImage(Image_roi.data, Image_roi.shape[1], Image_roi.shape[0], QImage.Format_RGB888)
            pic_roi = cvt2QtFormat.scaled(300, 300, Qt.KeepAspectRatio)

            # Image = colors_pixels(frame)
            # Image = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
            # flip = cv2.flip(Image, 1)
            # convertir_QT = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
            # pic = convertir_QT.scaled(640, 480, Qt.KeepAspectRatio)

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
