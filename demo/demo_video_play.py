#! /usr/bin/python3
# coding = utf-8

import sys
import time
from PyQt5 import QtCore
from PyQt5.QtCore import Qt,pyqtSignal,QSize,QRect,QMetaObject, QCoreApplication, pyqtSlot,QPropertyAnimation,QThread
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPainter, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLabel, QHBoxLayout

from ___video_holder__ import MyThread
from detect import DetectThread


class mycsms(QMainWindow):
    def __init__(self):
        super(mycsms, self).__init__()
        self.image= QImage()
        # self.initUI()
        self.view = QLabel(self)
        self.view.setMinimumSize(800, 430)
        #self.view.setMaximumSize(370, 450)
        # self.view.setAlignment(Qt.AlignCenter)
        dlgLayout = QVBoxLayout(self)
        # dlgLayout.setContentsMargins(0, 0, 400, 400)
        dlgLayout.addWidget(self.view)
        dlgLayout.addStretch(40)
        self.setLayout(dlgLayout)
        self.move(400, 200)

        # 创建线程

        self.thread = DetectThread()
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
    myshow.setMinimumSize(800, 450)
    myshow.setMaximumSize(370, 450)
    myshow.show()
    sys.exit(app.exec_())
