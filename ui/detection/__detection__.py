from PyQt5.QtWidgets import QMainWindow, QMessageBox

# from ___video_holder__ import MyThread
from __detection_ui__ import Ui_MainWindow
from detect import DetectThread


class DetectionDesigner(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(DetectionDesigner, self).__init__()
        self.setupUi(self)

        # self.thread = MyThread()
        # # # 注册信号处理函数
        # self.thread.breakSignal.connect(self.display)
        # # # 启动线程
        # self.thread.start()

        self.detectThread = DetectThread()
        self.detectThread.sourceSignal.connect(self.display)
        self.detectThread.detectSignal.connect(self.displayDetect)
        self.detectThread.start()

    def display(self, pixMap):
        self.raw_video.setPixmap(pixMap)

    def displayDetect(self, pixMap):
        self.out_video_2.setPixmap(pixMap)

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
