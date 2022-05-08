# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'management.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_management(object):
    def setupUi(self, management):
        management.setObjectName("management")
        management.resize(800, 650)
        management.setMinimumSize(QtCore.QSize(800, 650))
        management.setMaximumSize(QtCore.QSize(800, 650))
        management.setStyleSheet("*{\n"
"font-size:24px;\n"
"font-family:sans-serif;\n"
"}\n"
"#management{  \n"
"    border-image: url(:/pic/images/re.png)\n"
"\n"
"}\n"
"QFrame{\n"
"background:rgba(0,0,0,0.8);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton{\n"
"background:#03a9f4;\n"
"color:#fff;\n"
"border-radius:15px;\n"
"}\n"
"QLineEdit{\n"
"border-radius:15px;\n"
"color:#03a9f4;\n"
"}\n"
"QLabel{\n"
"color:#fff;\n"
"background:transparent;\n"
"font-size:30px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(management)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(100, 60, 601, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 221, 61))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 120, 141, 31))
        self.label.setStyleSheet("font: 16pt \"楷体\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 141, 31))
        self.label_3.setStyleSheet("font: 16pt \"楷体\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 260, 141, 31))
        self.label_4.setStyleSheet("font: 16pt \"楷体\";")
        self.label_4.setObjectName("label_4")
        self.userId = QtWidgets.QLineEdit(self.frame)
        self.userId.setGeometry(QtCore.QRect(190, 110, 341, 41))
        self.userId.setToolTipDuration(-1)
        self.userId.setStyleSheet("font: 14pt \"楷体\";")
        self.userId.setText("")
        self.userId.setObjectName("userId")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(190, 180, 341, 41))
        self.password.setStyleSheet("font: 14pt \"楷体\";")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.buttonSure = QtWidgets.QPushButton(self.frame)
        self.buttonSure.setGeometry(QtCore.QRect(50, 340, 151, 41))
        self.buttonSure.setObjectName("buttonSure")
        self.buttonCLear = QtWidgets.QPushButton(self.frame)
        self.buttonCLear.setGeometry(QtCore.QRect(220, 340, 151, 41))
        self.buttonCLear.setObjectName("buttonCLear")
        self.buttonCancel = QtWidgets.QPushButton(self.frame)
        self.buttonCancel.setGeometry(QtCore.QRect(390, 340, 151, 41))
        self.buttonCancel.setObjectName("buttonCancel")
        self.password_2 = QtWidgets.QLineEdit(self.frame)
        self.password_2.setGeometry(QtCore.QRect(190, 250, 341, 41))
        self.password_2.setStyleSheet("font: 14pt \"楷体\";")
        self.password_2.setText("")
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_2.setObjectName("password_2")
        self.pushButton_exit = QtWidgets.QPushButton(self.frame)
        self.pushButton_exit.setGeometry(QtCore.QRect(50, 430, 491, 41))
        self.pushButton_exit.setObjectName("pushButton_exit")
        management.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(management)
        self.statusbar.setObjectName("statusbar")
        management.setStatusBar(self.statusbar)

        self.retranslateUi(management)
        QtCore.QMetaObject.connectSlotsByName(management)

    def retranslateUi(self, management):
        _translate = QtCore.QCoreApplication.translate
        management.setWindowTitle(_translate("management", "MainWindow"))
        self.label_2.setText(_translate("management", "账户管理"))
        self.label.setText(_translate("management", "用户名ID："))
        self.label_3.setText(_translate("management", "原密码："))
        self.label_4.setText(_translate("management", "修改密码："))
        self.userId.setToolTip(_translate("management", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\',\'monospace\'; font-size:10pt; color:#000000;\">输入用户名，字母数字，不可为中文或特殊字符。</span></p></body></html>"))
        self.userId.setPlaceholderText(_translate("management", "输入用户名，字母数字，不可为中文或特殊字符。"))
        self.password.setToolTip(_translate("management", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">密码为6到10位数字字母，首字母必须为大写。</span></p></body></html>"))
        self.password.setPlaceholderText(_translate("management", "密码为6到10位数字字母，首字母必须为大写"))
        self.buttonSure.setText(_translate("management", "确认修改"))
        self.buttonCLear.setText(_translate("management", "重  填"))
        self.buttonCancel.setText(_translate("management", "取  消"))
        self.password_2.setToolTip(_translate("management", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">密码为6到10位数字字母，首字母必须为大写。</span></p></body></html>"))
        self.password_2.setPlaceholderText(_translate("management", "密码为6到10位数字字母，首字母必须为大写"))
        self.pushButton_exit.setText(_translate("management", "退出登录"))
