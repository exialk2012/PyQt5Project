import sys
from MyWindowClass.MyWindow import MyWindow
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MyWindow()
    sys.exit(app.exec_())


