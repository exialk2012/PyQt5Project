from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json


class GDMain(QMainWindow):
    def __init__(self):
        super(GDMain, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口大小
        self.setFixedSize(800, 600)

        # 设置窗口标题
        self.setWindowTitle('引导工具 2.0')

        # 设置窗口的图标
        self.setWindowIcon(QIcon(r'..\GDToolVer2.0\icon.ico'))

        # 设置引导列树控件
        self.gdtreelabel = QLabel('引导节点列表')
        self.gdtree = QTreeWidget()

        # 设置状态栏启动文本
        # self.sb = QStatusBar()
        # self.sb.setStatusTip('启动成功')
        # self.setStatusBar(self.sb)
        # self.statuslabel = QLabel('启动成功')
        # self.statuslabel.resize(800,30)
        # self.statusBar().addWidget(self.statuslabel)
        self.statusBar().showMessage('启动成功', 3000)

        # 设置引导相关控件
        # 设置引导节点名与节点名输入框与插入按钮
        self.gdnamelabel = QLabel('GuideName')
        self.gdnameinputedit = QLineEdit()
        self.gdnameinputedit.setPlaceholderText('请输入引导节点名称')
        self.gdnameaddbtn = QPushButton('插入')
        self.gdnameaddbtn.setEnabled(False)
        self.gdnameaddbtn.clicked.connect(self.clickGDNameAdd)
        self.gdnamedelbtn = QPushButton('删除')
        self.gdnamedelbtn.setEnabled(False)
        self.gdnamedelbtn.clicked.connect(self.clickGDNameDel)
        self.gdnameinputedit.textChanged.connect(self.changeGDNameInputByLineText)

        # 设置引导文本显示相关
        self.gdnodecontent = {}
        self.gdnodeviewlabel = QLabel('引导文本预览:')
        self.gdnodeview = QTextEdit()
        self.gdnodeview.setReadOnly(True)
        self.gdnodeview.textChanged.connect(self.changSaveJsonByGDNodeView)

        # 设置保存引导json按钮相关
        self.gdjsonsavebtn = QPushButton('保存脚本')
        self.gdjsonsavebtn.setEnabled(False)
        self.gdjsonsavebtn.clicked.connect(self.clickGDJsonSave)

        # 设置布局
        # treeview相关布局
        hbox1 = QHBoxLayout()
        gdnodevbox = QVBoxLayout()
        # hbox.addStretch(1)
        gdnodevbox.addWidget(self.gdtreelabel)
        gdnodevbox.addWidget(self.gdtree)
        # hbox1.addLayout(gdnodevbox)

        # 引导节点名相关布局
        gdnamehbox = QHBoxLayout()
        gdnamehbox.addWidget(self.gdnamelabel)
        gdnamehbox.addWidget(self.gdnameinputedit)
        gdnamehbox.addWidget(self.gdnameaddbtn)
        gdnamehbox.addWidget(self.gdnamedelbtn)
        hbox1.addLayout(gdnamehbox)

        # 设置引导文本预览相关布局
        gdnodeviewvbox = QVBoxLayout()
        gdnodeviewvbox.addWidget(self.gdnodeviewlabel)
        gdnodeviewvbox.addWidget(self.gdnodeview)
        hbox1.addLayout(gdnodeviewvbox)

        # 设置保存脚本按钮相关布局
        savegdjsonhbox = QHBoxLayout()
        savegdjsonhbox.addStretch(10)
        savegdjsonhbox.addWidget(self.gdjsonsavebtn)
        gdnodeviewvbox.addLayout(savegdjsonhbox)

        objwidget = QWidget()
        objwidget.setLayout(hbox1)
        self.setCentralWidget(objwidget)
        self.show()

    def clickGDNameDel(self):
        self.gdnameinputedit.clear()
        self.statusBar().showMessage('已删除引导节点名', 3000)

    def clickGDNameAdd(self):
        self.gdnodecontent.update(GuideName=self.gdnameinputedit.text())
        self.gdnodeview.setText(str(self.gdnodecontent))
        self.statusBar().showMessage('添加引导名称成功', 3000)

    def clickGDJsonSave(self):
        if self.gdnodeview.toPlainText() != '' and self.gdnameinputedit.text() != '':
            gdnodejson = json.dumps(self.gdnodecontent)
            filepath = self.gdnameinputedit.text() + '.json'
            with open(filepath, 'w', encoding='utf8') as f:
                f.write(gdnodejson)
            self.statusBar().showMessage('保存引导文件：' + filepath + '成功', 3000)
        else:
            self.statusBar().showMessage('引导名为空或是引导没有内容输入，无法保存', 3000)

    def changeGDNameInputByLineText(self):
        if self.gdnameinputedit.text() != '':
            self.gdnameaddbtn.setEnabled(True)
            self.gdnamedelbtn.setEnabled(True)
        else:
            self.gdnameaddbtn.setEnabled(False)
            self.gdnamedelbtn.setEnabled(False)

    def changSaveJsonByGDNodeView(self):
        if self.gdnodeview.toPlainText() != '':
            self.gdjsonsavebtn.setEnabled(True)
        else:
            self.gdjsonsavebtn.setEnabled(False)
