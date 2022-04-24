# import time
#
# import cv2
# from PyQt5 import QtCore
# from PyQt5.QtCore import QThread, pyqtSignal
# from PyQt5.QtGui import QPixmap, QImage
#
#
# class MyThread(QThread):
#     # 定义信号,定义参数为str类型
#     breakSignal = pyqtSignal(QPixmap)
#
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.stoped = False
#         self.mutex = QtCore.QMutex()
#
#     def run(self):
#         with QtCore.QMutexLocker(self.mutex):
#             self.stoped = False
#
#         # cap = cv2.VideoCapture("rtsp://admin:123456@192.168.31.46:3389/stream0")
#         cap = cv2.VideoCapture(0)
#         print(cap.isOpened())
#
#         while cap.isOpened():
#             if self.stoped:
#                 return
#             ret, frame = cap.read()
#             # cv2.imshow("frame",frame)
#             # cv2.waitKey(1)
#
#             height, width, bytesPerComponent = frame.shape
#             bytesPerLine = bytesPerComponent * width
#             # 变换彩色空间顺序
#             cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
#
#             image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
#
#             self.breakSignal.emit(QPixmap.fromImage(image))
#             # 40毫秒发送一次信号
#             time.sleep(0.04)
#
#     def stop(self):
#         with QtCore.QMutexLocker(self.mutex):
#             self.stoped = True
#
#     def isStoped(self):
#         with QtCore.QMutexLocker(self.mutex):
#             return self.stoped
