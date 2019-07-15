from PyQt5.QtWidgets import QWidget, QLCDNumber
from PyQt5.QtGui import QIcon


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.uiInit()

    def uiInit(self):
        self.value = 0
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('不错的窗口')
        self.setWindowIcon(QIcon('icon.ico'))

        self.lcd = QLCDNumber(self)

        self.show()

    def mousePressEvent(self, e):
        self.value += 1
        self.lcd.display(self.value)
