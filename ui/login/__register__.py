import pickle

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QMessageBox

from __model__ import userRegister
from __register_ui__ import Ui_Register


class RegisterDesigner(QMainWindow, Ui_Register):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initEvent()

    def initEvent(self):
        print("event")
        self.pushbutton_init()
        self.line_init()
        self.buttonRegister.clicked.connect(self.check_password)
        self.buttonCLear.clicked.connect(self.clear_user_info)

    def clear_user_info(self):
        self.userId.setText('')
        self.password.setText('')
        self.passwordAgain.setText('')

    # 按钮初始化方法
    def pushbutton_init(self):
        # 设置注册按钮为不可点击状态，绑定槽函数
        self.buttonRegister.setEnabled(False)
        self.buttonRegister.clicked.connect(userRegister)
        # 取消按钮绑定取消注册槽函数
        # self.buttonExit.clicked.connect(self.cancel_func)

    # 检查输入方法,只有在三个文本输入框都有文字时，注册按钮才为可点击状态
    def check_input(self):
        if (self.userId.text() and self.password.text()
                and self.passwordAgain.text()):
            self.buttonRegister.setEnabled(True)
        else:
            self.buttonRegister.setEnabled(False)

    def line_init(self):
        """
         单行文本输入框初始化方法
         3个单行文本输入框都绑定检查用户输入槽函数
         设置用户密码显示方式：正在输入时明文，焦点转移后掩码
         注册提示
         设置文本校验器
         检查密码合法性
         """
        # 单行文本输入框内容变化绑定按钮显示
        self.userId.textChanged.connect(self.check_input)
        self.password.textChanged.connect(self.check_input)
        self.passwordAgain.textChanged.connect(self.check_input)
        # 设置密码显示方式
        self.password.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.passwordAgain.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        # 注册提示
        self.userId.setPlaceholderText('输入用户名，字母数字，不可为中文或特殊字符。')
        self.password.setPlaceholderText('密码为6到10位数字字母，首字母必须为大写。')
        self.passwordAgain.setPlaceholderText('请再次确认密码！')
        # 设置文本框校验器
        # 姓名文本框校验器设置
        # 1、创建正则表达式限定输入内容
        name_RegExp = QRegExp("[0-9A-Za-z]*")
        # 2、创建文本框校验器
        name_validator = QRegExpValidator(name_RegExp)
        # 3、文本输入框绑定创建的校验器
        self.userId.setValidator(name_validator)
        # 设置密码文本输入框校验器
        password_val = QRegExpValidator(QRegExp("^[A-Z][0-9A-Za-z]{10}$"))
        self.password.setValidator(password_val)
        self.passwordAgain.setValidator(password_val)

    # 检查用户输入密码合法性方法
    def check_password(self):
        password_1 = self.password.text()
        password_2 = self.passwordAgain.text()

        if len(password_1) < 6:
            QMessageBox.warning(None, '警告', '密码位数小于6')
            self.password.setText('')
            self.passwordAgain.setText('')
        else:
            if password_1 == password_2:
                pass
            else:
                QMessageBox.warning(None, '警告', '两次密码输入结果不一致！')
                self.password.setText('')
                self.passwordAgain.setText('')

    # 用户注册方法
    def register_func(self):
        # 先获取注册用户ID，检查用户ID是否存在
        ID = self.name_line.text()
        try:
            with open('users.pkl', 'rb') as f1:
                users = pickle.load(f1)
        except:
            users = {}

        # 如果用户ID已存在，提示用户ID已被注册
        if ID in users.keys():
            QMessageBox.information(None, '提示', '该用户ID已被注册！')
        # 否则收集用户注册信息
        else:
            gender = self.gender_data()
            user_data = [self.password1_line.text(),
                         self.nick_line.text(),
                         gender]
            # 写入用户信息字典
            users[ID] = user_data
            with open('users.pkl', 'wb') as f2:
                pickle.dump(users, f2)
            # 提醒用户注册成功，询问是否登录
            choice = QMessageBox.information(None, '提示', '注册成功，是否登录？',
                                             QMessageBox.Yes | QMessageBox.No)
            # 如选择是，关闭注册页面，并在登录页面用户ID显示注册ID,密码
            if choice == QMessageBox.Yes:
                self.successful_signal.emit([self.name_line.text(),
                                             self.password1_line.text()])
                self.close()
            # 如选择否，直接关闭注册页面。
            else:
                self.close()
