from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit

# from __RegisterQDialog__ import RegisterQDialog
from __model__ import userLogin, registerSuccessful
from __register__ import RegisterDesigner
from __ui__ import Ui_systemClass


class LoginDesigner(QMainWindow, Ui_systemClass):
    login_success = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initEvent()

    def initEvent(self):
        print("event")
        self.line_init()
        self.button_init()

    def checkUserPassword(self):
        user = self.user.text()
        password = self.password.text()
        print(f'user-password >> [{user}, {password}]')
        if user is not None and password is not None:
            if len(user) > 4 and len(password) > 4:
                self.buttonLogin.setEnabled(True)

    # 单行文本输入框初始化方法
    def line_init(self):
        self.user.setClearButtonEnabled(True)
        self.user.setTextMargins(10, 10, 10, 10)
        self.user.setPlaceholderText('在此输入用户名')  # 设置提示语
        self.user.textChanged.connect(self.checkUserPassword)  # 设置检查单行文本输入框输入状态
        self.password.setTextMargins(10, 10, 10, 10)
        self.password.setClearButtonEnabled(True)
        self.password.setPlaceholderText('在此输入密码')
        self.password.setEchoMode(QLineEdit.Password)  # 设置用户密码以掩码显示
        self.password.setEchoMode(QLineEdit.PasswordEchoOnEdit)  # 设置用户在输入时明文显示，控件焦点转移后掩码显示
        self.password.textChanged.connect(self.checkUserPassword)

    # 注册按钮
    # def userRegister(self):
    #     print("register")
    #     register = RegisterDesigner()
    #     register.successful_signal.connect(registerSuccessful)
    #     register.show()

    def userLogin(self):
        userLogin(self, self.user.text(), self.password.text())

    def button_init(self):
        self.buttonLogin.setEnabled(False)  # 先设置登录按钮为不可点击状态，当用户输入用户名及密码时才变为可点击状态
        self.buttonLogin.clicked.connect(self.userLogin)  # 登录按钮点击信号绑定槽函数
        # self.buttonRegister.clicked.connect(self.userRegister)  # 注册按钮点击信号绑定槽函数

    def LoginSuccessfulCallback(self):
        print("展示识别界面")
        self.login_success.emit("success")
        self.destroy()

    def closeEvent(self, closeEvent):
        print("close Event")
        result = QMessageBox.question(None, '温馨提示', '您真的要退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            closeEvent.accept()
        else:
            closeEvent.ignore()
