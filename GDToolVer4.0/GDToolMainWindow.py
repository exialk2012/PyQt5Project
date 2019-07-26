from GDToolLayout import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem, QTreeWidgetItemIterator
import json
import Info.TypeList


class GDToolMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setTypeToCombox()
        self.initGDTri()
        self.initBtnClick()
        self.show()

        self.gd_content = {}

    def setTypeToCombox(self):
        self.ui.cbox_gd_tri_type.addItems(Info.TypeList.LIST_GD_TRI_TYPE)
        self.ui.cbox_gd_pre_type.addItems(Info.TypeList.LIST_GD_PRE_TYPE)
        self.ui.cbox_gd_do_type.addItems(Info.TypeList.LIST_GD_DO_TYPE)
        self.ui.cbox_gd_click_to_nex.addItems(Info.TypeList.LIST_GD_TO_NEXT)
        self.ui.cbox_gd_auto_to_nex.addItems(Info.TypeList.LIST_GD_TO_NEXT)

    def initGDTri(self):
        self.ui.lbl_gd_tri_cont1.setVisible(False)
        self.ui.lbl_gd_tri_cont2.setVisible(False)
        self.ui.lbl_gd_tri_cont3.setVisible(False)
        self.ui.le_gd_tri_cont1.setVisible(False)
        self.ui.le_gd_tri_cont2.setVisible(False)
        self.ui.le_gd_tri_cont3.setVisible(False)

        self.ui.lbl_gd_pre_cont1.setVisible(False)
        self.ui.lbl_gd_pre_cont2.setVisible(False)
        self.ui.lbl_gd_pre_cont3.setVisible(False)
        self.ui.le_gd_pre_cont1.setVisible(False)
        self.ui.le_gd_pre_cont2.setVisible(False)
        self.ui.le_gd_pre_cont3.setVisible(False)

        self.ui.lbl_gd_do_cont1.setVisible(False)
        self.ui.lbl_gd_do_cont2.setVisible(False)
        self.ui.lbl_gd_do_cont3.setVisible(False)
        self.ui.lbl_gd_do_cont4.setVisible(False)
        self.ui.lbl_gd_do_cont5.setVisible(False)
        self.ui.le_gd_do_cont1.setVisible(False)
        self.ui.le_gd_do_cont2.setVisible(False)
        self.ui.le_gd_do_cont3.setVisible(False)
        self.ui.le_gd_do_cont4.setVisible(False)
        self.ui.le_gd_do_cont5.setVisible(False)

        self.ui.cbox_gd_tri_type.currentIndexChanged.connect(self.changeContentByType)
        self.ui.cbox_gd_pre_type.currentIndexChanged.connect(self.changeContentByType)
        self.ui.cbox_gd_do_type.currentIndexChanged.connect(self.changeContentByType)

    def initBtnClick(self):
        self.ui.btn_gd_tri_insert.clicked.connect(self.btnClickEvent)
        self.ui.btn_gd_pre_insert.clicked.connect(self.btnClickEvent)
        self.ui.btn_gd_do_insert_big.clicked.connect(self.btnClickEvent)
        self.ui.btn_create.clicked.connect(self.btnClickEvent)

    def changeContentByType(self):
        sender = self.sender()
        if sender == self.ui.cbox_gd_tri_type:
            if self.ui.cbox_gd_tri_type.currentText() in ['OpenPanel', 'NPCClick', 'GuideCompleted', 'ArrivalNode',
                                                          'PassingNode', 'UIClick']:
                self.ui.lbl_gd_tri_cont1.setVisible(True)
                self.ui.le_gd_tri_cont1.setVisible(True)
                self.ui.lbl_gd_tri_cont2.setVisible(False)
                self.ui.le_gd_tri_cont2.setVisible(False)
                self.ui.lbl_gd_tri_cont3.setVisible(False)
                self.ui.le_gd_tri_cont3.setVisible(False)
                if self.ui.cbox_gd_tri_type.currentText() == 'OpenPanel':
                    self.ui.lbl_gd_tri_cont1.setText('PanelName')
                elif self.ui.cbox_gd_tri_type.currentText() == 'NPCClick':
                    self.ui.lbl_gd_tri_cont1.setText('NPCId')
                elif self.ui.cbox_gd_tri_type.currentText() == 'GuideCompleted':
                    self.ui.lbl_gd_tri_cont1.setText('GuideName')
                elif self.ui.cbox_gd_tri_type.currentText() == 'ArrivalNode' or self.ui.cbox_gd_tri_type.currentText() == 'PassingNode':
                    self.ui.lbl_gd_tri_cont1.setText('Nodes')
                elif self.ui.cbox_gd_tri_type.currentText() == 'UIClick':
                    self.ui.lbl_gd_tri_cont1.setText('UIName')

            elif self.ui.cbox_gd_tri_type.currentText() == 'OpenArea':
                self.ui.lbl_gd_tri_cont1.setVisible(True)
                self.ui.lbl_gd_tri_cont1.setText('MapId')
                self.ui.le_gd_tri_cont1.setVisible(True)
                self.ui.lbl_gd_tri_cont2.setVisible(True)
                self.ui.lbl_gd_tri_cont2.setText('AreaId')
                self.ui.le_gd_tri_cont2.setVisible(True)
                self.ui.lbl_gd_tri_cont3.setVisible(False)
                self.ui.le_gd_tri_cont3.setVisible(False)

            elif self.ui.cbox_gd_tri_type.currentText() in ['LoginSuccess', '请选择类型']:
                self.ui.lbl_gd_tri_cont1.setVisible(False)
                self.ui.le_gd_tri_cont1.setVisible(False)
                self.ui.lbl_gd_tri_cont2.setVisible(False)
                self.ui.le_gd_tri_cont2.setVisible(False)
                self.ui.lbl_gd_tri_cont3.setVisible(False)
                self.ui.le_gd_tri_cont3.setVisible(False)

        elif sender == self.ui.cbox_gd_pre_type:
            if self.ui.cbox_gd_pre_type.currentText() == 'GuideCompleted':
                self.ui.lbl_gd_pre_cont1.setVisible(True)
                self.ui.lbl_gd_pre_cont1.setText('GuideName')
                self.ui.le_gd_pre_cont1.setVisible(True)
                self.ui.lbl_gd_pre_cont2.setVisible(False)
                self.ui.le_gd_pre_cont2.setVisible(False)
                self.ui.lbl_gd_pre_cont3.setVisible(False)
                self.ui.le_gd_pre_cont3.setVisible(False)
            else:
                self.ui.lbl_gd_pre_cont1.setVisible(False)
                self.ui.le_gd_pre_cont1.setVisible(False)
                self.ui.lbl_gd_pre_cont2.setVisible(False)
                self.ui.le_gd_pre_cont2.setVisible(False)
                self.ui.lbl_gd_pre_cont3.setVisible(False)
                self.ui.le_gd_pre_cont3.setVisible(False)

        elif sender == self.ui.cbox_gd_do_type:
            if self.ui.cbox_gd_do_type.currentText() in ['请选择类型', 'ClearTips', 'HideMask', 'ShowMask', 'ClearHighlight',
                                                         'ClearGuidePanel', 'Complete', 'EnterGame', 'PauseBgm']:
                self.ui.lbl_gd_do_cont1.setVisible(False)
                self.ui.lbl_gd_do_cont2.setVisible(False)
                self.ui.lbl_gd_do_cont3.setVisible(False)
                self.ui.lbl_gd_do_cont4.setVisible(False)
                self.ui.lbl_gd_do_cont5.setVisible(False)
                self.ui.le_gd_do_cont1.setVisible(False)
                self.ui.le_gd_do_cont2.setVisible(False)
                self.ui.le_gd_do_cont3.setVisible(False)
                self.ui.le_gd_do_cont4.setVisible(False)
                self.ui.le_gd_do_cont5.setVisible(False)

            elif self.ui.cbox_gd_do_type.currentText() in ['SetMaskAlpha', 'ShowPictures', 'SetInteractableNames',
                                                           'WaitPanelOpen', 'WaitPanelClose', 'SetMapActive',
                                                           'ShowNodeElement', 'HideNodeElement', 'EnableNodeEvent',
                                                           'DisableNodeEvent', 'LoadNpc', 'DestroyNPC', 'Await',
                                                           'OpenUIPanel', 'CloseUIPanel', 'UnlockModule',
                                                           'DefaultTeleport', 'UnlockNewTeleport', 'ClearMapEvent',
                                                           'ChangeHero', 'LockSkin', 'UnlockSkin', 'LockCardPackage',
                                                           'UnlockCardPackage', 'WaitEventCompleted',
                                                           'HideHeroThumbnail']:
                self.ui.lbl_gd_do_cont1.setVisible(True)
                self.ui.lbl_gd_do_cont2.setVisible(False)
                self.ui.lbl_gd_do_cont3.setVisible(False)
                self.ui.lbl_gd_do_cont4.setVisible(False)
                self.ui.lbl_gd_do_cont5.setVisible(False)
                self.ui.le_gd_do_cont1.setVisible(True)
                self.ui.le_gd_do_cont2.setVisible(False)
                self.ui.le_gd_do_cont3.setVisible(False)
                self.ui.le_gd_do_cont4.setVisible(False)
                self.ui.le_gd_do_cont5.setVisible(False)
                if self.ui.cbox_gd_do_type.currentText() == 'SetMaskAlpha':
                    self.ui.lbl_gd_do_cont1.setText('Alpha')
                elif self.ui.cbox_gd_do_type.currentText() == 'ShowPictures':
                    self.ui.lbl_gd_do_cont1.setText('Paths')
                elif self.ui.cbox_gd_do_type.currentText() == 'SetInteractableNames':
                    self.ui.lbl_gd_do_cont1.setText('Names')
                elif self.ui.cbox_gd_do_type.currentText() == 'WaitPanelOpen' or self.ui.cbox_gd_do_type.currentText() == 'WaitPanelClose':
                    self.ui.lbl_gd_do_cont1.setText('PanelName')
                elif self.ui.cbox_gd_do_type.currentText() == 'SetMapActive':
                    self.ui.lbl_gd_do_cont1.setText('Active')
                elif self.ui.cbox_gd_do_type.currentText() == 'ShowNodeElement' or self.ui.cbox_gd_do_type.currentText() == 'HideNodeElement':
                    self.ui.lbl_gd_do_cont1.setText('NodeIds')
                elif self.ui.cbox_gd_do_type.currentText() == 'EnableNodeEvent' or self.ui.cbox_gd_do_type.currentText() == 'DisableNodeEvent':
                    self.ui.lbl_gd_do_cont1.setText('NodeIds')
                elif self.ui.cbox_gd_do_type.currentText() == 'LoadNpc':
                    self.ui.lbl_gd_do_cont1.setText('NPCInfo')
                elif self.ui.cbox_gd_do_type.currentText() == 'DestroyNPC':
                    self.ui.lbl_gd_do_cont1.setText('NPCId')
                elif self.ui.cbox_gd_do_type.currentText() == 'Await':
                    self.ui.lbl_gd_do_cont1.setText('WaitTime')
                elif self.ui.cbox_gd_do_type.currentText() == 'OpenUIPanel' or self.ui.cbox_gd_do_type.currentText() == 'CloseUIPanel':
                    self.ui.lbl_gd_do_cont1.setText('PanelName')
                elif self.ui.cbox_gd_do_type.currentText() == 'UnlockNewTeleport' or self.ui.cbox_gd_do_type.currentText() == 'DefaultTeleport':
                    self.ui.lbl_gd_do_cont1.setText('TeleportTag')
                elif self.ui.cbox_gd_do_type.currentText() == 'UnlockModule':
                    self.ui.lbl_gd_do_cont1.setText('Module')
                elif self.ui.cbox_gd_do_type.currentText() == 'ClearMapEvent':
                    self.ui.lbl_gd_do_cont1.setText('NodeId')
                elif self.ui.cbox_gd_do_type.currentText() == 'ChangeHero':
                    self.ui.lbl_gd_do_cont1.setText('SkinId')
                elif self.ui.cbox_gd_do_type.currentText() == 'LockSkin' or self.ui.cbox_gd_do_type.currentText() == 'UnlockSkin':
                    self.ui.lbl_gd_do_cont1.setText('HeroSkinIds')
                elif self.ui.cbox_gd_do_type.currentText() == 'LockCardPackage' or self.ui.cbox_gd_do_type.currentText() == 'UnlockCardPackage':
                    self.ui.lbl_gd_do_cont1.setText('CardPackages')
                elif self.ui.cbox_gd_do_type.currentText() == 'WaitEventCompleted':
                    self.ui.lbl_gd_do_cont1.setText('NodeIds')
                elif self.ui.cbox_gd_do_type.currentText() == 'HideHeroThumbnail':
                    self.ui.lbl_gd_do_cont1.setText('HeroSkinIds')
                else:
                    pass

            elif self.ui.cbox_gd_do_type.currentText() in ['SetBlink', 'HideUIObject', 'ShowUIObject',
                                                           'SetInteractable', 'SetCanWalk', 'PlayAVG', 'EnterAdventure',
                                                           'Teleport', 'WaitAreaOpen', 'WaitAreaClose', 'WaitMoveTo',
                                                           'ShowSingleEffect', 'AddMapEvent', 'PlayVideo', 'PlayBgm',
                                                           'HeroEvolutionHideHero']:
                self.ui.lbl_gd_do_cont1.setVisible(True)
                self.ui.lbl_gd_do_cont2.setVisible(True)
                self.ui.lbl_gd_do_cont3.setVisible(False)
                self.ui.lbl_gd_do_cont4.setVisible(False)
                self.ui.lbl_gd_do_cont5.setVisible(False)
                self.ui.le_gd_do_cont1.setVisible(True)
                self.ui.le_gd_do_cont2.setVisible(True)
                self.ui.le_gd_do_cont3.setVisible(False)
                self.ui.le_gd_do_cont4.setVisible(False)
                self.ui.le_gd_do_cont5.setVisible(False)

                if self.ui.cbox_gd_do_type.currentText() == 'SetBlink':
                    self.ui.lbl_gd_do_cont1.setText('Position')
                    self.ui.lbl_gd_do_cont2.setText('Rotation')

                elif self.ui.cbox_gd_do_type.currentText() == 'HideUIObject' or self.ui.cbox_gd_do_type.currentText() == 'ShowUIObject' or self.ui.cbox_gd_do_type.currentText() == 'SetInteractable':
                    self.ui.lbl_gd_do_cont1.setText('Panel')
                    self.ui.lbl_gd_do_cont2.setText('Objects')

                elif self.ui.cbox_gd_do_type.currentText() == 'SetCanWalk':
                    self.ui.lbl_gd_do_cont1.setText('NodeIds')
                    self.ui.lbl_gd_do_cont2.setText('CanWalk')

                elif self.ui.cbox_gd_do_type.currentText() == 'PlayAVG':
                    self.ui.lbl_gd_do_cont1.setText('Name')
                    self.ui.lbl_gd_do_cont2.setText('StopBgm')

                elif self.ui.cbox_gd_do_type.currentText() == 'EnterAdventure':
                    self.ui.lbl_gd_do_cont1.setText('AreaId')
                    self.ui.lbl_gd_do_cont2.setText('SectionId')

                elif self.ui.cbox_gd_do_type.currentText() == 'Teleport':
                    self.ui.lbl_gd_do_cont1.setText('MapId')
                    self.ui.lbl_gd_do_cont2.setText('NodeId')

                elif self.ui.cbox_gd_do_type.currentText() == 'WaitAreaOpen' or self.ui.cbox_gd_do_type.currentText() == 'WaitAreaClose':
                    self.ui.lbl_gd_do_cont1.setText('MapId')
                    self.ui.lbl_gd_do_cont2.setText('AreaId')

                elif self.ui.cbox_gd_do_type.currentText() == 'WaitMoveTo':
                    self.ui.lbl_gd_do_cont1.setText('PassingNodes')
                    self.ui.lbl_gd_do_cont2.setText('ArrivalNodes')

                elif self.ui.cbox_gd_do_type.currentText() == 'ShowSingleEffect':
                    self.ui.lbl_gd_do_cont1.setText('EffectName')
                    self.ui.lbl_gd_do_cont2.setText('OverridElements')

                elif self.ui.cbox_gd_do_type.currentText() == 'AddMapEvent':
                    self.ui.lbl_gd_do_cont1.setText('NodeId')
                    self.ui.lbl_gd_do_cont2.setText('Data')

                elif self.ui.cbox_gd_do_type.currentText() == 'PlayVideo':
                    self.ui.lbl_gd_do_cont1.setText('ClipPath')
                    self.ui.lbl_gd_do_cont2.setText('CanSkip')

                elif self.ui.cbox_gd_do_type.currentText() == 'PlayBgm':
                    self.ui.lbl_gd_do_cont1.setText('BgmName')
                    self.ui.lbl_gd_do_cont2.setText('Replay')

                elif self.ui.cbox_gd_do_type.currentText() == 'HeroEvolutionHideHero':
                    self.ui.lbl_gd_do_cont1.setText('HeroSkinIds')
                    self.ui.lbl_gd_do_cont2.setText('HeroIds')

                else:
                    pass


            elif self.ui.cbox_gd_do_type.currentText() in ['Highlight', 'SetElementAngle']:
                self.ui.lbl_gd_do_cont1.setVisible(True)
                self.ui.lbl_gd_do_cont2.setVisible(True)
                self.ui.lbl_gd_do_cont3.setVisible(True)
                self.ui.lbl_gd_do_cont4.setVisible(False)
                self.ui.lbl_gd_do_cont5.setVisible(False)
                self.ui.le_gd_do_cont1.setVisible(True)
                self.ui.le_gd_do_cont2.setVisible(True)
                self.ui.le_gd_do_cont3.setVisible(True)
                self.ui.le_gd_do_cont4.setVisible(False)
                self.ui.le_gd_do_cont5.setVisible(False)

                if self.ui.cbox_gd_do_type.currentText() == 'Highlight':
                    self.ui.lbl_gd_do_cont1.setText('Panel')
                    self.ui.lbl_gd_do_cont2.setText('Objects')
                    self.ui.lbl_gd_do_cont3.setText('Order')

                elif self.ui.cbox_gd_do_type.currentText() == 'SetElementAngle':
                    self.ui.lbl_gd_do_cont1.setText('NodeId')
                    self.ui.lbl_gd_do_cont2.setText('Angle')
                    self.ui.lbl_gd_do_cont3.setText('Duration')

                else:
                    pass

            elif self.ui.cbox_gd_do_type.currentText() in ['SetTips', 'LoadElement']:
                self.ui.lbl_gd_do_cont1.setVisible(True)
                self.ui.lbl_gd_do_cont2.setVisible(True)
                self.ui.lbl_gd_do_cont3.setVisible(True)
                self.ui.lbl_gd_do_cont4.setVisible(True)
                self.ui.lbl_gd_do_cont5.setVisible(True)
                self.ui.le_gd_do_cont1.setVisible(True)
                self.ui.le_gd_do_cont2.setVisible(True)
                self.ui.le_gd_do_cont3.setVisible(True)
                self.ui.le_gd_do_cont4.setVisible(True)
                self.ui.le_gd_do_cont5.setVisible(True)

                if self.ui.cbox_gd_do_type.currentText() == 'SetTips':
                    self.ui.lbl_gd_do_cont1.setText('Text')
                    self.ui.lbl_gd_do_cont2.setText('Position')
                    self.ui.lbl_gd_do_cont3.setText('ShowFrame')
                    self.ui.lbl_gd_do_cont4.setText('AutoDisappear')
                    self.ui.lbl_gd_do_cont5.setText('Duration')

                elif self.ui.cbox_gd_do_type.currentText() == 'LoadElement':
                    self.ui.lbl_gd_do_cont1.setText('NodeId')
                    self.ui.lbl_gd_do_cont2.setText('ElementKey')
                    self.ui.lbl_gd_do_cont3.setText('Position')
                    self.ui.lbl_gd_do_cont4.setText('EulerAngles')
                    self.ui.lbl_gd_do_cont5.setText('Scale')
                else:
                    pass

            else:
                pass

    def btnClickEvent(self):
        sender = self.sender()
        if sender == self.ui.btn_gd_tri_insert:
            if self.ui.cbox_gd_tri_type.currentText() == '请选择类型':
                self.ui.statusbar.showMessage('请选择触发类型')
                return

            elif self.ui.cbox_gd_tri_type.currentText() == 'LoginSuccess':
                root = QTreeWidgetItem(self.ui.tree_gd_tri)
                root.setText(0, 'Data')
                child = QTreeWidgetItem(root)
                child.setText(0, 'TriggerType')
                child.setText(1, self.ui.cbox_gd_tri_type.currentText())
                self.ui.tree_gd_tri.addTopLevelItem(root)

            elif self.ui.cbox_gd_tri_type.currentText() in ['OpenPanel', 'NPCClick', 'GuideCompleted', 'ArrivalNode',
                                                            'PassingNode', 'UIClick']:
                root = QTreeWidgetItem(self.ui.tree_gd_tri)
                root.setText(0, 'Data')
                child1 = QTreeWidgetItem(root)
                child1.setText(0, 'TriggerType')
                child1.setText(1, self.ui.cbox_gd_tri_type.currentText())

                child2 = QTreeWidgetItem(root)
                child2.setText(0, self.ui.lbl_gd_tri_cont1.text())
                child2.setText(1, self.ui.le_gd_tri_cont1.text())

                self.ui.tree_gd_tri.addTopLevelItem(root)

            elif self.ui.cbox_gd_tri_type.currentText() == 'OpenArea':
                root = QTreeWidgetItem(self.ui.tree_gd_tri)
                root.setText(0, 'Data')
                child1 = QTreeWidgetItem(root)
                child1.setText(0, 'TriggerType')
                child1.setText(1, self.ui.cbox_gd_tri_type.currentText())

                child2 = QTreeWidgetItem(root)
                child2.setText(0, self.ui.lbl_gd_tri_cont1.text())
                child2.setText(1, self.ui.le_gd_tri_cont1.text())

                child3 = QTreeWidgetItem(root)
                child3.setText(0, self.ui.lbl_gd_tri_cont2.text())
                child3.setText(1, self.ui.le_gd_tri_cont2.text())

                self.ui.tree_gd_tri.addTopLevelItem(root)

            else:
                return

        elif sender == self.ui.btn_gd_pre_insert:
            if self.ui.cbox_gd_pre_type.currentText() == '请选择类型':
                self.ui.statusbar.showMessage('请选择前置条件类型')
                return

            elif self.ui.cbox_gd_pre_type.currentText() == 'GuideCompleted':
                root = QTreeWidgetItem(self.ui.tree_gd_pre)
                root.setText(0, 'Data')
                child1 = QTreeWidgetItem(root)
                child1.setText(0, 'TriggerType')
                child1.setText(1, self.ui.cbox_gd_pre_type.currentText())

                child2 = QTreeWidgetItem(root)
                child2.setText(0, self.ui.lbl_gd_pre_cont1.text())
                child2.setText(1, self.ui.le_gd_pre_cont1.text())

                self.ui.tree_gd_pre.addTopLevelItem(root)

            else:
                return

        elif sender == self.ui.btn_gd_do_insert_big:
            if self.ui.cbox_gd_do_type.currentText() == "请选择类型":
                self.ui.statusbar.showMessage('请选择执行效果类型')
                return

            else:
                root = QTreeWidgetItem(self.ui.tree_gd_do)
                root.setText(0, 'NodeData')

                child_is_click_to_next = QTreeWidgetItem(root)
                child_is_click_to_next.setText(0, self.ui.lbl_gd_click_to_next.text())
                child_is_click_to_next.setText(1, self.ui.cbox_gd_click_to_nex.currentText())

                child_is_auto_to_next = QTreeWidgetItem(root)
                child_is_auto_to_next.setText(0, self.ui.lbl_gd_auto_to_next.text())
                child_is_auto_to_next.setText(1, self.ui.cbox_gd_auto_to_nex.currentText())

                root_dodata = QTreeWidgetItem(root)
                root_dodata.setText(0, 'DoData')

                root_dodata_data = QTreeWidgetItem(root_dodata)
                root_dodata_data.setText(0, 'Data')

                do_data_child_type = QTreeWidgetItem(root_dodata_data)
                do_data_child_type.setText(0, 'DoType')
                do_data_child_type.setText(1, self.ui.cbox_gd_do_type.currentText())

                if self.ui.cbox_gd_do_type.currentText() in ['ClearTips', 'HideMask', 'ShowMask', 'ClearHighlight',
                                                             'ClearGuidePanel', 'Complete', 'EnterGame', 'PauseBgm']:
                    pass

                elif self.ui.cbox_gd_do_type.currentText() in ['SetMaskAlpha', 'ShowPictures', 'SetInteractableNames',
                                                               'WaitPanelOpen', 'WaitPanelClose', 'SetMapActive',
                                                               'ShowNodeElement', 'HideNodeElement', 'EnableNodeEvent',
                                                               'DisableNodeEvent', 'LoadNpc', 'DestroyNPC', 'Await',
                                                               'OpenUIPanel', 'CloseUIPanel', 'UnlockModule',
                                                               'DefaultTeleport', 'UnlockNewTeleport', 'ClearMapEvent',
                                                               'ChangeHero', 'LockSkin', 'UnlockSkin',
                                                               'LockCardPackage',
                                                               'UnlockCardPackage', 'WaitEventCompleted',
                                                               'HideHeroThumbnail']:
                    do_data_child1 = QTreeWidgetItem(root_dodata_data)
                    do_data_child1.setText(0, self.ui.lbl_gd_do_cont1.text())
                    do_data_child1.setText(1, self.ui.le_gd_do_cont1.text())

                elif self.ui.cbox_gd_do_type.currentText() in ['SetBlink', 'HideUIObject', 'ShowUIObject',
                                                               'SetInteractable', 'SetCanWalk', 'PlayAVG',
                                                               'EnterAdventure',
                                                               'Teleport', 'WaitAreaOpen', 'WaitAreaClose',
                                                               'WaitMoveTo',
                                                               'ShowSingleEffect', 'AddMapEvent', 'PlayVideo',
                                                               'PlayBgm',
                                                               'HeroEvolutionHideHero']:
                    do_data_child1 = QTreeWidgetItem(root_dodata_data)
                    do_data_child1.setText(0, self.ui.lbl_gd_do_cont1.text())
                    do_data_child1.setText(1, self.ui.le_gd_do_cont1.text())
                    do_data_child2 = QTreeWidgetItem(root_dodata_data)
                    do_data_child2.setText(0, self.ui.lbl_gd_do_cont2.text())
                    do_data_child2.setText(1, self.ui.le_gd_do_cont2.text())

                elif self.ui.cbox_gd_do_type.currentText() in ['Highlight', 'SetElementAngle']:
                    do_data_child1 = QTreeWidgetItem(root_dodata_data)
                    do_data_child1.setText(0, self.ui.lbl_gd_do_cont1.text())
                    do_data_child1.setText(1, self.ui.le_gd_do_cont1.text())
                    do_data_child2 = QTreeWidgetItem(root_dodata_data)
                    do_data_child2.setText(0, self.ui.lbl_gd_do_cont2.text())
                    do_data_child2.setText(1, self.ui.le_gd_do_cont2.text())
                    do_data_child3 = QTreeWidgetItem(root_dodata_data)
                    do_data_child3.setText(0, self.ui.lbl_gd_do_cont3.text())
                    do_data_child3.setText(1, self.ui.le_gd_do_cont3.text())

                elif self.ui.cbox_gd_do_type.currentText() in ['SetTips', 'LoadElement']:
                    do_data_child1 = QTreeWidgetItem(root_dodata_data)
                    do_data_child1.setText(0, self.ui.lbl_gd_do_cont1.text())
                    do_data_child1.setText(1, self.ui.le_gd_do_cont1.text())
                    do_data_child2 = QTreeWidgetItem(root_dodata_data)
                    do_data_child2.setText(0, self.ui.lbl_gd_do_cont2.text())
                    do_data_child2.setText(1, self.ui.le_gd_do_cont2.text())
                    do_data_child3 = QTreeWidgetItem(root_dodata_data)
                    do_data_child3.setText(0, self.ui.lbl_gd_do_cont3.text())
                    do_data_child3.setText(1, self.ui.le_gd_do_cont3.text())
                    do_data_child4 = QTreeWidgetItem(root_dodata_data)
                    do_data_child4.setText(0, self.ui.lbl_gd_do_cont4.text())
                    do_data_child4.setText(1, self.ui.le_gd_do_cont4.text())
                    do_data_child5 = QTreeWidgetItem(root_dodata_data)
                    do_data_child5.setText(0, self.ui.lbl_gd_do_cont5.text())
                    do_data_child5.setText(1, self.ui.le_gd_do_cont5.text())

                else:
                    return

            self.ui.tree_gd_do.addTopLevelItem(root)

        elif sender == self.ui.btn_create:
            if self.ui.le_gd_name.text() == '':
                self.ui.statusbar.showMessage('请先输入引导名')
                return
            else:
                self.gd_content['GuideName'] = self.ui.le_gd_name.text()

            if self.ui.tree_gd_tri.topLevelItem(0) is None:
                self.ui.statusbar.showMessage('触发条件不存在')
                return
            else:
                list_gd_tri_data = []
                for i in range(self.ui.tree_gd_tri.topLevelItemCount()):
                    dict_gd_tri_data1 = {}
                    dict_gd_tri_data2 = {}
                    for j in range(self.ui.tree_gd_tri.topLevelItem(i).childCount()):
                        dict_gd_tri_data2[
                            self.ui.tree_gd_tri.topLevelItem(i).child(j).text(0)] = self.ui.tree_gd_tri.topLevelItem(
                            i).child(j).text(1)
                    dict_gd_tri_data1['Data'] = dict_gd_tri_data2
                    list_gd_tri_data.append(dict_gd_tri_data1)
                self.gd_content['Triggers'] = list_gd_tri_data

            if self.ui.tree_gd_pre.topLevelItem(0) is None:
                self.ui.statusbar.showMessage('前置条件不存在')
                return

            else:
                list_gd_pre_data = []
                for i in range(self.ui.tree_gd_pre.topLevelItemCount()):
                    dict_gd_pre_data1 = {}
                    dict_gd_pre_data2 = {}
                    for j in range(self.ui.tree_gd_pre.topLevelItem(i).childCount()):
                        dict_gd_pre_data2[
                            self.ui.tree_gd_pre.topLevelItem(i).child(j).text(0)] = self.ui.tree_gd_pre.topLevelItem(
                            i).child(j).text(1)
                    dict_gd_pre_data1['Data'] = dict_gd_pre_data2
                    list_gd_pre_data.append(dict_gd_pre_data1)
                self.gd_content['Preconditions'] = list_gd_pre_data

            if self.ui.tree_gd_do.topLevelItem(0) is None:
                self.ui.statusbar.showMessage('执行效果不存在')
                return

            else:
                list_gd_nodedata = []
                for i in range(self.ui.tree_gd_do.topLevelItemCount()):
                    dict_gd_nodedata = {}
                    dict_gd_nodedata[self.ui.lbl_gd_click_to_next.text()] = self.ui.cbox_gd_click_to_nex.currentText()
                    dict_gd_nodedata[self.ui.lbl_gd_auto_to_next.text()] = self.ui.cbox_gd_auto_to_nex.currentText()
                    list_gd_dodata = []
                    dict_gd_dodata1 = {}
                    dict_gd_dodata2 = {}
                    for j1 in range(self.ui.tree_gd_do.topLevelItem(i).childCount()):
                        for j2 in range(self.ui.tree_gd_do.topLevelItem(i).child(j1).childCount()):
                            dict_gd_dodata2[self.ui.tree_gd_do.topLevelItem(i).child(j1).child(j2).text(0)] = self.ui.tree_gd_do.topLevelItem(i).child(j1).child(j2).text(1)
                    dict_gd_dodata1['Data'] = dict_gd_dodata2
                    list_gd_dodata.append(dict_gd_dodata1)
                    print('1')
                    dict_gd_nodedata['DoData'] = list_gd_dodata
                    list_gd_nodedata.append(dict_gd_nodedata)
                self.gd_content['NodeData'] = list_gd_nodedata

            final_gd_content = json.dumps(self.gd_content, indent=4)
            self.ui.pte_preview.setPlainText(str(final_gd_content))
