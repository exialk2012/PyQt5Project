import sys
from PyQt5.QtWidgets import QApplication
from GDToolMainWindow import GDToolMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = GDToolMainWindow()
    sys.exit(app.exec_())
