import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class Example5(QWidget):
    def __init__(self):
        super(Example5, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('退出练习')
        self.resize(300,200)
        self.btn = QPushButton('退出', self)
        hbox = QHBoxLayout()
        hbox.addWidget(self.btn)
        self.setLayout(hbox)

        self.btn.clicked.connect(self.onClick_Button)
        self.show()

    def onClick_Button(self):
        sender = self.sender()
        print(sender.text())
        mapp = QApplication.instance()
        mapp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    exm5 = Example5()
    sys.exit(app.exec_())
