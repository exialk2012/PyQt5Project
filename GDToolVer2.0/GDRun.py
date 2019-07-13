import sys
from GDMainWin import GDMain
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gd = GDMain()
    sys.exit(app.exec_())