from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle('引导工具')
        self.setWindowIcon(QIcon(r'E:\PyQt Project\PyQt5Project\GDToolsVerson_1\icon.ico'))

        self.mb = QMenuBar(self)
        self.mb.resize(800, 25)
        self.comm_menu = QMenu('通用(&c)', self)
        self.mb.addMenu(self.comm_menu)
        self.save_act = QAction('保存(&s)', self)
        self.comm_menu.addAction(self.save_act)
        self.comm_menu.addSeparator()
        self.exit_act = QAction('退出(&q)', self)
        self.comm_menu.addAction(self.exit_act)

        self.exit_act.toggled.connect(self.close)

        self.show()
