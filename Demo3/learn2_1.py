from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Example3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.resize(640, 480)
        self.setFixedSize(640, 480)

        self.lbText1 = QLabel('这个是第一行的文本', self)
        self.edit1 = QLineEdit(self)
        self.lbText2 = QLabel('这个是第二行的文本', self)
        self.edit2 = QLineEdit(self)
        self.btn1 = QPushButton('按钮1', self)
        self.btn2 = QPushButton('按钮2', self)
        self.btn3 = QPushButton('按钮3', self)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.lbText1)
        hbox1.addWidget(self.edit1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.lbText2)
        hbox2.addWidget(self.edit2)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(5)
        hbox3.addWidget(self.btn1)
        hbox3.addStretch(2)
        hbox3.addWidget(self.btn2)
        hbox3.addStretch(2)
        hbox3.addWidget(self.btn3)
        hbox3.addStretch(5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addStretch(2)
        vbox.addLayout(hbox2)
        vbox.addStretch(10)
        vbox.addLayout(hbox3)
        vbox.addStretch(10)

        self.setLayout(vbox)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    exm3 = Example3()
    sys.exit(app.exec_())
