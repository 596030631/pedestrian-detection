import pickle

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from management import Ui_management


class ManagerDesigner(QMainWindow, Ui_management):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initEvent()

    def initEvent(self):
        print("event")
        self.buttonCLear.clicked.connect(self.clear)
        self.buttonSure.clicked.connect(self.button_sure)
        self.buttonSure.clicked.connect(self.commit_password)

    def commit_password(self):
        print("commit_password")
        self.check_password()

    def check_password(self):
        password_1 = self.password.text()
        password_2 = self.password_2.text()
        if len(password_1) < 6 or len(password_2) < 6:
            QMessageBox.warning(None, '警告', '密码位数小于6')
            self.password.setText('')
            self.password_2.setText('')
        else:
            self.update_passwd()

    # 用户注册方法
    def update_passwd(self):
        # 先获取注册用户ID，检查用户ID是否存在
        ID = self.userId.text()
        try:
            with open('users.pkl', 'rb') as f1:
                users = pickle.load(f1)
        except:
            users = {}

        # 如果用户ID已存在，提示用户ID已被注册
        if ID not in users.keys():
            QMessageBox.information(None, '提示', '用户ID NOT FOUND！')
        # 否则收集用户注册信息
        else:
            print("cunzai")
            passwdOld = users[ID][0]
            print(passwdOld)
            if passwdOld == self.password.text():
                user_data = [self.password_2.text(),
                             self.password_2.text()]
                # 写入用户信息字典
                users[ID] = user_data
                with open('users.pkl', 'wb') as f2:
                    pickle.dump(users, f2)
                # 提醒用户注册成功，询问是否登录
                QMessageBox.information(None, '提示', '成功', QMessageBox.No)
            else:
                QMessageBox.information(None, '提示', 'passwd error', QMessageBox.No)

    def clear(self):
        self.userId.setText("")
        self.password.setText("")
        self.password_2.setText("")

    def button_sure(self):
        print("sure")
