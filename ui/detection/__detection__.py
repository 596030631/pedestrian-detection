from PyQt5.QtWidgets import QMainWindow, QMessageBox

from __detection_ui__ import Ui_MainWindow
from detect import DetectThread

list_model = ['yolov5n.pt', 'yolov5s.pt']
list_camera_ip = ['yolov5n.pt', 'yolov5s.pt']

class DetectionDesigner(QMainWindow, Ui_MainWindow):
    currentSelectModelName = list_model[0]

    def __init__(self):
        super(DetectionDesigner, self).__init__()
        self.setupUi(self)
        self.initEvent()

    def display(self, pixMap):
        self.raw_video.setPixmap(pixMap)

    def displayDetect(self, pixMap):
        self.out_video_2.setPixmap(pixMap)

    def initEvent(self):
        print('initEvent')
        self.comboBoxModel.addItem('yolov5n.pt')
        self.comboBoxModel.addItem('yolov5s.pt')
        self.comboBoxModel.activated.connect(self.activated)
        self.comboBoxCameraIP.addItem('192.168.1.188')
        self.comboBoxCameraIP.addItem('192.168.1.11')
        self.comboBoxCameraIP.addItem('192.168.1.12')
        self.buttonStart.clicked.connect(self.Start)
        self.buttonStop.clicked.connect(self.Stop)

    def Start(self):
        print('start')
        self.detectThread = DetectThread()
        self.detectThread.sourceSignal.connect(self.display)
        self.detectThread.detectSignal.connect(self.displayDetect)
        self.detectThread.start()


    def Stop(self):
        print('stop')
        self.detectThread.stop()

    def activated(self):
        print("activated")
        sender = self.sender()
        print(sender.currentText())


    def comboBoxModelActivated(self, lb):
        print('comboBoxModelActivated:' + lb)




    def closeEvent(self, closeEvent):
        print("关闭操作")
        result = QMessageBox.question(None, "温馨提示", "您真的要退出吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            closeEvent.accept()
        else:
            closeEvent.ignore()
            
    def Open(self):
        print("open")
        self.show()
