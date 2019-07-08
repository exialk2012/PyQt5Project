from Setting.Setting import IconPath
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        # self.cwd = os.getcwd()
        '''
        主窗口的相关设置
        '''
        # 设置窗口大小
        self.setGeometry(0,0,800,600)
        # 设置窗口大小
        self.setFixedSize(self.width(),self.height())
        # 设置窗口标题
        self.setWindowTitle('GuideDataTool')
        # 设置窗口显示图标
        self.setWindowIcon(QIcon(IconPath))

        '''
        菜单栏的相关设置
        '''
        menubar = QMenuBar(self)
        menubar.setGeometry(0,0,800,23)
        menu_comm = menubar.addMenu('常规')
        # menu_comm.

        '''
        引导名label相关
        '''
        self.guidenamelbl = QLabel(self)
        self.guidenamelbl.move(10,33)
        self.guidenamelbl.setText('引导名：')
        self.guidenamelbl.setFont(QFont('A',12))

        '''
        引导名输入框相关
        '''
        self.guidenameel = QLineEdit(self)
        self.guidenameel.move(75,33)
        self.guidenameel.setText('请输入引导节点名称')
        self.guidenameel.selectAll()
        self.guidenameel.setFocus()

        '''
        保存文件按钮相关
        '''
        self.savebtn = QPushButton(self)
        self.savebtn.move(250,33)
        self.savebtn.setText('保存Json')
        self.savebtn.clicked.connect(self.slot_Btn_SaveFile)

        self.show()

    def slot_Btn_SaveFile(self):
        fileName_choose,fileType = QFileDialog.getSaveFileName(self,'文件保存',self.guidenameel.text(),'Json File(*.json)')

        if fileName_choose == '':
            print('\n取消选择')
            return

        print('\n你选择要保存的文件为：')
        print(fileName_choose)
        print('文件筛选器:',fileType)