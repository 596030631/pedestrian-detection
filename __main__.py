import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

#
# class Designer(QMainWindow, ui.system.Ui_systemClass):
#
#     def __init__(self):
#         super().__init__()
#         # self.initUI()
#         self.setupUi(self)
#
#     def Login(self):
#         print("login")
#
#
#     def closeEvent(self, closeEvent):
#         print("关闭操作")
#         result = QMessageBox.question(None, "温馨提示", "您真的要退出吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#         if result == QMessageBox.Yes:
#             closeEvent.accept()
#         else:
#             closeEvent.ignore()
from __detection__ import DetectionDesigner
from __login__ import LoginDesigner
from __manager__ import ManagerDesigner
from __register__ import RegisterDesigner


def initUI(self):
    self.closeButton.clicked.connect(self.close)
    self.show()

app = QtWidgets.QApplication(sys.argv)
login_ui = LoginDesigner()
detection_ui = DetectionDesigner()
manager_ui = ManagerDesigner()


def exit_login():
    manager_ui.close()
    detection_ui.close()
    login_ui.show()


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # mainWindow = QMainWindow()
    # ui = ui.system.Ui_systemClass()  # 类的初始化
    # ui.setupUi(mainWindow)  # 传对象
    # mainWindow.show()


    manager_ui.buttonCancel.clicked.connect(manager_ui.close)
    manager_ui.pushButton_exit.clicked.connect(exit_login)

    register = RegisterDesigner()

    login_ui.login_success.connect(detection_ui.Open)
    login_ui.buttonRegister.clicked.connect(register.show)
    detection_ui.actionsetting.triggered.connect(manager_ui.show)

    detection_ui.show()

    # app = QApplication(sys.argv)
    # mainWindow = QMainWindow()
    # ui = ui.pedestrian_detection_UI.Ui_MainWindow()  # 类的初始化
    # ui.setupUi(mainWindow)  # 传对象
    # mainWindow.show()

    app.setWindowIcon(QIcon(":images/zong.png"))
    sys.exit(app.exec_())  # 主要作用是用死循环来监听界面的关闭按钮等界面控制等事件
