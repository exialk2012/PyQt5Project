from PyQt5.QtWidgets import QWidget,QLCDNumber

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.uiInit()

    def uiInit(self):
        self.value = 0
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('不错的窗口')

        self.lcd = QLCDNumber(self)

        self.show()

    def mousePressEvent(self, e):
        self.value += 1
        self.lcd.display(self.value)