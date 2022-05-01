import os

import cv2
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog

from __detection_ui__ import Ui_MainWindow
from detect import DetectThread

list_model = ['yolov5n.pt', 'yolov5s.pt']
list_camera_ip = ['yolov5n.pt', 'yolov5s.pt']


class DetectionDesigner(QMainWindow, Ui_MainWindow):
    currentSelectModelName = list_model[0]
    running = False

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
        self.buttonImage.clicked.connect(self.chooseImage)
        self.buttonChooseVideo.clicked.connect(self.chooseVideo)
        self.buttonLocalCamera.clicked.connect(self.buttonOpenLocalCamera)

    def buttonOpenLocalCamera(self):
        print('buttonOpenCamera')
        try:
            if self.running:
                self.running = False
                self.buttonLocalCamera.setText("本地摄像头关闭")
                self.detectThread.stop()
            else:
                self.running = True
                self.buttonLocalCamera.setText("本地摄像头开启")
                self.detectThread = DetectThread(p_source='0')
                self.detectThread.sourceSignal.connect(self.display)
                self.detectThread.detectSignal.connect(self.displayDetect)
                self.detectThread.start()
        except:
            print()

    def Start(self):
        print('start')
        if self.running:
            self.running = False
            self.detectThread.stop()
        else:
            self.running = True
            rtspUrl = 'rtsp://admin:123456@192.168.31.46:3389/stream0'
            self.detectThread = DetectThread(p_source=rtspUrl)
            self.detectThread.sourceSignal.connect(self.display)
            self.detectThread.detectSignal.connect(self.displayDetect)
            self.detectThread.start()

    def Stop(self):
        print('stop')
        if self.running:
            self.running = False
            self.detectThread.stop()

    def chooseImage(self):
        print('chooseImage')
        filename = QFileDialog.getOpenFileNames(self, '选择图像', os.getcwd(), "All Files(*.jpg))")
        print(filename)
        img_path = filename[0][0]
        print(img_path)
        img = cv2.imread(img_path)
        print(img)
        # height, width, bytesPerComponent = img.shape
        # bytesPerLine = bytesPerComponent * width
        # cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        # img = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        # self.raw_video.setPixmap(QPixmap.fromImage(img))

        if self.running:
            self.running = False
            self.detectThread.stop()
        else:
            self.running = True
            self.detectThread = DetectThread(p_source=img_path)
            self.detectThread.sourceSignal.connect(self.display)
            self.detectThread.detectSignal.connect(self.displayDetect)
            self.detectThread.start()

    def chooseVideo(self):
        print('chooseVideo')
        filename = QFileDialog.getOpenFileNames(self, '选择视频', os.getcwd(), "All Files(*.mp4)")
        print(filename)
        video_path = filename[0][0]

        if self.running:
            self.running = False
            self.detectThread.stop()
        else:
            self.running = True
            self.detectThread = DetectThread(p_source=video_path)
            self.detectThread.sourceSignal.connect(self.display)
            self.detectThread.detectSignal.connect(self.displayDetect)
            self.detectThread.start()

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
