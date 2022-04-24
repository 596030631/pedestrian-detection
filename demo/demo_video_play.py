#! /usr/bin/python3
# coding = utf-8

import sys
import time
from PyQt5 import QtCore
from PyQt5.QtCore import Qt,pyqtSignal,QSize,QRect,QMetaObject, QCoreApplication, pyqtSlot,QPropertyAnimation,QThread
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPainter, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLabel, QHBoxLayout

import cv2
# 线程类：
class MyThread(QThread):
        # 定义信号,定义参数为str类型
    breakSignal = pyqtSignal(QPixmap)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.stoped= False
        self.mutex= QtCore.QMutex()


    def run(self):
        with QtCore.QMutexLocker(self.mutex):
            self.stoped= False

        cap = cv2.VideoCapture("rtsp://admin:123456@192.168.31.46:3389/stream0")
        print(cap.isOpened())

        while cap.isOpened():
            if self.stoped:
                return
            ret,frame = cap.read()
            # cv2.imshow("frame",frame)
            # cv2.waitKey(1)

            height, width, bytesPerComponent = frame.shape
            bytesPerLine = bytesPerComponent * width
            # 变换彩色空间顺序
            cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)

            image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)


            self.breakSignal.emit(QPixmap.fromImage(image))
            #40毫秒发送一次信号
            time.sleep(0.04)

    def stop(self):
        with QtCore.QMutexLocker(self.mutex):
            self.stoped= True

    def isStoped(self):
        with QtCore.QMutexLocker(self.mutex):
            return self.stoped

class mycsms(QMainWindow):
    def __init__(self):
        super(mycsms, self).__init__()
        self.image= QImage()
        # self.initUI()
        self.view = QLabel(self)
        self.view.setMinimumSize(800, 430);
        #self.view.setMaximumSize(370, 450);
        # self.view.setAlignment(Qt.AlignCenter)
        dlgLayout = QVBoxLayout(self)
        # dlgLayout.setContentsMargins(0, 0, 400, 400)
        dlgLayout.addWidget(self.view)
        dlgLayout.addStretch(40)
        self.setLayout(dlgLayout)
        self.move(400, 200)

        # 创建线程

        self.thread = MyThread()
        # # 注册信号处理函数
        self.thread.breakSignal.connect(self.showCamer)
        # # 启动线程
        self.thread.start()
    # 读摄像头
    def showCamer(self,qpixmap):
        self.view.setPixmap(qpixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = mycsms()
    myshow.setMinimumSize(800, 450);
    myshow.setMaximumSize(370, 450);
    myshow.show()
    sys.exit(app.exec_())
