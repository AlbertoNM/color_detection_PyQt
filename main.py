from ui import Ui_MainWindow
from PyQt5.QtCore import QObject
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from our_tools.tools import *
from our_tools.colors import colores

area = 5000
low_H, low_S, low_V, up_H, up_S, up_V = 0,0,0,179,255,255
color_name = "rojo"

class MainApp(QMainWindow):

    def __init__(self, parent=None, *args):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

	    #! --------------------- Boxes ------------------------ !#

        #* Botón de inicio
        self.ui.start_button.clicked.connect(self.start)

        #* Botón de stop
        self.ui.stop_button.clicked.connect(self.stop)

        #* Input de número
        self.ui.input_area.textChanged.connect(self.slider_value)

        #* Input de color
        self.ui.type_input.returnPressed.connect(self.color_name_change)

        #* Slider
        self.ui.slider_area.valueChanged.connect(self.detection_area)

        #* Sliders HSV min
        self.ui.sliderMin_H.valueChanged.connect(self.spinMin_H_value)
        self.ui.spinMin_H.valueChanged.connect(self.sliderMin_H_value)

        self.ui.sliderMin_S.valueChanged.connect(self.spinMin_S_value)
        self.ui.spinMin_S.valueChanged.connect(self.sliderMin_S_value)

        self.ui.sliderMin_V.valueChanged.connect(self.spinMin_V_value)
        self.ui.spinMin_V.valueChanged.connect(self.sliderMin_V_value)

        #* Sliders HSV max
        self.ui.sliderMax_H.valueChanged.connect(self.spinMax_H_value)
        self.ui.spinMax_H.valueChanged.connect(self.sliderMax_H_value)

        self.ui.sliderMax_S.valueChanged.connect(self.spinMax_S_value)
        self.ui.spinMax_S.valueChanged.connect(self.sliderMax_S_value)

        self.ui.sliderMax_V.valueChanged.connect(self.spinMax_V_value)
        self.ui.spinMax_V.valueChanged.connect(self.sliderMax_V_value)

	#! --------------------- FULL VIDEO ---------------------- !#

    def start(self):

        self.Work = Work()
        self.Work.Imageupd.connect(self.Imageupd_slot)
        self.Work.start()

    def cv_to_qt(self, Image, widht = 640, height = 480):

        pic = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
        convertir_QT = QImage(pic.data, pic.shape[1], pic.shape[0], QImage.Format_RGB888)
        frame = convertir_QT.scaled(widht, height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(frame)

    @pyqtSlot(np.ndarray)
    def Imageupd_slot(self, Image):

        # global low_H, low_S, low_V, up_H, up_S, up_V, area

        if self.ui.HSV_checkBox.isChecked() == True and self.ui.type_checkBox.isChecked() == False:

            frame = HSV_pixeles(Image, low_H, low_S, low_S, up_H, up_S, up_V)
            frame = self.cv_to_qt(frame, 300, 300)
            self.ui.roi_video.setPixmap(frame)

            roi = make_roi(Image)
            HSV_color(roi, area, low_H, low_S, low_V, up_H, up_S, up_V)

        if self.ui.type_checkBox.isChecked() == True and self.ui.HSV_checkBox.isChecked() == False:

            frame = name_pixeles(Image, color_name)
            frame = self.cv_to_qt(frame, 300, 300)
            self.ui.roi_video.setPixmap(frame)

            roi = make_roi(Image)
            name_color(roi, area, color_name)

        if self.ui.type_checkBox.isChecked() == False and self.ui.HSV_checkBox.isChecked() == False:

            frame = colors_pixels(Image)
            frame = self.cv_to_qt(frame, 300, 300)
            self.ui.roi_video.setPixmap(frame)

            roi = make_roi(Image)
            color_detection(roi, area)


        make_rectangle(Image)
        original = self.cv_to_qt(Image)
        self.ui.video.setPixmap(original)

    def stop(self):
        try:

            self.ui.video.clear()
            self.Work.stop()
        except:
            pass

    def color_name_change(self):

        new_color = self.ui.type_input.text()
        new_color = new_color.strip().lower()

        if new_color in colores:
            global color_name
            color_name = new_color
            self.ui.label_color_output.setText(f"{new_color} en pantalla")
        else:
            self.ui.label_color_output.setText(f"{new_color} no está en lista")


	#! ------------------ Slider e input -------------------- !#

    def detection_area(self, value):
        self.ui.input_area.setText(str(value))
        global area
        area = value

    def slider_value(self):
        try:
            self.ui.slider_area.setValue(int(self.ui.input_area.text()))
            global area
            area = int(self.ui.input_area.text())
        except:
            self.ui.input_area.setText(str(1))
            area = 1

	#! ----------------- Sliders HSV min ------------------- !#

    def sliderMin_H_value(self, value):
        self.ui.sliderMin_H.setValue(value)
        global low_H, low_S, low_V, up_H, up_S, up_V
        low_H = value
        self.ui.cuadro_color.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 hsv({low_H*2},{low_S},{low_V}), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMin_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({low_H*2},{low_S},{low_V}));")
        self.ui.sliderMin_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({low_H*2},{low_S},{low_V}));")

    def sliderMin_S_value(self, value):
        self.ui.sliderMin_S.setValue(value)
        global low_H, low_S, low_V, up_H, up_S, up_V
        low_S = value
        self.ui.cuadro_color.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 hsv({low_H*2},{low_S},{low_V}), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMin_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({low_H*2},{low_S},{low_V}));")
        self.ui.sliderMin_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({low_H*2},{low_S},{low_V}));")

    def sliderMin_V_value(self, value):
        self.ui.sliderMin_V.setValue(value)
        global low_H, low_S, low_V, up_H, up_S, up_V
        low_V = value
        self.ui.cuadro_color.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 hsv({low_H*2},{low_S},{low_V}), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMin_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({low_H*2},{low_S},{low_V}));")
        self.ui.sliderMin_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({low_H*2},{low_S},{low_V}));")

    def spinMin_H_value(self, value):
        self.ui.spinMin_H.setValue(value)
        global low_H, low_S, low_V, up_H, up_S, up_V
        low_H = value
        self.ui.cuadro_color.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 hsv({low_H*2},{low_S},{low_V}), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMin_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({low_H*2},{low_S},{low_V}));")
        self.ui.sliderMin_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({low_H*2},{low_S},{low_V}));")

    def spinMin_S_value(self, value):
        self.ui.spinMin_S.setValue(value)
        global low_H, low_S, low_V, up_H, up_S, up_V
        low_S = value
        self.ui.cuadro_color.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 hsv({low_H*2},{low_S},{low_V}), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMin_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({low_H*2},{low_S},{low_V}));")
        self.ui.sliderMin_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({low_H*2},{low_S},{low_V}));")

    def spinMin_V_value(self, value):
        self.ui.spinMin_V.setValue(value)
        global low_H, low_S, low_V, up_H, up_S, up_V
        low_V = value
        self.ui.cuadro_color.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 hsv({low_H*2},{low_S},{low_V}), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMin_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({low_H*2},{low_S},{low_V}));")
        self.ui.sliderMin_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({low_H*2},{low_S},{low_V}));")

	#! ----------------- Sliders HSV max ------------------- !#

    def sliderMax_H_value(self, value):
        self.ui.sliderMax_H.setValue(value)
        global low_H, low_S, low_V, up_H, up_S, up_V
        up_H = value
        self.ui.cuadro_color.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 hsv({low_H*2},{low_S},{low_V}), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMax_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({up_H*2},{up_V},{up_S}));")
        self.ui.sliderMax_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({up_H*2},{up_V},{up_S}));")

    def sliderMax_S_value(self, value):
        self.ui.sliderMax_S.setValue(value)
        global low_H, low_S, low_V, up_H, up_S, up_V
        up_S = value
        self.ui.cuadro_color.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 hsv({low_H*2},{low_S},{low_V}), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMax_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMax_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({up_H*2},{up_S},{up_V}));")

    def sliderMax_V_value(self, value):
        self.ui.sliderMax_V.setValue(value)
        global low_H, low_S, low_V, up_H, up_S, up_V
        up_V = value
        self.ui.cuadro_color.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 hsv({low_H*2},{low_S},{low_V}), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMax_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMax_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({up_H*2},{up_S},{up_V}));")

    def spinMax_H_value(self, value):
        self.ui.spinMax_H.setValue(value)
        global low_H, low_S, low_V, up_H, up_S, up_V
        up_H = value
        self.ui.cuadro_color.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 hsv({low_H*2},{low_S},{low_V}), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMax_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMax_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({up_H*2},{up_S},{up_V}));")

    def spinMax_S_value(self, value):
        self.ui.spinMax_S.setValue(value)
        global low_H, low_S, low_V, up_H, up_S, up_V
        up_S = value
        self.ui.cuadro_color.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 hsv({low_H*2},{low_S},{low_V}), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMax_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMax_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({up_H*2},{up_S},{up_V}));")

    def spinMax_V_value(self, value):
        self.ui.spinMax_V.setValue(value)
        global low_H, low_S, low_V, up_H, up_S, up_V
        up_V = value
        self.ui.cuadro_color.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 hsv({low_H*2},{low_S},{low_V}), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMax_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMax_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({up_H*2},{up_S},{up_V}));")

class Work(QThread):

    Imageupd = pyqtSignal(np.ndarray)

    def __init__(self, parent = None, index = 0):
        super(Work, self).__init__(parent)
        self.index = index
        self.hilo = True

    def run(self):

        cap = cv2.VideoCapture(0)

        while self.hilo:

            ret, frame = cap.read()
            pic = cv2.flip(frame, 1)

            if ret:
                self.Imageupd.emit(pic)

    def stop(self):
        self.hilo = False
        self.quit()

if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()
