# import sys
# import cv2
# from PyQt5 import QtCore, QtWidgets
# from PyQt5.QtGui import QIcon
# import ui.system
#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
# import ui.pedestrian_detection_UI
# from PyQt5.QtCore import *
#
# import ui.pedestrian_detection_UI
#
# from ui.system import Ui_systemClass
# from ui.pedestrian_detection_UI import Ui_MainWindow
# from PyQt5 import QtCore, QtGui, QtWidgets
#
#
# class Ui_systemClass(object):
#     def setupUi(self, systemClass):
#         systemClass.setObjectName("systemClass")
#         systemClass.resize(940, 666)
#         systemClass.setMinimumSize(QtCore.QSize(940, 666))
#         systemClass.setMaximumSize(QtCore.QSize(940, 666))
#
#         # 隐藏框架和标题栏
#         # systemClass.setWindowFlags(QtCore.Qt.FramelessWindowHint)
#         # systemClass.setAttribute(QtCore.Qt.WA_TranslucentBackground)
#
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/pic/images/zong.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         systemClass.setWindowIcon(icon)
#         systemClass.setStyleSheet("*{\n"
# "font-size:24px;\n"
# "font-family:sans-serif;\n"
# "}\n"
# "#systemClass{  \n"
# "background-image:\n"
# "\n"
# "}\n"
# "QFrame{\n"
# "background:rgba(0,0,0,0.8);\n"
# "border-radius:15px;\n"
# "}\n"
# "QPushButton{\n"
# "background:#03a9f4;\n"
# "color:#fff;\n"
# "border-radius:15px;\n"
# "}\n"
# "QLineEdit{\n"
# "border-radius:15px;\n"
# "color:#03a9f4;\n"
# "}\n"
# "QLabel{\n"
# "color:#fff;\n"
# "background:transparent;\n"
# "font-size:30px;\n"
# "}\n"
# "QTextEdit{\n"
# "color:#fff;\n"
# "background:transparent;\n"
# "font-size:30px;\n"
# "}\n"
# "QCheckBox{\n"
# "color:#fff;\n"
# "background:transparent;\n"
# "font-size:15px;\n"
# "}")
#         self.frame = QtWidgets.QFrame(systemClass)
#         self.frame.setGeometry(QtCore.QRect(170, 160, 581, 381))
#         self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame.setObjectName("frame")
#         self.pushButton = QtWidgets.QPushButton(self.frame)
#         self.pushButton.setGeometry(QtCore.QRect(40, 280, 241, 41))
#         self.pushButton.setObjectName("pushButton")
#         self.lineEdit = QtWidgets.QLineEdit(self.frame)
#         self.lineEdit.setGeometry(QtCore.QRect(40, 100, 501, 51))
#         self.lineEdit.setText("")
#         self.lineEdit.setCursorPosition(0)
#         self.lineEdit.setObjectName("lineEdit")
#         self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
#         self.lineEdit_2.setGeometry(QtCore.QRect(40, 170, 501, 51))
#         self.lineEdit_2.setText("")
#         self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.lineEdit_2.setCursorPosition(0)
#         self.lineEdit_2.setObjectName("lineEdit_2")
#         self.checkBox = QtWidgets.QCheckBox(self.frame)
#         self.checkBox.setGeometry(QtCore.QRect(100, 240, 151, 41))
#         self.checkBox.setObjectName("checkBox")
#         self.label_2 = QtWidgets.QLabel(self.frame)
#         self.label_2.setGeometry(QtCore.QRect(240, 30, 221, 71))
#         self.label_2.setStyleSheet("")
#         self.label_2.setObjectName("label_2")
#         self.textEdit = QtWidgets.QTextEdit(self.frame)
#         self.textEdit.setGeometry(QtCore.QRect(370, 250, 104, 31))
#         self.textEdit.setObjectName("textEdit")
#         self.pushButton_2 = QtWidgets.QPushButton(self.frame)
#         self.pushButton_2.setGeometry(QtCore.QRect(310, 280, 231, 41))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.label = QtWidgets.QLabel(systemClass)
#         self.label.setGeometry(QtCore.QRect(40, 40, 851, 571))
#         self.label.setStyleSheet("border-image:url(:/pic/images/tu01.png)\n"
# "")
#         self.label.setText("")
#         self.label.setObjectName("label")
#         self.closeButton = QtWidgets.QPushButton(systemClass)
#         self.closeButton.setGeometry(QtCore.QRect(820, 60, 50, 28))
#         self.closeButton.setMinimumSize(QtCore.QSize(50, 28))
#         self.closeButton.setMaximumSize(QtCore.QSize(50, 28))
#         self.closeButton.setStyleSheet("QPushButton {\n"
# "border-style: solid;\n"
# "border-width: 0px;\n"
# "border-radius: 0px;\n"
# "background-color: rgba(223, 223, 223, 0);}\n"
# "QPushButton::focus{outline: none;}\n"
# "QPushButton::hover {\n"
# "border-style: solid;\n"
# "border-width: 0px;\n"
# "border-radius: 0px;\n"
# "background-color: rgba(223, 223, 223, 150);}")
#         self.closeButton.setText("")
#         icon1 = QtGui.QIcon()
#         icon1.addPixmap(QtGui.QPixmap(":/pic/images/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.closeButton.setIcon(icon1)
#         self.closeButton.setObjectName("closeButton")
#         self.minButton = QtWidgets.QPushButton(systemClass)
#         self.minButton.setGeometry(QtCore.QRect(770, 60, 50, 28))
#         self.minButton.setMinimumSize(QtCore.QSize(50, 28))
#         self.minButton.setMaximumSize(QtCore.QSize(50, 28))
#         self.minButton.setStyleSheet("QPushButton {\n"
# "border-style: solid;\n"
# "border-width: 0px;\n"
# "border-radius: 0px;\n"
# "background-color: rgba(223, 223, 223, 0);}\n"
# "QPushButton::focus{outline: none;}\n"
# "QPushButton::hover {\n"
# "border-style: solid;\n"
# "border-width: 0px;\n"
# "border-radius: 0px;\n"
# "background-color: rgba(223, 223, 223, 150);}")
#         self.minButton.setText("")
#         icon2 = QtGui.QIcon()
#         icon2.addPixmap(QtGui.QPixmap(":/pic/images/min.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.minButton.setIcon(icon2)
#         self.minButton.setObjectName("minButton")
#         self.label_3 = QtWidgets.QLabel(systemClass)
#         self.label_3.setGeometry(QtCore.QRect(60, 50, 61, 41))
#         self.label_3.setStyleSheet("image: url(:/pic/images/zong.png);")
#         self.label_3.setText("")
#         self.label_3.setObjectName("label_3")
#         self.label_4 = QtWidgets.QLabel(systemClass)
#         self.label_4.setGeometry(QtCore.QRect(120, 60, 309, 31))
#         self.label_4.setObjectName("label_4")
#         self.label.raise_()
#         self.frame.raise_()
#         self.closeButton.raise_()
#         self.minButton.raise_()
#         self.label_3.raise_()
#         self.label_4.raise_()
#
#         self.retranslateUi(systemClass)
#         self.closeButton.clicked.connect(systemClass.close)
#         self.minButton.clicked.connect(systemClass.showMinimized)
#         QtCore.QMetaObject.connectSlotsByName(systemClass)
#
#     def retranslateUi(self, systemClass):
#         _translate = QtCore.QCoreApplication.translate
#         systemClass.setWindowTitle(_translate("systemClass", "system"))
#         self.pushButton.setText(_translate("systemClass", "登    录"))
#         self.lineEdit.setPlaceholderText(_translate("systemClass", "用户名"))
#         self.lineEdit_2.setPlaceholderText(_translate("systemClass", "密码"))
#         self.checkBox.setText(_translate("systemClass", "记住密码"))
#         self.label_2.setText(_translate("systemClass", "Login"))
#         self.textEdit.setHtml(_translate("systemClass", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'sans-serif\'; font-size:30px; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15px; text-decoration: underline; color:#00aaff;\">忘记密码？</span></p></body></html>"))
#         self.pushButton_2.setText(_translate("systemClass", "注    册"))
#         self.label_4.setText(_translate("systemClass", "<html><head/><body><p><span style=\" font-size:12pt;\">行人检测与追踪系统</span></p></body></html>"))
#
#
# '''
# 本地网络通讯软件：
# 登录，注册界面
# '''
#
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt, pyqtSignal, QRegExp
# from PyQt5.QtGui import QFont, QIcon, QRegExpValidator
#
# import pickle
#
#
# # 用户登录页面
# class LoginPage(QWidget):
#     '''用户注册，登录窗口'''
#
# class Designer(QMainWindow, ui.system.Ui_systemClass):
#
#     def __init__(self):
#         super().__init__()
#         # self.initUI()
#         # self.setupUi(self)
#
#
#
#
#
#         self.label_0 = QLabel('用户登录页面')
#         # 设置label控件居中
#         self.label_0.setAlignment(Qt.AlignCenter)
#         # 设置字体样式
#         self.label_0.setFont(QFont('宋体', 12, QFont.Bold))
#         self.name_label = QLabel('用户名')
#         self.password_label = QLabel('密码')
#         # 单行文本输入框控件
#         self.name_line = QLineEdit()
#         self.password_line = QLineEdit()
#         # 单行文本输入框初始化
#         self.line_init()
#         # 按钮
#         self.login_button = QPushButton('登录')
#         self.register_button = QPushButton('注册')
#         self.exit_button = QPushButton('退出')
#         # 设置用户登录界面状态控件,复选框控件
#         self.remember_name = QCheckBox('记住用户名')
#         self.remember_password = QCheckBox('记住密码')
#         self.auto_login = QCheckBox('自动登录')
#         # 复选框初始化
#         self.checkbox_init()
#         # 按钮初始化方法
#         self.pushbutton_init()
#         # 布局管理器
#         self.h1_layout = QHBoxLayout()  # 水平布局管理器
#         self.h2_layout = QHBoxLayout()
#         self.grid_layout = QGridLayout()  # 网格布局管理器
#         self.v_layout = QVBoxLayout()  # 垂直布局管理器
#         # 页面布局初始化
#         self.layout_init()
#
#     # 页面布局初始化方法
#     def layout_init(self):
#         # 网格布局管理器
#         self.grid_layout.setSpacing(20)
#         self.grid_layout.addWidget(self.name_label, 0, 0, 1, 1)
#         self.grid_layout.addWidget(self.name_line, 0, 1, 1, 1)
#         self.grid_layout.addWidget(self.password_label, 1, 0, 1, 1)
#         self.grid_layout.addWidget(self.password_line, 1, 1, 1, 1)
#         # 水平布局布局管理器 1
#         self.h1_layout.addWidget(self.login_button)
#         self.h1_layout.addWidget(self.register_button)
#         self.h1_layout.addWidget(self.exit_button)
#         # 水平布局管理器 2
#         self.h2_layout.addStretch(1)
#         self.h2_layout.addWidget(self.remember_name)
#         self.h2_layout.addWidget(self.remember_password)
#         self.h2_layout.addWidget(self.auto_login)
#         # 垂直布局管理器
#         self.v_layout.addStretch(1)
#         self.v_layout.addWidget(self.label_0)
#         self.v_layout.addSpacing(10)
#         self.v_layout.addLayout(self.grid_layout)
#         self.v_layout.addSpacing(10)
#         self.v_layout.addLayout(self.h2_layout)
#         self.v_layout.addSpacing(10)
#         self.v_layout.addLayout(self.h1_layout)
#         self.v_layout.addStretch(1)
#         # 设置最终布局
#         self.setLayout(self.v_layout)
#         # 登录页面初始化状态
#         self.login_init()
#
#     # 单行文本输入框初始化方法
#     def line_init(self):
#         # 设置提示语
#         self.name_line.setPlaceholderText('在此输入用户名')
#         self.password_line.setPlaceholderText('在此输入密码')
#         # 设置用户密码以掩码显示
#         # self.password_line.setEchoMode(QLineEdit.Password)
#         # 设置用户在输入时明文显示，控件焦点转移后掩码显示
#         self.password_line.setEchoMode(QLineEdit.PasswordEchoOnEdit)
#         # 设置检查单行文本输入框输入状态
#         self.name_line.textChanged.connect(self.check_input)
#         self.password_line.textChanged.connect(self.check_input)
#
#     # 按钮初始化方法
#     def pushbutton_init(self):
#         # 先设置登录按钮为不可点击状态，当用户输入用户名及密码时才变为可点击状态
#         self.login_button.setEnabled(False)
#         # 登录按钮点击信号绑定槽函数
#         self.login_button.clicked.connect(self.do_login)
#         # 注册按钮点击信号绑定槽函数
#         self.register_button.clicked.connect(self.do_register)
#         # 退出按钮点击信号绑定槽函数
#         self.exit_button.clicked.connect(self.close)
#
#     # 复选框初始化
#     def checkbox_init(self):
#         # 将三个复选框按钮状态变化信号分别绑定对应槽函数
#         self.remember_name.stateChanged.connect(
#             self.remember_name_func)
#         self.remember_password.stateChanged.connect(
#             self.remember_password_func)
#         self.auto_login.stateChanged.connect(self.auto_login_func)
#
#     # 检查文本输入框方法
#     def check_input(self):
#         # 当用户名及密码输入框均有内容时，设置登录按钮为可点击状态，或者不可点击。
#         if self.name_line.text() and self.password_line.text():
#             self.login_button.setEnabled(True)
#         else:
#             self.login_button.setEnabled(False)
#
#     # 登录方法
#     # 在登录方法中，检查用户设置的登录状态
#     def do_login(self):
#         # 获取用户输入的用户名及密码
#         name, password = self.name_line.text(), self.password_line.text()
#         # 向服务端发送登录请求
#         # ----这边先以读取一个本地文件作为试验，模拟登录系统----
#         try:
#             # 用Python自带模块pickle来进行文件读取操作，以rb方式读取文件
#             with open('../data/users.pkl', 'rb') as f:
#                 users = pickle.load(f)
#         except:
#             QMessageBox.warning(self, '警告', '暂无用户数据！请先注册！')
#             return
#         # -----------------模拟登录-----------------------
#         if name in users.keys():
#             if password == users[name][0]:
#                 # 检查用户登录状态
#                 self.check_login_state()
#                 QMessageBox.information(self, '提示', '登录成功！')
#             else:
#                 QMessageBox.warning(self, '警告', '密码错误！')
#         else:
#             QMessageBox.warning(self, '警告', '用户不存在！')
#
#     # 用户注册方法
#     def do_register(self):
#         # 向服务端发送注册请求，
#         # ----这边也以一个文件读取操作，模拟登录系统----
#         register_page = RegisterPage()
#         # 注册页面的注册成功信号绑定，在登录页面输入注册成功后的用户ID及密码
#         register_page.successful_signal.connect(self.successful_func)
#         register_page.exec()
#
#     # 注册成功方法
#     def successful_func(self, data):
#         print(data)
#         # 将注册成功数据写入登录页面
#         self.name_line.setText(data[0])
#         self.password_line.setText(data[1])
#
#     # 登录界面，记住用户名方法
#     def remember_name_func(self):
#         if self.remember_name.isChecked():
#             name = self.name_line.text()
#             with open('./temp/login.pkl', 'wb') as f:
#                 pickle.dump(name, f)
#         else:
#             with open('./temp/login.pkl', 'wb') as f:
#                 pickle.dump(0, f)
#
#     # 登录界面，记住密码方法
#     def remember_password_func(self):
#         if self.remember_password.isChecked():
#             # 用户点击记住密码，用户名也必须记住，
#             # 所以记住用户名按钮也需被选中。
#             self.remember_name.setChecked(True)
#             # 登录界面信息。
#             data = [self.name_line.text(), self.password_line.text()]
#             with open('./temp/login.pkl', 'wb') as f:
#                 pickle.dump(data, f)
#
#     # 登录界面，自动登录方法、
#     def auto_login_func(self):
#         if self.auto_login.isChecked():
#             data = [self.name_line.text(), self.password_line.text()]
#             with open('./temp/auto.pkl', 'wb') as f:
#                 pickle.dump(data, f)
#
#     # 登录页面信息初始化方法
#     def login_init(self):
#         # 尝试读取记住用户名，或记住用户密码保存文件数据
#         try:
#             with open('./temp/login.pkl', 'rb') as f:
#                 data = pickle.load(f)
#             # 判断数据类型,
#             # 如果是字符串，及仅选中了记住用户名复选框
#             if isinstance(data, str):
#                 self.name_line.setText(data)
#                 self.remember_name.setChecked(True)
#             else:
#                 self.name_line.setText(data[0])
#                 self.password_line.setText(data[1])
#                 self.remember_name.setChecked(True)
#                 self.remember_password.setChecked(True)
#         except:
#             pass
#         # 尝试读取自动登录保存文件数据
#         try:
#             with open('./temp/auto.pkl', 'rb') as f:
#                 data2 = pickle.load(f)
#             self.name_line.setText(data2[0])
#             self.password_line.setText(data2[1])
#             # 调用登录方法
#             self.do_login()
#         except:
#             pass
#
#     # 检查用户登录状态方法
#     def check_login_state(self):
#         self.remember_name_func()
#         self.remember_password_func()
#         self.auto_login_func()
#
#
# # 注册对话框
# class RegisterPage(QDialog):
#     # 自定义注册成功信号,传递列表信息
#     successful_signal = pyqtSignal(list)
#
#     def __init__(self):
#         super(RegisterPage, self).__init__()
#         self.setWindowTitle('用户注册')
#         self.setWindowIcon(QIcon('../image/title.png'))
#         # 设置窗口显示位置
#         self.move(900, 400)
#         self.setFixedSize(450, 250)
#         self.label_0 = QLabel('欢迎注册')
#         self.label_0.setFont(QFont('宋体', 12, QFont.Bold))
#         self.label_0.setAlignment(Qt.AlignCenter)
#         self.name_label = QLabel('用户ID：')
#         self.password1_label = QLabel('用户密码：')
#         self.password2_label = QLabel('重复密码：')
#         # 其他用户信息label控件
#         self.nick_label = QLabel('昵称：')
#         self.gender_label = QLabel('性别：')
#         # 单行文本输入框
#         self.name_line = QLineEdit()
#         self.password1_line = QLineEdit()
#         # 再次输入密码的单行文本输入款为自定义的文本输入框
#         self.password2_line = MyLineEdit()
#         self.nick_line = QLineEdit()
#         # 性别单选框
#         self.male_button = QRadioButton('男')
#         self.female_button = QRadioButton('女')
#         # 单行文本输入框初始化
#         self.line_init()
#         # 用户其他信息控件尺寸调整
#         self.modify_widget()
#         # 按钮
#         self.register_button = QPushButton('注册')
#         self.cancel_button = QPushButton('取消')
#         # 按钮初始化方法
#         self.pushbutton_init()
#         # 布局管理器
#         self.h1_layout = QHBoxLayout()
#         self.h2_layout = QHBoxLayout()
#         self.grid_layout = QGridLayout()
#         self.v_layout = QVBoxLayout()
#         # 页面布局初始化
#         self.layout_init()
#
#     # 页面布局初始化方法
#     def layout_init(self):
#         # 网格布局
#         # 设置网格布局中控件间距
#         self.grid_layout.setSpacing(20)
#         self.grid_layout.addWidget(self.name_label, 0, 0, 1, 1)
#         self.grid_layout.addWidget(self.name_line, 0, 1, 1, 1)
#         self.grid_layout.addWidget(self.password1_label, 1, 0, 1, 1)
#         self.grid_layout.addWidget(self.password1_line, 1, 1, 1, 1)
#         self.grid_layout.addWidget(self.password2_label, 2, 0, 1, 1)
#         self.grid_layout.addWidget(self.password2_line, 2, 1, 1, 1)
#         # 水平布局1
#         self.h1_layout.addWidget(self.register_button)
#         self.h1_layout.addWidget(self.cancel_button)
#         # 水平布局2
#         self.h2_layout.addWidget(self.nick_label)
#         self.h2_layout.addSpacing(12)
#         self.h2_layout.addWidget(self.nick_line)
#         self.h2_layout.addSpacing(10)
#         self.h2_layout.addWidget(self.gender_label)
#         self.h2_layout.addWidget(self.male_button)
#         self.h2_layout.addWidget(self.female_button)
#         # 垂直布局
#         self.v_layout.addStretch(1)
#         self.v_layout.addWidget(self.label_0)
#         self.v_layout.addSpacing(10)
#         self.v_layout.addLayout(self.grid_layout)
#         self.v_layout.addSpacing(10)
#         self.v_layout.addLayout(self.h2_layout)
#         self.v_layout.addSpacing(10)
#         self.v_layout.addLayout(self.h1_layout)
#         self.v_layout.addStretch(1)
#         # 设置最终布局
#         self.setLayout(self.v_layout)
#
#     # 控件尺寸调整方法
#     def modify_widget(self):
#         self.nick_label.setMinimumWidth(60)
#         self.nick_line.setMaximumWidth(150)
#
#     # 单行文本输入框初始化方法
#     # 3个单行文本输入框都绑定检查用户输入槽函数
#     # 设置用户密码显示方式：正在输入时明文，焦点转移后掩码
#     # 注册提示
#     # 设置文本校验器
#     # 检查密码合法性
#     def line_init(self):
#         # 单行文本输入框内容变化绑定按钮显示
#         self.name_line.textChanged.connect(self.check_input)
#         self.password1_line.textChanged.connect(self.check_input)
#         self.password2_line.textChanged.connect(self.check_input)
#         # 设置密码显示方式
#         self.password1_line.setEchoMode(QLineEdit.PasswordEchoOnEdit)
#         self.password2_line.setEchoMode(QLineEdit.PasswordEchoOnEdit)
#         # 注册提示
#         self.name_line.setPlaceholderText('输入用户名，字母数字，不可为中文或特殊字符。')
#         self.password1_line.setPlaceholderText('密码为6到10位数字字母，首字母必须为大写。')
#         self.password2_line.setPlaceholderText('请再次确认密码！')
#         # 设置文本框校验器
#         # 姓名文本框校验器设置
#         # 1、创建正则表达式限定输入内容
#         name_RegExp = QRegExp("[0-9A-Za-z]*")
#         # 2、创建文本框校验器
#         name_validator = QRegExpValidator(name_RegExp)
#         # 3、文本输入框绑定创建的校验器
#         self.name_line.setValidator(name_validator)
#         # 设置密码文本输入框校验器
#         password_val = QRegExpValidator(QRegExp("^[A-Z][0-9A-Za-z]{10}$"))
#         self.password1_line.setValidator(password_val)
#         self.password2_line.setValidator(password_val)
#         # 检查密码输入,验证密码输入位数，两次密码输入是否一致。
#         self.password2_line.focus_out.connect(self.check_password)
#
#     # 按钮初始化方法
#     def pushbutton_init(self):
#         # 设置注册按钮为不可点击状态，绑定槽函数
#         self.register_button.setEnabled(False)
#         self.register_button.clicked.connect(self.register_func)
#         # 取消按钮绑定取消注册槽函数
#         self.cancel_button.clicked.connect(self.cancel_func)
#
#     # 检查输入方法,只有在三个文本输入框都有文字时，注册按钮才为可点击状态
#     def check_input(self):
#         if (self.name_line.text() and self.password1_line.text()
#                 and self.password2_line.text()):
#             self.register_button.setEnabled(True)
#         else:
#             self.register_button.setEnabled(False)
#
#     # 取消注册方法
#     # 如果用户在注册界面输入了数据，提示用户是否确认取消注册，如未输入数据则直接退出。
#     def cancel_func(self):
#         if (self.name_line.text() or self.password1_line.text()
#                 or self.password2_line.text()):
#             choice = QMessageBox.information(self, '提示', '是否取消注册？',
#                                              QMessageBox.Yes | QMessageBox.No)
#             if choice == QMessageBox.Yes:
#                 self.close()
#             else:
#                 return
#         else:
#             self.close()
#
#     # 检查用户输入密码合法性方法
#     def check_password(self):
#         password_1 = self.password1_line.text()
#         password_2 = self.password2_line.text()
#
#         if len(password_1) < 6:
#             QMessageBox.warning(self, '警告', '密码位数小于6')
#             self.password1_line.setText('')
#             self.password2_line.setText('')
#         else:
#             if password_1 == password_2:
#                 pass
#             else:
#                 QMessageBox.warning(self, '警告', '两次密码输入结果不一致！')
#                 self.password1_line.setText('')
#                 self.password2_line.setText('')
#
#     # 用户注册方法
#     def register_func(self):
#         # 先获取注册用户ID，检查用户ID是否存在
#         ID = self.name_line.text()
#         try:
#             with open('../data/users.pkl', 'rb') as f1:
#                 users = pickle.load(f1)
#         except:
#             users = {}
#
#         # 如果用户ID已存在，提示用户ID已被注册
#         if ID in users.keys():
#             QMessageBox.information(self, '提示', '该用户ID已被注册！')
#         # 否则收集用户注册信息
#         else:
#             gender = self.gender_data()
#             user_data = [self.password1_line.text(),
#                          self.nick_line.text(),
#                          gender]
#             # 写入用户信息字典
#             users[ID] = user_data
#             with open('../data/users.pkl', 'wb') as f2:
#                 pickle.dump(users, f2)
#             # 提醒用户注册成功，询问是否登录
#             choice = QMessageBox.information(self, '提示', '注册成功，是否登录？',
#                                              QMessageBox.Yes | QMessageBox.No)
#             # 如选择是，关闭注册页面，并在登录页面用户ID显示注册ID,密码
#             if choice == QMessageBox.Yes:
#                 self.successful_signal.emit([self.name_line.text(),
#                                              self.password1_line.text()])
#                 self.close()
#             # 如选择否，直接关闭注册页面。
#             else:
#                 self.close()
#
#     # 用户性别信息收集,男为1，女为2，未选择为0
#     def gender_data(self):
#         if self.male_button.isChecked():
#             gender = 1
#         elif self.female_button.isChecked():
#             gender = 2
#         else:
#             gender = 0
#         return gender
#
#
# # 自定义一单行文本输入框，重写焦点转移事件,让焦点转移时发出一个自定义信号。
# class MyLineEdit(QLineEdit):
#     focus_out = pyqtSignal(str)
#
#     def focusOutEvent(self, QFocusEvent):
#         super(MyLineEdit, self).focusOutEvent(QFocusEvent)
#         self.focus_out.emit(self.text())
#
#
# if __name__ == '__main__':
#     page = QApplication(sys.argv)
#     # 实例父页面
#     window = LoginPage()
#     window.show()
#     sys.exit(page.exec())
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainWindow = QMainWindow()
#     ui = ui.system.Ui_systemClass()  # 类的初始化
#     ui.setupUi(mainWindow)  # 传对象
#     mainWindow.show()