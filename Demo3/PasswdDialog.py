from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class PasswdDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.resize(350, 100)
        self.setWindowTitle('密码3')
        self.lb = QLabel('请输入密码', self)

        self.edit = QLineEdit(self)
        self.edit.installEventFilter(self)

        self.bt1 = QPushButton('OK', self)
        self.bt2 = QPushButton('Cancel', self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.bt1)
        hbox.addStretch(1)
        hbox.addWidget(self.bt2)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addWidget(self.edit)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.edit.setContextMenuPolicy(Qt.NoContextMenu)
        self.edit.setPlaceholderText('密码不超15位，只能有数字和字母，必须以字母开头')
        self.edit.setEchoMode(QLineEdit.Password)

        regx = QRegExp('^[a-zA-z][0-9A-Za-z]{14}$')
        validetor = QRegExpValidator(regx, self.edit)
        self.edit.setValidator(validetor)

        self.bt1.clicked.connect(self.ok)
        self.bt2.clicked.connect(self.cancel)

        object = QObject()

    def eventFilter(self, object, event):
        if object == self.edit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(
                        QKeySequence.Paste):
                    return True
            return QDialog.eventFilter(self, object, event)

    def ok(self):
        self.text = self.edit.text()
        if len(self.text) == 0:
            QMessageBox.warning(self, '警告', '密码不能为空')
        elif len(self.text) < 6:
            QMessageBox.warning(self, '警告', '密码不能少于6位')
        else:
            self.done(1)

    def cancel(self):
        self.done(0)
