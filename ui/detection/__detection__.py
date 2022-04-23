from PyQt5.QtWidgets import QMainWindow, QMessageBox

import pedestrian_detection_UI


class DetectionDesigner(QMainWindow, pedestrian_detection_UI.Ui_MainWindow):

    def __init__(self):
        super(DetectionDesigner, self).__init__()
        self.setupUi(self)

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