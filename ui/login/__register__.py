from PyQt5.QtWidgets import QMainWindow

from __model__ import userRegister
from __register_ui__ import Ui_Register


class RegisterDesigner(QMainWindow, Ui_Register):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initEvent()

    def initEvent(self):
        print("event")



        self.buttonRegister.clicked.connect(userRegister)
