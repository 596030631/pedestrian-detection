import pickle

from PyQt5.QtWidgets import QMessageBox


def userLogin(self, name, password):
    print("login")
    # 获取用户输入的用户名及密码
    # 向服务端发送登录请求
    # ----这边先以读取一个本地文件作为试验，模拟登录系统----
    try:
        # 用Python自带模块pickle来进行文件读取操作，以rb方式读取文件
        with open('users.pkl', 'rb') as f:
            users = pickle.load(f)
    except:
        QMessageBox.warning(None, '警告', '暂无用户数据！请先注册！')
        print("请先注册，暂无用户数据")
        return
    # -----------------模拟登录-----------------------
    if name in users.keys():
        if password == users[name][0]:
            # 检查用户登录状态
            # self.check_login_state()
            print("登录成功")
            QMessageBox.information(None, '提示', '登录成功！')
            self.LoginSuccessfulCallback()
        else:
            QMessageBox.warning(None, '警告', '密码错误！')
            print("密码错误")
    else:
        QMessageBox.warning(None, '警告', '用户不存在！')
        print("用户不存在")


def registerSuccessful():
    print("注册成功")



def userRegister():
    print("用户注册")