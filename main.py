# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.py'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from login import *

class login(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(login, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.end_event)  # 绑定登陆函数
        self.pushButton_2.clicked.connect(self.exit)  # 绑定退出函数

    # 登陆函数
    def end_event(self):
        login_user = self.lineEdit_3.text()
        login_password = self.lineEdit_4.text()
        if login_user == "zb666" and login_password == "123456":
            QMessageBox.about(self, '欢迎！', '登陆成功')
        else:
            QMessageBox.warning(self, '警告', '用户名或密码错误')

    # 退出函数
    def exit(self):
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = login()
    myWin.show()
    sys.exit(app.exec_())