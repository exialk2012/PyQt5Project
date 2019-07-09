from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 330, 300)
        self.setWindowTitle('MessageBox示例')

        self.lbl = QLabel('这里是显示的内容', self)
        self.lbl.move(20, 20)

        self.bt1 = QPushButton('提示', self)
        self.bt1.move(20, 50)
        self.bt2 = QPushButton('询问', self)
        self.bt2.move(120, 50)
        self.bt3 = QPushButton('警告', self)
        self.bt3.move(220, 50)
        self.bt4 = QPushButton('错误', self)
        self.bt4.move(20, 100)
        self.bt5 = QPushButton('关于', self)
        self.bt5.move(120, 100)
        self.bt6 = QPushButton('关于QT', self)
        self.bt6.move(220, 100)

        self.bt1.clicked.connect(self.info)
        self.bt2.clicked.connect(self.question)
        self.bt3.clicked.connect(self.warning)
        self.bt4.clicked.connect(self.critical)
        self.bt5.clicked.connect(self.about)
        self.bt6.clicked.connect(self.aboutqt)

        self.show()

    def info(self):
        reply = QMessageBox.information(self, '提示框', '你看到了这串内容了吧', QMessageBox.Ok | QMessageBox.Close,
                                        QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.lbl.setText('你选择了OK')
        else:
            self.lbl.setText('你选择了Close')

    def question(self):
        reply = QMessageBox.question(self, '询问', '这是一个询问消息对话框，默认是No',
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.lbl.setText('你选择了Yes！')
        elif reply == QMessageBox.No:
            self.lbl.setText('你选择了No！')
        else:
            self.lbl.setText('你选择了Cancel！')

    def warning(self):
        cb = QCheckBox('你是否要打勾')
        msb = QMessageBox()
        msb.setWindowTitle('警告')
        msb.setIcon(QMessageBox.Warning)
        msb.setText('这是一个警告对话框')
        msb.setInformativeText('出现变更，是否愿意保存？')
        save = msb.addButton('保存', QMessageBox.AcceptRole)
        nosave = msb.addButton('不保存', QMessageBox.RejectRole)
        cancle = msb.addButton('取消', QMessageBox.DestructiveRole)
        msb.setDefaultButton(save)
        msb.setCheckBox(cb)
        cb.stateChanged.connect(self.check)
        reply = msb.exec_()
        if reply == QMessageBox.AcceptRole:
            self.lbl.setText('你选择了保存！')
        elif reply == QMessageBox.RejectRole:
            self.lbl.setText('你选择了不保存！')
        else:
            self.lbl.setText('你选择了取消！')

    def check(self):
        if self.sender().isChecked():
            self.lbl.setText('你打勾了哦')
        else:
            self.lbl.setText('怎么又不打了啊')

    def critical(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('错误')
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("这是一个错误消息对话框")
        msgBox.setStandardButtons(QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore)
        msgBox.setDefaultButton(QMessageBox.Retry)
        # msgBox.setDetailedText('这是详细的信息：学点编程吧，我爱你！')
        reply = msgBox.exec()

        if reply == QMessageBox.Retry:
            self.lbl.setText('你选择了Retry！')
        elif reply == QMessageBox.Abort:
            self.lbl.setText('你选择了Abort！')
        else:
            self.lbl.setText('你选择了Ignore！')

    def about(self):
        # QMessageBox.about(self,'关于','这是一个关于消息对话框!')
        msgBox = QMessageBox(QMessageBox.NoIcon, '关于', '不要意淫了，早点洗洗睡吧!')
        msgBox.setIconPixmap(QPixmap(r"E:\PyQt Project\PyQt5Project\Demo3\2.PNG"))
        msgBox.exec()

    def aboutqt(self):
        QMessageBox.aboutQt(self, '关于Qt')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
