import sys
from PyQt5.QtWidgets import QWidget,QApplication,QListView

class TestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.uiInit()

    def uiInit(self):
        self.list = QListView(self)
        # self.list.seti
        self.setGeometry(300,300,640,480)
        self.setWindowTitle('测试用的窗口')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tw = TestWindow()
    sys.exit(app.exec_())