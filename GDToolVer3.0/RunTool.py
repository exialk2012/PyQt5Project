import sys
from  PyQt5.QtWidgets import QApplication
from InitWindow import InitWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = InitWindow()
    sys.exit(app.exec_())