import os
import threading

import cv2
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from pyqt5_plugins.examplebuttonplugin import QtGui

from __detection_ui__ import Ui_MainWindow
from detect import DetectThread

list_model = ['yolov5n.pt', 'yolov5s.pt']
list_camera_ip = ['yolov5n.pt', 'yolov5s.pt']
list_detect_name = ['all', 'car', 'person', 'bicycle', 'motorcycle', 'traffic light', 'truck']


class DetectionDesigner(QMainWindow, Ui_MainWindow):
    currentSelectModelName = list_model[0]
    running = False
    detect_name_index = 0
    pause = True  # 暂停视频

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

        self.stopButton.clicked.connect(self.StopSource)

        self.buttonStart.clicked.connect(self.StartRtsp)

        self.buttonStop.clicked.connect(self.StopSource)
        self.buttonImage.clicked.connect(self.chooseImage)
        self.buttonChooseVideo.clicked.connect(self.chooseVideo)
        self.buttonLocalCamera.clicked.connect(self.buttonOpenLocalCamera)

        self.comboBox_select.addItem("car")
        self.comboBox_select.addItem("person")
        self.comboBox_select.addItem("bicycle")
        self.comboBox_select.addItem("motorcycle")
        self.comboBox_select.addItem("traffic light")
        self.comboBox_select.addItem("truck")
        self.comboBox_select.activated.connect(self.comboBoxSelectClass)
        self.actionsave.triggered.connect(self.action_save)
        self.actionauthor.triggered.connect(self.action_author)
        self.actionversion.triggered.connect(self.action_version)
        self.actionhelp.triggered.connect(self.action_help)
        self.runButton.clicked.connect(self.detect_trigger)
        self.progressBar.setMaximum(100)
        self.raw_video.setScaledContents(True)
        self.out_video_2.setScaledContents(True)

        self.horizontalSlider.setMaximum(100)  # 置信度
        self.horizontalSlider.setValue(35)
        self.conSpinBox.setValue(0.35)
        self.horizontalSlider.valueChanged.connect(self.probChange)

        self.horizontalSlider_iou.setMaximum(100)  # iou
        self.horizontalSlider_iou.setValue(25)
        self.iouSpinBox_2.setValue(0.25)
        self.horizontalSlider_iou.valueChanged.connect(self.iouChange)

    def StartRtsp(self):
        self.StartNewResource('rtsp://admin:123456@192.168.31.46:3389/stream0')

    def probChange(self, value):
        print("置信度改变 " + str(value))
        self.conSpinBox.setValue(value / 100)
        if self.running:
            self.detectThread.changeProb(value)

    def iouChange(self, value):
        print("IOU改变 " + str(value))
        self.iouSpinBox_2.setValue(value / 100)
        if self.running:
            self.detectThread.changeIOU(value)

    def action_save(self):
        print("save")
        QMessageBox.question(None, "温馨提示", "Save", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    def action_help(self):
        print("save")
        QMessageBox.question(None, "help", "保存\tCtrl+S\n账户管理\tCtrl+T\n版本信息\tF1\n帮助文档\tF2\n联系我们\tF3",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    def action_author(self):
        print("author")
        QMessageBox.question(None, "author", "alan", QMessageBox.No, QMessageBox.No)

    def action_version(self):
        print("version")
        QMessageBox.question(None, "version", "v1.0.0", QMessageBox.No, QMessageBox.No)

    def detect_trigger(self):
        print("-----------------")
        self.pause = not self.pause
        if self.pause:
            print("pause")
            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap(":/pic/images/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.runButton.setIcon(icon7)
            if self.running:
                self.detectThread.detectPause()
        else:
            print("start")
            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap(":/pic/images/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.runButton.setIcon(icon7)
            if self.running:
                self.detectThread.detectStart()

    def buttonOpenLocalCamera(self):
        print('buttonOpenCamera')
        try:
            if self.running:
                self.StopSource()
                self.buttonLocalCamera.setText("本地摄像头关闭")
            else:
                self.StartNewResource(source='0')
        except:
            print()

    def setting_progress(self, v):
        self.progressBar.setValue(v)

    def comboBoxSelectClass(self, name_index):
        print("comboBoxSelect")
        print(name_index)
        self.detect_name_index = name_index
        if self.running:
            self.detectThread.chooseSpecialClass(name_index)

    def displayobjectLcdNumber(self, number_array):
        print("displayObjectLcdLabel")
        print(number_array)
        self.lcdNumber_1.display(number_array['1'])
        self.lcdNumber_2.display(number_array['2'])
        self.lcdNumber_3.display(number_array['3'])
        self.lcdNumber_4.display(number_array['4'])
        self.lcdNumber_5.display(number_array['5'])
        self.lcdNumber.display(number_array['6'])

        if self.detect_name_index == 0:
            print("all")
            # all_nu = 0
            # for nu in number_array.values():
            #     all_nu += nu
            # print(all_nu)
            self.label_numer_result.setText(f"{number_array['0']}")
        else:
            print(self.detect_name_index)
            self.label_numer_result.setText(f"{number_array[str(self.detect_name_index)]}")
            print('ffffffffffffffffffffff')

    def StartNewResource(self, source):
        print('StartNewResource')
        if self.running:
            result = QMessageBox.question(None, "温馨提示", "您确定结束正在进行的检测吗", QMessageBox.Yes | QMessageBox.No,
                                          QMessageBox.No)
            if result == QMessageBox.Yes:
                self.running = False
                self.detectThread.stop()
                timer = threading.Timer(interval=1, function=self.StartNewResource, args=(source,))
                timer.start()

        else:
            self.running = True
            # rtspUrl =
            self.detectThread = DetectThread(p_source=source)
            self.detectThread.sourceSignal.connect(self.display)
            self.detectThread.detectSignal.connect(self.displayDetect)
            self.detectThread.objectSignal.connect(self.displayobjectLcdNumber)
            self.detectThread.progressSignal.connect(self.setting_progress)
            self.detectThread.start()

    def StopSource(self):
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

        # if self.running:
        #     self.running = False
        #     self.detectThread.stop()
        # else:
        #     self.running = True
        #     self.detectThread = DetectThread(p_source=img_path)
        #     self.detectThread.sourceSignal.connect(self.display)
        #     self.detectThread.detectSignal.connect(self.displayDetect)
        #     self.detectThread.objectSignal.connect(self.displayobjectLcdNumber)
        #     self.detectThread.progressSignal.connect(self.setting_progress)
        #     self.detectThread.start()
        self.StartNewResource(source=img_path)

    def chooseVideo(self):
        print('chooseVideo')
        filename = QFileDialog.getOpenFileNames(self, '选择视频', os.getcwd(), "All Files(*.mp4)")
        print(filename)
        video_path = filename[0][0]

        # if self.running:
        #     self.running = False
        #     self.detectThread.stop()
        # else:
        #     self.running = True
        #     self.detectThread = DetectThread(p_source=video_path)
        #     self.detectThread.sourceSignal.connect(self.display)
        #     self.detectThread.detectSignal.connect(self.displayDetect)
        #     self.detectThread.objectSignal.connect(self.displayobjectLcdNumber)
        #     self.detectThread.progressSignal.connect(self.setting_progress)
        #     self.detectThread.start()
        self.StartNewResource(video_path)

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
