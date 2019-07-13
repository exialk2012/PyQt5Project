import sys
from GDMainWin import GDMain
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon(r'E:\PyQt5Project\GDToolVer2.0\icon.ico'))
    gd = GDMain()
    sys.exit(app.exec_())