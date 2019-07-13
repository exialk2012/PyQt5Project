import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Example4(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 150)
        self.setWindowTitle('进度条练习')

        self.lb = QLabel('数量：', self)
        self.lb.move(20, 40)

        self.btn = QPushButton('开始', self)
        self.btn.move(20, 80)

        self.edit = QLineEdit('100000', self)
        self.edit.move(100, 40)

        self.show()

        self.btn.clicked.connect(self.showProcessDialog)

    def showProcessDialog(self):
        num = int(self.edit.text())
        process = QProgressDialog(self)
        process.setWindowTitle('请稍等')
        process.setLabelText('正在处理中……')
        process.setCancelButtonText('取消')
        process.setMinimumDuration(5)
        process.setWindowModality(Qt.WindowModal)
        process.setRange(0, num)
        for i in range(num):
            process.setValue(i)
            if process.wasCanceled():
                QMessageBox.warning(self, '警告', '操作失败')
                break

        else:
            process.setValue(num)
            QMessageBox.information(self, '提示', '操作成功')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex4 = Example4()
    sys.exit(app.exec_())
