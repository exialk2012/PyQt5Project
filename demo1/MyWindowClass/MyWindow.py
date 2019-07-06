from PyQt5.QtWidgets import QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.uiInit()

    def uiInit(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('不错的窗口')

        self.show()