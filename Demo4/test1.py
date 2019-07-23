import sys
from PyQt5.QtWidgets import *


class Test1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.setFixedSize(600, 400)
        self.btn = QPushButton('启动', self)
        self.txedit = QPlainTextEdit(self)
        vbox = QVBoxLayout()
        vbox.addWidget(self.btn, 1)
        vbox.addWidget(self.txedit, 1)
        obj = QWidget()
        obj.setLayout(vbox)
        self.setCentralWidget(obj)

        self.btn.clicked.connect(self.testTXT)

        self.show()

    def testTXT(self):
        for i in range(3000):
            self.txedit.appendPlainText('第{0}行输出'.format(str(i)))
            QApplication.processEvents()
        self.statusBar().showMessage('complete')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Test1()
    sys.exit(app.exec_())
