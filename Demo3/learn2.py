import sys
from PasswdDialog import PasswdDialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.resize(380, 180)
        self.setFixedSize(380, 180)
        self.setWindowTitle('密码窗口的练习')

        self.lb1 = QLabel('这里显示密码', self)
        self.lb1.move(20, 20)

        self.bt1 = QPushButton('输入密码1', self)
        self.bt1.move(20, 60)
        self.bt2 = QPushButton('输入密码2', self)
        self.bt2.move(150, 60)
        self.bt3 = QPushButton('输入密码3', self)
        self.bt3.move(280, 60)

        self.show()

        self.bt1.clicked.connect(self.showPassWordDialog)
        self.bt2.clicked.connect(self.showPassWordDialog)
        self.bt3.clicked.connect(self.showPassWordDialog)

    def showPassWordDialog(self):
        sender = self.sender()
        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, '密码1', '请输入密码：', QLineEdit.Password)
            if ok:
                self.lb1.setText(text)

        elif sender == self.bt2:
            text, ok = QInputDialog.getText(self, '密码2', '请输入密码：', QLineEdit.PasswordEchoOnEdit)
            if ok:
                self.lb1.setText(text)

        else:
            pwd = PasswdDialog()
            r = pwd.exec_()
            if r:
                self.lb1.setText(pwd.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex2 = Example2()
    sys.exit(app.exec_())
