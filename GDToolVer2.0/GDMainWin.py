from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json


class GDMain(QMainWindow):
    def __init__(self):
        super(GDMain, self).__init__()
        self.initMainWindow()

    def initMainWindow(self):
        self.setMainWindowProperty()
        self.initTreeView()
        self.initGDName()
        self.initTriggers()
        self.initConditional()
        self.initNodeData()
        self.initJsonView()
        self.initGDJsonSaveBtn()
        self.initObjectWidgets()
        self.show()

    def setMainWindowProperty(self):
        self.setFixedSize(800, 720)
        self.setWindowTitle('引导工具 2.0')
        self.setWindowIcon(QIcon(r'..\GDToolVer2.0\icon.ico'))

        self.statusBar().showMessage('启动成功', 3000)

    def initTreeView(self):
        # 设置引导列树控件
        self.gd_tree_lbl = QLabel('引导节点列表')
        self.gd_tree_viewer = QTreeWidget()

    def initGDName(self):
        # 设置引导节点名与节点名输入框与插入按钮
        self.gd_name_lbl = QLabel('<b>GuideName</b>')
        self.gd_name_input_edit = QLineEdit()
        self.gd_name_input_edit.setPlaceholderText('请输入引导节点名称')
        self.gd_name_add_btn = QPushButton('插入')
        self.gd_name_del_btn = QPushButton('删除')

        gd_name_widgets = [
            self.gd_name_add_btn,
            self.gd_name_del_btn
        ]

        self.isWidgetEnable(gd_name_widgets, False)

        self.gd_name_add_btn.clicked.connect(self.clickGDNameAdd)
        self.gd_name_del_btn.clicked.connect(self.clickGDNameDel)
        self.gd_name_input_edit.textChanged.connect(self.changeGDNameInputByLineText)

    def initTriggers(self):
        # 设置引导节点触发器与触发器相关
        trigger_types = [
            "-- 请选择触发器类型 --",
            "OpenPanel",
            "OpenArea",
            "NPCClick",
            "GuideCompleted",
            "ArrivalNode",
            "PassingNode",
            "LoginSuccess",
            "UIClick"
        ]
        self.triggers_lbl = QLabel('<b>Triggers</b>')
        self.triggers_data_lbl = QLabel('Data')
        self.trigger_type_lbl = QLabel('TriggerType')
        self.trigger_type_cb = QComboBox()
        self.trigger_type_cb.addItems(trigger_types)
        self.trigger_type_cb.setMaxVisibleItems(5)
        self.trigger_data_lbl1 = QLabel('content1')
        self.trigger_data_lineedit1 = QLineEdit()
        self.trigger_data_lbl2 = QLabel('content2')
        self.trigger_data_lineedit2 = QLineEdit()
        self.trigger_data_lbl3 = QLabel('content3')
        self.trigger_data_lineedit3 = QLineEdit()

        trigger_widgets_isvisiable_list = [
            self.trigger_data_lbl1,
            self.trigger_data_lineedit1,
            self.trigger_data_lbl2,
            self.trigger_data_lineedit2,
            self.trigger_data_lbl3,
            self.trigger_data_lineedit3
        ]
        self.isWidgetVisible(trigger_widgets_isvisiable_list, False)

        self.trigger_add_btn = QPushButton('添加')
        self.trigger_del_btn = QPushButton('删除')
        self.trigger_insert_btn = QPushButton('插入')
        self.trigger_remove_btn = QPushButton('移除')

        trigger_widgets_isenable_list = [
            self.trigger_add_btn,
            self.trigger_del_btn,
            self.trigger_insert_btn,
            self.trigger_remove_btn
        ]
        self.isWidgetEnable(trigger_widgets_isenable_list, False)

        self.trigger_data_lbls_list = [
            self.trigger_data_lbl1,
            self.trigger_data_lbl2,
            self.trigger_data_lbl3
        ]

        self.trigger_data_edits_list = [
            self.trigger_data_lineedit1,
            self.trigger_data_lineedit2,
            self.trigger_data_lineedit3
        ]

        self.trigger_data_btns_list = [
            self.trigger_add_btn,
            self.trigger_del_btn,
            self.trigger_insert_btn,
            self.trigger_remove_btn
        ]

        self.trigger_type_cb.currentIndexChanged.connect(self.changeTriggerDataByType)

    def initConditional(self):
        # 设置引导前置条件触发器相关
        self.pre_cb = QCheckBox('Preconditions')
        self.pre_cb.stateChanged.connect(self.pre_CB_StateChange)

        self.pre_data_lbl = QLabel('Data')
        self.pre_condition_type_lbl = QLabel('ConditionType')
        self.pre_condition_type_edit = QComboBox()
        self.pre_condition_type_edit.addItem('-- 请选择条件类型 --')
        self.pre_condition_type_edit.addItem('GuideCompleted')

        self.pre_condition_data_lbl1 = QLabel('content1')
        self.pre_condition_data_edit1 = QLineEdit()

        self.pre_condition_data_lbl2 = QLabel('content2')
        self.pre_condition_data_edit2 = QLineEdit()

        self.pre_condition_data_lbl3 = QLabel('content3')
        self.pre_condition_data_edit3 = QLineEdit()

        self.pre_add_btn = QPushButton('添加')
        self.pre_del_btn = QPushButton('删除')
        self.pre_insert_btn = QPushButton('插入')
        self.pre_remove_btn = QPushButton('移除')

        pre_cond_isvisiable_list = [
            self.pre_condition_data_lbl1,
            self.pre_condition_data_edit1,
            self.pre_condition_data_lbl2,
            self.pre_condition_data_edit2,
            self.pre_condition_data_lbl3,
            self.pre_condition_data_edit3
        ]
        pre_cond_isenable_list = [
            self.pre_data_lbl,
            self.pre_condition_type_lbl,
            self.pre_condition_type_edit,
            self.pre_add_btn,
            self.pre_del_btn,
            self.pre_insert_btn,
            self.pre_remove_btn
        ]
        self.isWidgetVisible(pre_cond_isvisiable_list, False)
        self.isWidgetEnable(pre_cond_isenable_list, False)

        self.pre_cond_data_lbls = [
            self.pre_condition_data_lbl1,
            self.pre_condition_data_lbl2,
            self.pre_condition_data_lbl3
        ]

        self.pre_cond_data_edits = [
            self.pre_condition_data_edit1,
            self.pre_condition_data_edit2,
            self.pre_condition_data_edit3
        ]

        self.pre_cond_data_btns = [
            self.pre_add_btn,
            self.pre_del_btn,
            self.pre_insert_btn,
            self.pre_remove_btn
        ]

        self.pre_condition_type_edit.currentIndexChanged.connect(self.changeConditionByType)

    def initNodeData(self):
        # 设置NodeData相关空间
        node_data_types = [
            "-- 请选择执行条件 --",
            "SetTips",
            "ClearTips",
            "SetBlink",
            "HideMask",
            "ShowMask",
            "SetMaskAlpha",
            "Highlight",
            "ClearHighlight",
            "HideUIObject",
            "ShowUIObject",
            "ClearGuidePanel",
            "ShowPictures",
            "SetInteractableNames",
            "SetInteractable",
            "WaitPanelOpen",
            "WaitPanelClose",
            "SetCanWalk",
            "SetMapActive",
            "ShowNodeElement",
            "HideNodeElement",
            "EnableNodeEvent",
            "DisableNodeEvent",
            "LoadNpc",
            "DestroyNPC",
            "PlayAVG",
            "EnterAdventure",
            "Await",
            "OpenUIPanel",
            "CloseUIPanel",
            "Teleport",
            "Complete",
            "WaitAreaOpen",
            "WaitAreaClose",
            "WaitMoveTo",
            "UnlockModule",
            "ShowSingleEffect",
            "EnterGame",
            "LoadElement",
            "DefaultTeleport",
            "UnlockNewTeleport",
            "AddMapEvent",
            "ClearMapEvent",
            "PlayVideo",
            "PlayBgm",
            "PauseBgm",
            "ChangeHero",
            "LockSkin",
            "UnlockSkin",
            "LockCardPackage",
            "UnlockCardPackage",
            "HeroEvolutionHideHero",
            "HideHeroThumbnail",
            "WaitEventCompleted",
            "SetElementAngle"
        ]
        self.nodedata_lbl = QLabel('<b>NodeData</b>')

        self.is_click_to_next_lbl = QLabel('IsClickToNext')
        self.is_click_to_next_cb = QComboBox()
        self.is_click_to_next_cb.addItem('false')
        self.is_click_to_next_cb.addItem('true')

        self.is_auto_to_next_lbl = QLabel('IsAutoToNext')
        self.is_auto_to_next_cb = QComboBox()
        self.is_auto_to_next_cb.addItem('false')
        self.is_auto_to_next_cb.addItem('true')

        self.dodata_lbl = QLabel('DoData')

        self.data_lbl = QLabel('Data')

        self.dotype_lbl = QLabel('DoType')
        self.dotype_cb = QComboBox()
        self.dotype_cb.addItems(node_data_types)
        self.dotype_cb.setMaxVisibleItems(10)
        # self.dotype_cb.setPlaceholderText('请选择引导执行效果')

        self.dotype_data_lbl1 = QLabel('content1')
        self.dotype_data_edit1 = QLineEdit()
        self.dotype_data_lbl2 = QLabel('content2')
        self.dotype_data_edit2 = QLineEdit()
        self.dotype_data_lbl3 = QLabel('content3')
        self.dotype_data_edit3 = QLineEdit()
        self.dotype_data_lbl4 = QLabel('content4')
        self.dotype_data_edit4 = QLineEdit()
        self.dotype_data_lbl5 = QLabel('content5')
        self.dotype_data_edit5 = QLineEdit()
        self.dotype_data_summary_lbl = QLabel('Summary')
        self.dotype_data_summary_edit = QLineEdit()

        self.nodedata_add_btn = QPushButton('添加')
        self.nodedata_del_btn = QPushButton('删除')
        self.nodedata_insert_btn = QPushButton('插入')
        self.nodedata_remove_btn = QPushButton('移除')

        node_data_isvisiable_list = [
            self.dotype_data_lbl1,
            self.dotype_data_edit1,
            self.dotype_data_lbl2,
            self.dotype_data_edit2,
            self.dotype_data_lbl3,
            self.dotype_data_edit3,
            self.dotype_data_lbl4,
            self.dotype_data_edit4,
            self.dotype_data_lbl5,
            self.dotype_data_edit5,
            self.dotype_data_summary_lbl,
            self.dotype_data_summary_edit
        ]
        node_data_isenable_list = [
            self.nodedata_add_btn,
            self.nodedata_del_btn,
            self.nodedata_insert_btn,
            self.nodedata_remove_btn
        ]
        self.isWidgetVisible(node_data_isvisiable_list, False)
        self.isWidgetEnable(node_data_isenable_list, False)

        self.node_data_lbls_list = [
            self.dotype_data_lbl1,
            self.dotype_data_lbl2,
            self.dotype_data_lbl3,
            self.dotype_data_lbl4,
            self.dotype_data_lbl5,
            self.dotype_data_summary_lbl
        ]

        self.node_data_edits_list = [
            self.dotype_data_edit1,
            self.dotype_data_edit2,
            self.dotype_data_edit3,
            self.dotype_data_edit4,
            self.dotype_data_edit5,
            self.dotype_data_summary_edit
        ]

        self.node_data_btns_list = [
            self.nodedata_add_btn,
            self.nodedata_del_btn,
            self.nodedata_insert_btn,
            self.nodedata_remove_btn
        ]

        self.dotype_cb.currentIndexChanged.connect(self.changeNodeDataByType)

    def initJsonView(self):
        # 设置引导文本显示相关
        self.gd_node_content = {}
        self.gd_node_view_lbl = QLabel('引导文本预览:')
        self.gd_node_view = QTextEdit()
        self.gd_node_view.setReadOnly(True)
        self.gd_node_view.textChanged.connect(self.changSaveJsonByGDNodeView)

    def initGDJsonSaveBtn(self):
        # 设置保存引导json按钮相关
        self.gd_json_save_btn = QPushButton('保存脚本')
        self.gd_json_save_btn.setEnabled(False)
        self.gd_json_save_btn.clicked.connect(self.clickGDJsonSave)

    def initObjectWidgets(self):
        obj_widget = QWidget()
        obj_widget.setLayout(self.setWindowLayout())
        self.setCentralWidget(obj_widget)

    def clickGDNameDel(self):
        self.gd_name_input_edit.clear()
        self.statusBar().showMessage('已删除引导节点名', 3000)

    def clickGDNameAdd(self):
        self.gd_node_content.update(GuideName=self.gd_name_input_edit.text())
        self.gd_node_view.setText(str(self.gd_node_content))
        self.statusBar().showMessage('添加引导名称成功', 3000)

    def clickGDJsonSave(self):
        if self.gd_node_view.toPlainText() != '' and self.gd_name_input_edit.text() != '':
            gdnodejson = json.dumps(self.gd_node_content)
            filepath = self.gd_name_input_edit.text() + '.json'
            with open(filepath, 'w', encoding='utf8') as f:
                f.write(gdnodejson)
            self.statusBar().showMessage('保存引导文件：' + filepath + '成功', 3000)
        else:
            self.statusBar().showMessage('引导名为空或是引导没有内容输入，无法保存', 3000)

    def changeGDNameInputByLineText(self):
        if self.gd_name_input_edit.text() != '':
            self.gd_name_add_btn.setEnabled(True)
            self.gd_name_del_btn.setEnabled(True)
        else:
            self.gd_name_add_btn.setEnabled(False)
            self.gd_name_del_btn.setEnabled(False)

    def changSaveJsonByGDNodeView(self):
        if self.gd_node_view.toPlainText() != '':
            self.gd_json_save_btn.setEnabled(True)
        else:
            self.gd_json_save_btn.setEnabled(False)

    def pre_CB_StateChange(self):
        if self.pre_cb.isChecked() == False:
            self.pre_data_lbl.setEnabled(False)
            self.pre_condition_type_lbl.setEnabled(False)
            self.pre_condition_type_edit.setEnabled(False)
            self.pre_condition_data_lbl1.setEnabled(False)
            self.pre_condition_data_edit1.setEnabled(False)
            self.pre_condition_data_lbl2.setEnabled(False)
            self.pre_condition_data_edit2.setEnabled(False)
            self.pre_condition_data_lbl3.setEnabled(False)
            self.pre_condition_data_edit3.setEnabled(False)
            self.statusBar().showMessage('前置条件已禁用')
        else:
            self.pre_data_lbl.setEnabled(True)
            self.pre_condition_type_lbl.setEnabled(True)
            self.pre_condition_type_edit.setEnabled(True)
            self.pre_condition_data_lbl1.setEnabled(True)
            self.pre_condition_data_edit1.setEnabled(True)
            self.pre_condition_data_lbl2.setEnabled(True)
            self.pre_condition_data_edit2.setEnabled(True)
            self.pre_condition_data_lbl3.setEnabled(True)
            self.pre_condition_data_edit3.setEnabled(True)
            self.statusBar().showMessage('前置条件已启用')

    def setWindowLayout(self):
        # 设置布局
        main_hbox = QHBoxLayout()

        # treeview相关布局
        gd_tree_vbox = QVBoxLayout()

        # hbox.addStretch(1)
        gd_tree_vbox.addWidget(self.gd_tree_lbl)
        gd_tree_vbox.addWidget(self.gd_tree_viewer)
        # main_hbox.addLayout(gd_tree_vbox)

        # 引导节点名相关布局
        gd_input_vbox = QVBoxLayout()
        gd_name_hbox = QHBoxLayout()
        gd_name_hbox.addWidget(self.gd_name_lbl)
        gd_name_hbox.addWidget(self.gd_name_input_edit)
        gd_name_hbox.addWidget(self.gd_name_add_btn)
        gd_name_hbox.addWidget(self.gd_name_del_btn)
        gd_input_vbox.addLayout(gd_name_hbox)
        gd_input_vbox.addStretch(3)

        # 引导触发器相关布局
        gd_input_vbox.addWidget(self.triggers_lbl)
        gd_input_vbox.addWidget(self.triggers_data_lbl)
        trigger_type_hbox = QHBoxLayout()
        trigger_type_hbox.addWidget(self.trigger_type_lbl)
        trigger_type_hbox.addWidget(self.trigger_type_cb)
        gd_input_vbox.addLayout(trigger_type_hbox)

        trigger_data1_hbox = QHBoxLayout()
        trigger_data1_hbox.addWidget(self.trigger_data_lbl1)
        trigger_data1_hbox.addWidget(self.trigger_data_lineedit1)
        gd_input_vbox.addLayout(trigger_data1_hbox)

        trigger_data2_hbox = QHBoxLayout()
        trigger_data2_hbox.addWidget(self.trigger_data_lbl2)
        trigger_data2_hbox.addWidget(self.trigger_data_lineedit2)
        gd_input_vbox.addLayout(trigger_data2_hbox)

        trigger_data3_hbox = QHBoxLayout()
        trigger_data3_hbox.addWidget(self.trigger_data_lbl3)
        trigger_data3_hbox.addWidget(self.trigger_data_lineedit3)
        gd_input_vbox.addLayout(trigger_data3_hbox)

        trigger_btn_hbox = QHBoxLayout()
        trigger_btn_hbox.addWidget(self.trigger_add_btn)
        trigger_btn_hbox.addWidget(self.trigger_del_btn)
        trigger_btn_hbox.addWidget(self.trigger_insert_btn)
        trigger_btn_hbox.addWidget(self.trigger_remove_btn)
        gd_input_vbox.addLayout(trigger_btn_hbox)

        gd_input_vbox.addStretch(3)

        # 引导前置条件相关布局
        gd_input_vbox.addWidget(self.pre_cb)
        gd_input_vbox.addWidget(self.pre_data_lbl)

        pre_cond_type_hbox = QHBoxLayout()
        pre_cond_type_hbox.addWidget(self.pre_condition_type_lbl)
        pre_cond_type_hbox.addWidget(self.pre_condition_type_edit)
        gd_input_vbox.addLayout(pre_cond_type_hbox)

        pre_cond_data_hbox1 = QHBoxLayout()
        pre_cond_data_hbox2 = QHBoxLayout()
        pre_cond_data_hbox3 = QHBoxLayout()
        pre_cond_data_hbox1.addWidget(self.pre_condition_data_lbl1)
        pre_cond_data_hbox1.addWidget(self.pre_condition_data_edit1)
        pre_cond_data_hbox2.addWidget(self.pre_condition_data_lbl2)
        pre_cond_data_hbox2.addWidget(self.pre_condition_data_edit2)
        pre_cond_data_hbox3.addWidget(self.pre_condition_data_lbl3)
        pre_cond_data_hbox3.addWidget(self.pre_condition_data_edit3)
        gd_input_vbox.addLayout(pre_cond_data_hbox1)
        gd_input_vbox.addLayout(pre_cond_data_hbox2)
        gd_input_vbox.addLayout(pre_cond_data_hbox3)

        pre_cond_btn_hbox = QHBoxLayout()
        pre_cond_btn_hbox.addWidget(self.pre_add_btn)
        pre_cond_btn_hbox.addWidget(self.pre_del_btn)
        pre_cond_btn_hbox.addWidget(self.pre_insert_btn)
        pre_cond_btn_hbox.addWidget(self.pre_remove_btn)
        gd_input_vbox.addLayout(pre_cond_btn_hbox)
        gd_input_vbox.addStretch(3)

        # 引导NodeData布局相关
        gd_input_vbox.addWidget(self.nodedata_lbl)

        is_click_tonext_hbox = QHBoxLayout()
        is_click_tonext_hbox.addWidget(self.is_click_to_next_lbl)
        is_click_tonext_hbox.addWidget(self.is_click_to_next_cb)
        gd_input_vbox.addLayout(is_click_tonext_hbox)

        is_auto_tonext_hbox = QHBoxLayout()
        is_auto_tonext_hbox.addWidget(self.is_auto_to_next_lbl)
        is_auto_tonext_hbox.addWidget(self.is_auto_to_next_cb)
        gd_input_vbox.addLayout(is_auto_tonext_hbox)

        gd_input_vbox.addWidget(self.dodata_lbl)
        gd_input_vbox.addWidget(self.data_lbl)

        dotype_hbox = QHBoxLayout()
        dotype_hbox.addWidget(self.dotype_lbl)
        dotype_hbox.addWidget(self.dotype_cb)
        gd_input_vbox.addLayout(dotype_hbox)

        dotype_data_hbox1 = QHBoxLayout()
        dotype_data_hbox1.addWidget(self.dotype_data_lbl1)
        dotype_data_hbox1.addWidget(self.dotype_data_edit1)
        gd_input_vbox.addLayout(dotype_data_hbox1)

        dotype_data_hbox2 = QHBoxLayout()
        dotype_data_hbox2.addWidget(self.dotype_data_lbl2)
        dotype_data_hbox2.addWidget(self.dotype_data_edit2)
        gd_input_vbox.addLayout(dotype_data_hbox2)

        dotype_data_hbox3 = QHBoxLayout()
        dotype_data_hbox3.addWidget(self.dotype_data_lbl3)
        dotype_data_hbox3.addWidget(self.dotype_data_edit3)
        gd_input_vbox.addLayout(dotype_data_hbox3)

        dotype_data_hbox4 = QHBoxLayout()
        dotype_data_hbox4.addWidget(self.dotype_data_lbl4)
        dotype_data_hbox4.addWidget(self.dotype_data_edit4)
        gd_input_vbox.addLayout(dotype_data_hbox4)

        dotype_data_hbox5 = QHBoxLayout()
        dotype_data_hbox5.addWidget(self.dotype_data_lbl5)
        dotype_data_hbox5.addWidget(self.dotype_data_edit5)
        gd_input_vbox.addLayout(dotype_data_hbox5)

        dotype_data_summary_hbox = QHBoxLayout()
        dotype_data_summary_hbox.addWidget(self.dotype_data_summary_lbl)
        dotype_data_summary_hbox.addWidget(self.dotype_data_summary_edit)
        gd_input_vbox.addLayout(dotype_data_summary_hbox)

        dotype_btn_hbox = QHBoxLayout()
        dotype_btn_hbox.addWidget(self.nodedata_add_btn)
        dotype_btn_hbox.addWidget(self.nodedata_del_btn)
        dotype_btn_hbox.addWidget(self.nodedata_insert_btn)
        dotype_btn_hbox.addWidget(self.nodedata_remove_btn)

        gd_input_vbox.addLayout(dotype_btn_hbox)

        gd_input_vbox.addStretch(3)
        main_hbox.addLayout(gd_input_vbox)

        # 设置引导文本预览相关布局
        gd_node_view_vbox = QVBoxLayout()
        gd_node_view_vbox.addWidget(self.gd_node_view_lbl)
        gd_node_view_vbox.addWidget(self.gd_node_view)
        main_hbox.addLayout(gd_node_view_vbox)

        # 设置保存脚本按钮相关布局
        save_gd_json_hbox = QHBoxLayout()
        save_gd_json_hbox.addStretch(10)
        save_gd_json_hbox.addWidget(self.gd_json_save_btn)
        gd_node_view_vbox.addLayout(save_gd_json_hbox)

        return main_hbox

    def isWidgetEnable(self, widgets: list, isEnable: bool):
        if widgets == []:
            pass
        else:
            for widget in widgets:
                widget.setEnabled(isEnable)

    def isWidgetVisible(self, widgets: list, isVisible: bool):
        if widgets == []:
            pass
        else:
            for widget in widgets:
                widget.setVisible(isVisible)

    def changeTriggerDataByType(self):
        if self.trigger_type_cb.currentText() == "-- 请选择触发器类型 --":
            # print(self.trigger_type_cb.currentText())
            for lbl in self.trigger_data_lbls_list:
                lbl.setVisible(False)
            for edit in self.trigger_data_edits_list:
                edit.setVisible(False)
            for btn in self.trigger_data_btns_list:
                btn.setEnabled(False)

        elif self.trigger_type_cb.currentText() == "OpenPanel":
            self.trigger_data_lbls_list[0].setText('PanelName')
            self.trigger_data_lbls_list[0].setVisible(True)
            self.trigger_data_lbls_list[1].setVisible(False)
            self.trigger_data_lbls_list[2].setVisible(False)
            self.trigger_data_edits_list[0].setVisible(True)
            self.trigger_data_edits_list[1].setVisible(False)
            self.trigger_data_edits_list[2].setVisible(False)

        elif self.trigger_type_cb.currentText() == "OpenArea":
            self.trigger_data_lbls_list[0].setText('MapId')
            self.trigger_data_lbls_list[0].setVisible(True)
            self.trigger_data_lbls_list[1].setText('AreaId')
            self.trigger_data_lbls_list[1].setVisible(True)
            self.trigger_data_lbls_list[2].setVisible(False)
            self.trigger_data_edits_list[0].setVisible(True)
            self.trigger_data_edits_list[1].setVisible(True)
            self.trigger_data_edits_list[2].setVisible(False)

        elif self.trigger_type_cb.currentText() == "NPCClick":
            self.trigger_data_lbls_list[0].setText('NPCId')
            self.trigger_data_lbls_list[0].setVisible(True)
            self.trigger_data_lbls_list[1].setVisible(False)
            self.trigger_data_lbls_list[2].setVisible(False)
            self.trigger_data_edits_list[0].setVisible(True)
            self.trigger_data_edits_list[1].setVisible(False)
            self.trigger_data_edits_list[2].setVisible(False)

        elif self.trigger_type_cb.currentText() == "GuideCompleted":
            self.trigger_data_lbls_list[0].setText('GuideName')
            self.trigger_data_lbls_list[0].setVisible(True)
            self.trigger_data_lbls_list[1].setVisible(False)
            self.trigger_data_lbls_list[2].setVisible(False)
            self.trigger_data_edits_list[0].setVisible(True)
            self.trigger_data_edits_list[1].setVisible(False)
            self.trigger_data_edits_list[2].setVisible(False)

        elif self.trigger_type_cb.currentText() == "ArrivalNode":
            self.trigger_data_lbls_list[0].setText('Nodes')
            self.trigger_data_lbls_list[0].setVisible(True)
            self.trigger_data_lbls_list[1].setVisible(False)
            self.trigger_data_lbls_list[2].setVisible(False)
            self.trigger_data_edits_list[0].setVisible(True)
            self.trigger_data_edits_list[1].setVisible(False)
            self.trigger_data_edits_list[2].setVisible(False)

        elif self.trigger_type_cb.currentText() == "PassingNode":
            self.trigger_data_lbls_list[0].setText('Nodes')
            self.trigger_data_lbls_list[0].setVisible(True)
            self.trigger_data_lbls_list[1].setVisible(False)
            self.trigger_data_lbls_list[2].setVisible(False)
            self.trigger_data_edits_list[0].setVisible(True)
            self.trigger_data_edits_list[1].setVisible(False)
            self.trigger_data_edits_list[2].setVisible(False)

        elif self.trigger_type_cb.currentText() == "LoginSuccess":
            for lbl in self.trigger_data_lbls_list:
                lbl.setVisible(False)
            for edit in self.trigger_data_edits_list:
                edit.setVisible(False)

        elif self.trigger_type_cb.currentText() == "UIClick":
            self.trigger_data_lbls_list[0].setText('UIName')
            self.trigger_data_lbls_list[0].setVisible(True)
            self.trigger_data_lbls_list[1].setVisible(False)
            self.trigger_data_lbls_list[2].setVisible(False)
            self.trigger_data_edits_list[0].setVisible(True)
            self.trigger_data_edits_list[1].setVisible(False)
            self.trigger_data_edits_list[2].setVisible(False)

        else:
            pass

    def changeConditionByType(self):
        if self.pre_condition_type_edit.currentText() == '-- 请选择条件类型 --':
            for lbl in self.pre_cond_data_lbls:
                lbl.setVisible(False)
            for edit in self.pre_cond_data_editss:
                edit.setVisible(False)

            for btn in self.pre_cond_data_btns:
                btn.setEnabled(False)

        elif self.pre_condition_type_edit.currentText() == 'GuideCompleted':
            self.pre_cond_data_lbls[0].setText('GuideName')
            self.pre_cond_data_lbls[0].setVisible(True)
            self.pre_cond_data_lbls[1].setVisible(False)
            self.pre_cond_data_lbls[1].setVisible(False)
            self.pre_cond_data_edits[0].setVisible(True)
            self.pre_cond_data_edits[1].setVisible(False)
            self.pre_cond_data_edits[2].setVisible(False)

        else:
            pass

    def changeNodeDataByType(self):
        if self.dotype_cb.currentText() == '-- 请选择执行条件 --':
            for lbl in self.node_data_lbls_list:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list:
                edit.setVisible(False)

            for btn in self.node_data_btns_list:
                btn.setEnabled(False)


        elif self.dotype_cb.currentText() == 'SetTips':
            for lbl in self.node_data_lbls_list:
                lbl.setVisible(True)
            for edit in self.node_data_edits_list:
                edit.setVisible(True)
            self.node_data_lbls_list[0].setText('Text')
            self.node_data_lbls_list[1].setText('Position')
            self.node_data_lbls_list[2].setText('ShowFrame')
            self.node_data_lbls_list[3].setText('AutoDisappear')
            self.node_data_lbls_list[4].setText('Duration')


        elif self.dotype_cb.currentText() == 'ClearTips':
            for lbl in self.node_data_lbls_list[0:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[0:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'SetBlink':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('Position')
            self.node_data_lbls_list[1].setText('Rotation')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'HideMask':
            for lbl in self.node_data_lbls_list[0:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[0:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'ShowMask':
            for lbl in self.node_data_lbls_list[0:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[0:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'SetMaskAlpha':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('Alpha')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'Highlight':
            for lbl in self.node_data_lbls_list[3:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[3:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('Panel')
            self.node_data_lbls_list[1].setText('Objects')
            self.node_data_lbls_list[2].setText('Order')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[2].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[2].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'ClearHighlight':
            for lbl in self.node_data_lbls_list:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list:
                edit.setVisible(False)

        elif self.dotype_cb.currentText() == 'HideUIObject':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('Panel')
            self.node_data_lbls_list[1].setText('Objects')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'ShowUIObject':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('Panel')
            self.node_data_lbls_list[1].setText('Objects')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'ClearGuidePanel':
            for lbl in self.node_data_lbls_list:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list:
                edit.setVisible(False)

        elif self.dotype_cb.currentText() == 'ShowPictures':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('Paths')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'SetInteractableNames':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('Names')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'SetInteractable':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('Panel')
            self.node_data_lbls_list[1].setText('Objects')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'WaitPanelOpen':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('PanelName')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'WaitPanelClose':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('PanelName')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'SetCanWalk':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('NodeIds')
            self.node_data_lbls_list[1].setText('CanWalk')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'SetMapActive':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('Active')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'ShowNodeElement':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('NodeIds')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'HideNodeElement':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('NodeIds')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'EnableNodeEvent':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('NodeIds')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'DisableNodeEvent':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('NodeIds')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'LoadNpc':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('NPCInfo')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'DestroyNPC':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('NPCId')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'PlayAVG':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('Name')
            self.node_data_lbls_list[1].setText('StopBgm')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'EnterAdventure':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('AreaId')
            self.node_data_lbls_list[1].setText('SectionId')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'Await':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('WaitTime')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'OpenUIPanel':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('PanelName')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'CloseUIPanel':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('PanelName')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'Teleport':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('MapId')
            self.node_data_lbls_list[1].setText('NodeId')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'Complete':
            for lbl in self.node_data_lbls_list[0:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[0:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'WaitAreaOpen':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('MapId')
            self.node_data_lbls_list[1].setText('AreaId')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'WaitAreaClose':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('MapId')
            self.node_data_lbls_list[1].setText('AreaId')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'WaitMoveTo':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('PassingNodes')
            self.node_data_lbls_list[1].setText('ArrivalNodes')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'UnlockModule':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('Module')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'ShowSingleEffect':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('EffectName')
            self.node_data_lbls_list[1].setText('OverridElements')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'EnterGame':
            for lbl in self.node_data_lbls_list[0:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[0:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'LoadElement':
            for lbl in self.node_data_lbls_list:
                lbl.setVisible(True)
            for edit in self.node_data_edits_list:
                edit.setVisible(True)
            self.node_data_lbls_list[0].setText('NodeId')
            self.node_data_lbls_list[1].setText('ElementKey')
            self.node_data_lbls_list[2].setText('Position')
            self.node_data_lbls_list[3].setText('EulerAngles')
            self.node_data_lbls_list[4].setText('Scale')

        elif self.dotype_cb.currentText() == 'DefaultTeleport':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('TeleportTag')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'UnlockNewTeleport':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('TeleportTag')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'AddMapEvent':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('NodeId')
            self.node_data_lbls_list[1].setText('Data')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'ClearMapEvent':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('NodeId')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'PlayVideo':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('ClipPath')
            self.node_data_lbls_list[1].setText('CanSkip')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'PlayBgm':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('BgmName')
            self.node_data_lbls_list[1].setText('Replay')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'PauseBgm':
            for lbl in self.node_data_lbls_list[0:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[0:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'ChangeHero':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('SkinId')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'LockSkin':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('HeroSkinIds')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'UnlockSkin':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('HeroSkinIds')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'LockCardPackage':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('CardPackages')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'UnlockCardPackage':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('CardPackages')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'HeroEvolutionHideHero':
            for lbl in self.node_data_lbls_list[2:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[2:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('HeroSkinIds')
            self.node_data_lbls_list[1].setText('HeroIds')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'HideHeroThumbnail':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('HeroSkinIds')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'WaitEventCompleted':
            for lbl in self.node_data_lbls_list[1:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[1:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('NodeIds')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        elif self.dotype_cb.currentText() == 'SetElementAngle':
            for lbl in self.node_data_lbls_list[3:-1]:
                lbl.setVisible(False)
            for edit in self.node_data_edits_list[3:-1]:
                edit.setVisible(False)
            self.node_data_lbls_list[0].setText('NodeId')
            self.node_data_lbls_list[1].setText('Angle')
            self.node_data_lbls_list[2].setText('Duration')
            self.node_data_lbls_list[0].setVisible(True)
            self.node_data_lbls_list[1].setVisible(True)
            self.node_data_lbls_list[2].setVisible(True)
            self.node_data_lbls_list[-1].setVisible(True)
            self.node_data_edits_list[0].setVisible(True)
            self.node_data_edits_list[1].setVisible(True)
            self.node_data_edits_list[2].setVisible(True)
            self.node_data_edits_list[-1].setVisible(True)

        else:
            pass



