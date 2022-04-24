# # 注册对话框
# import pickle
#
# from PyQt5.QtCore import pyqtSignal, Qt, QRegExp
# from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
# from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QRadioButton, QPushButton, QHBoxLayout, QGridLayout, \
#     QVBoxLayout, QMessageBox
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
# class RegisterQDialog(QDialog):
#     # 自定义注册成功信号,传递列表信息
#     successful_signal = pyqtSignal(list)
#
#     def __init__(self):
#         super(RegisterQDialog, self).__init__()
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
#             with open('users.pkl', 'rb') as f1:
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
#             with open('users.pkl', 'wb') as f2:
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
