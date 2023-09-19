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
        self.video = QLabel('video', self)
        self.roi_video = QLabel('Roi', self)
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
        self.stop_button.setStyleSheet("background: #ffffff")
        self.stop_button.setGeometry(100, 500, 75, 23)
    
    def start(self):
        self.Work = Work()
        self.Work.start()
        self.Work.Imageupd.connect(self.Imageupd_slot)
    
    def Imageupd_slot(self, Image):
        self.video.setPixmap(QPixmap.fromImage(Image))
    
    def stop(self):
        self.video.clear()
        self.Work.stop()
        

class Work(QThread):
    
    Imageupd = pyqtSignal(QImage)
    Imageupd_roi = pyqtSignal(QImage)
    
    def run(self):
        
        self.hilo_corriendo = True
        
        cap = cv2.VideoCapture(0)
        while self.hilo_corriendo:
        
            ret, frame = cap.read()
            roi_color(frame)
        
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                flip = cv2.flip(Image, 1)
                convertir_QT = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
                pic = convertir_QT.scaled(640, 480, Qt.KeepAspectRatio)
                self.Imageupd.emit(pic)
    
    # def run(self):
    #     self.hilo_corriendo2 = True
    #     cap = cv2.VideoCapture(0)
    #     while self.hilo_corriendo2:
    #         ret, frame = cap.read()
    #         if ret:
    #             Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #             flip = cv2.flip(Image, 1)
    #             convertir_QT = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
    #             pic = convertir_QT.scaled(300, 300, Qt.KeepAspectRatio)
    #             self.Imageupd_2.emit(pic)
    
    def stop(self):
        self.hilo_corriendo = False
        self.hilo_corriendo2 = False
        self.quit()


if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()