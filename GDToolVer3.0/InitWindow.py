from NewGDToolMainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow


class InitWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
