from modules import *

class MainApp(QMainWindow):

    def __init__(self, parent=None, *args):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

	    #! --------------------- Boxes ------------------------ !#

        #* Lista de cámaras
        self.online_cam = QCameraInfo.availableCameras()
        self.ui.camera_list.addItems([c.description() for c in self.online_cam])

        #* Botón de inicio
        self.ui.start_button.clicked.connect(self.start)

        #* Botón de stop
        self.ui.stop_button.clicked.connect(self.stop)

        #* Input de número
        self.ui.input_area.textChanged.connect(self.slider_value)

        #* Input de color
        self.ui.type_input.returnPressed.connect(lambda:self.ui.label_color_name.setText(self.ui.type_input.text().strip().lower().capitalize()) if self.ui.type_input.text().strip().lower() in colores else self.ui.label_color_output.setText(f"{self.ui.type_input.text().strip().lower()} no está en lista"))

        #* Slider del area
        self.ui.slider_area.valueChanged.connect(self.detection_area)

        #* Sliders HSV min
        self.ui.sliderMin_H.valueChanged.connect(self.HSV_spinValues)
        self.ui.spinMin_H.valueChanged.connect(self.HSV_sliderValues)

        self.ui.sliderMin_S.valueChanged.connect(self.HSV_spinValues)
        self.ui.spinMin_S.valueChanged.connect(self.HSV_sliderValues)

        self.ui.sliderMin_V.valueChanged.connect(self.HSV_spinValues)
        self.ui.spinMin_V.valueChanged.connect(self.HSV_sliderValues)

        #* Sliders HSV max
        self.ui.sliderMax_H.valueChanged.connect(self.HSV_spinValues)
        self.ui.spinMax_H.valueChanged.connect(self.HSV_sliderValues)

        self.ui.sliderMax_S.valueChanged.connect(self.HSV_spinValues)
        self.ui.spinMax_S.valueChanged.connect(self.HSV_sliderValues)

        self.ui.sliderMax_V.valueChanged.connect(self.HSV_spinValues)
        self.ui.spinMax_V.valueChanged.connect(self.HSV_sliderValues)

        #* Imagen de ayuda
        self.ui.help_image.setPixmap(QtGui.QPixmap("./images/guide.JPG").scaled(1200,1200,Qt.KeepAspectRatio))

	#! ----------------------- VIDEO ------------------------ !#

    def start(self):

        global camIndex
        camIndex = self.ui.camera_list.currentIndex()
        self.Work = Work()
        self.Work.Imageupd.connect(self.HSV_slot)
        self.Work.Imageupd.connect(self.tf_slot)
        self.Work.start()

    def cv_to_qt(self, Image, widht = 300, height = 300):

        pic = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
        convertir_QT = QImage(pic.data, pic.shape[1], pic.shape[0], QImage.Format_RGB888)
        frame = convertir_QT.scaled(widht, height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(frame)

    @pyqtSlot(np.ndarray)
    def HSV_slot(self, Image):

        if self.ui.default_radiobutton.isChecked():

            frame = colors_pixels(Image)
            frame = self.cv_to_qt(frame)
            self.ui.HSV_video.setPixmap(frame)
            color_detection(Image, area)

        if self.ui.HSV_radiobutton.isChecked():

            frame = HSV_pixeles(Image, low_H, low_S, low_S, up_H, up_S, up_V)
            frame = self.cv_to_qt(frame)
            self.ui.HSV_video.setPixmap(frame)
            HSV_color(Image, area, low_H, low_S, low_V, up_H, up_S, up_V)

        if self.ui.type_radiobutton.isChecked():

            frame = name_pixeles(Image, self.ui.label_color_name.text().strip().lower())
            frame = self.cv_to_qt(frame)
            self.ui.HSV_video.setPixmap(frame)
            name_color(Image, area, self.ui.label_color_name.text().strip().lower())

        original = self.cv_to_qt(Image)
        self.ui.RGB_video.setPixmap(original)

    @pyqtSlot(np.ndarray)
    def tf_slot(self, Image):
        pass

    def stop(self):
        try:
            self.ui.video.clear()
            self.ui.roi_video.clear()
            self.Work.stop()
        except:
            pass

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

	#! ------------------ HSV values -------------------- !#

    def HSV_sliderValues(self):

        global low_H, low_S, low_V, up_H, up_S, up_V

        low_H = self.ui.spinMin_H.value()
        low_S = self.ui.spinMin_S.value()
        low_V = self.ui.spinMin_V.value()
        up_H = self.ui.spinMax_H.value()
        up_S = self.ui.spinMax_S.value()
        up_V = self.ui.spinMax_V.value()

        self.ui.sliderMin_H.setValue(low_H)
        self.ui.sliderMin_S.setValue(low_S)
        self.ui.sliderMin_V.setValue(low_V)
        self.ui.sliderMax_H.setValue(up_H)
        self.ui.sliderMax_S.setValue(up_S)
        self.ui.sliderMax_V.setValue(up_V)

        self.ui.cuadro_color.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 hsv({low_H*2},{low_S},{low_V}), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMin_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({low_H*2},{low_S},{low_V}));")
        self.ui.sliderMin_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({low_H*2},{low_S},{low_V}));")
        self.ui.sliderMax_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMax_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({up_H*2},{up_S},{up_V}));")

    def HSV_spinValues(self):

        global low_H, low_S, low_V, up_H, up_S, up_V

        low_H = self.ui.sliderMin_H.value()
        low_S = self.ui.sliderMin_S.value()
        low_V = self.ui.sliderMin_V.value()
        up_H = self.ui.sliderMax_H.value()
        up_S = self.ui.sliderMax_S.value()
        up_V = self.ui.sliderMax_V.value()

        self.ui.spinMin_H.setValue(low_H)
        self.ui.spinMin_S.setValue(low_S)
        self.ui.spinMin_V.setValue(low_V)
        self.ui.spinMax_H.setValue(up_H)
        self.ui.spinMax_S.setValue(up_S)
        self.ui.spinMax_V.setValue(up_V)

        self.ui.cuadro_color.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 hsv({low_H*2},{low_S},{low_V}), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMin_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({low_H*2},{low_S},{low_V}));")
        self.ui.sliderMin_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({low_H*2},{low_S},{low_V}));")
        self.ui.sliderMax_S.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,0,255), stop:1 hsv({up_H*2},{up_S},{up_V}));")
        self.ui.sliderMax_V.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 hsv(0,255,0), stop:1 hsv({up_H*2},{up_S},{up_V}));")


class Work(QThread):

    Imageupd = pyqtSignal(np.ndarray)

    def run(self):

        global camIndex

        self.hilo = True
        cap = cv2.VideoCapture(camIndex)

        while self.hilo:

            ret, frame = cap.read()
            pic = cv2.flip(frame, 1)

            if ret:
                self.Imageupd.emit(pic)

    def stop(self):
        self.hilo = False
        self.stop()

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(open("./styles/main.css", "r").read())
    window = MainApp()
    window.show()
    app.exec_()
