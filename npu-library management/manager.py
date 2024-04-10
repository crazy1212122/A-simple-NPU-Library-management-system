from PyQt5 import QtCore, QtGui, QtWidgets
from connect import *
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox,QFileDialog
import bjgl
import sys
import math
import time
import pandas as pd
import pymysql

cursor,conn=connect()
class Ui_Admin(object):
        def setupUi(self, bookadmin):
                bookadmin.setObjectName("Form3")
                bookadmin.resize(1150, 725)
                self.tabWidget = QtWidgets.QTabWidget(bookadmin)
                self.tabWidget.setGeometry(QtCore.QRect(30, 30, 1051, 661))
                self.tabWidget.setStyleSheet("#shuji\n"
                                             "{\n"
                                             "    border-image: url(:/书2.jpg);\n"
                                             "}\n"
                                             "#xuesheng\n"
                                             "{\n"
                                             "    border-image: url(:/书2.jpg);\n"
                                             "}\n"
                                             "#jieyue\n"
                                             "{\n"
                                             "    border-image: url(:/书2.jpg);\n"
                                             "}\n"
                                             "#drsj\n"
                                             "{\n"
                                             "    border-image: url(:/书2.jpg);\n"
                                             "}\n"
                                             "#drxs\n"
                                             "{\n"
                                             "    border-image: url(:/书2.jpg);\n"
                                             "}\n"
                                             "#manager_add\n"
                                             "{\n"
                                             "    border-image: url(:/书2.jpg);\n"
                                             "}\n"
                                             "#dljl\n"
                                             "{\n"
                                             "    border-image: url(:/书2.jpg);\n"
                                             "}")
                self.tabWidget.setDocumentMode(False)
                self.tabWidget.setObjectName("tabWidget")
                self.shuji = QtWidgets.QWidget()
                self.shuji.setObjectName("shuji")
                self.shujibiao = QtWidgets.QTableWidget(self.shuji)
                self.shujibiao.setGeometry(QtCore.QRect(0, 0, 701, 481))
                self.shujibiao.setObjectName("shujibiao")
                self.shujibiao.setColumnCount(9)
                self.shujibiao.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao.setHorizontalHeaderItem(7, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao.setHorizontalHeaderItem(8, item)
                self.widget = QtWidgets.QWidget(self.shuji)
                self.widget.setGeometry(QtCore.QRect(710, 20, 331, 461))
                self.widget.setStyleSheet("")
                self.widget.setObjectName("widget")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
                self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.sm = QtWidgets.QLineEdit(self.widget)
                self.sm.setMinimumSize(QtCore.QSize(300, 40))
                self.sm.setText("")
                self.sm.setObjectName("sm")
                self.verticalLayout_3.addWidget(self.sm)
                self.sh = QtWidgets.QLineEdit(self.widget)
                self.sh.setMinimumSize(QtCore.QSize(300, 40))
                self.sh.setText("")
                self.sh.setObjectName("sh")
                self.verticalLayout_3.addWidget(self.sh)
                self.zz = QtWidgets.QLineEdit(self.widget)
                self.zz.setMinimumSize(QtCore.QSize(300, 40))
                self.zz.setText("")
                self.zz.setObjectName("zz")
                self.verticalLayout_3.addWidget(self.zz)
                self.cb = QtWidgets.QLineEdit(self.widget)
                self.cb.setMinimumSize(QtCore.QSize(300, 40))
                self.cb.setObjectName("cb")
                self.verticalLayout_3.addWidget(self.cb)
                self.bj = QtWidgets.QLineEdit(self.widget)
                self.bj.setMinimumSize(QtCore.QSize(300, 40))
                self.bj.setObjectName("bj")
                self.verticalLayout_3.addWidget(self.bj)
                self.jc = QtWidgets.QLineEdit(self.widget)
                self.jc.setMinimumSize(QtCore.QSize(300, 40))
                self.jc.setObjectName("jc")
                self.verticalLayout_3.addWidget(self.jc)
                self.gc = QtWidgets.QLineEdit(self.widget)
                self.gc.setMinimumSize(QtCore.QSize(300, 40))
                self.gc.setObjectName("gc")
                self.verticalLayout_3.addWidget(self.gc)
                self.shujihao = QtWidgets.QLineEdit(self.widget)
                self.shujihao.setMinimumSize(QtCore.QSize(300, 40))
                self.shujihao.setObjectName("shujihao")
                self.verticalLayout_3.addWidget(self.shujihao)
                self.lineEdit = QtWidgets.QLineEdit(self.widget)
                self.lineEdit.setMinimumSize(QtCore.QSize(300, 40))
                self.lineEdit.setObjectName("lineEdit")
                self.verticalLayout_3.addWidget(self.lineEdit)
                self.layoutWidget = QtWidgets.QWidget(self.shuji)
                self.layoutWidget.setGeometry(QtCore.QRect(0, 490, 771, 131))
                self.layoutWidget.setObjectName("layoutWidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout()
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.tainjia1 = QtWidgets.QPushButton(self.layoutWidget)
                self.tainjia1.setMinimumSize(QtCore.QSize(200, 50))
                self.tainjia1.setObjectName("tainjia1")
                self.verticalLayout_2.addWidget(self.tainjia1)
                self.xiugai1 = QtWidgets.QPushButton(self.layoutWidget)
                self.xiugai1.setMinimumSize(QtCore.QSize(200, 50))
                self.xiugai1.setObjectName("xiugai1")
                self.verticalLayout_2.addWidget(self.xiugai1)
                self.horizontalLayout.addLayout(self.verticalLayout_2)
                self.verticalLayout = QtWidgets.QVBoxLayout()
                self.verticalLayout.setObjectName("verticalLayout")
                self.shanchu1 = QtWidgets.QPushButton(self.layoutWidget)
                self.shanchu1.setMinimumSize(QtCore.QSize(0, 50))
                self.shanchu1.setObjectName("shanchu1")
                self.verticalLayout.addWidget(self.shanchu1)
                self.jilu = QtWidgets.QPushButton(self.layoutWidget)
                self.jilu.setMinimumSize(QtCore.QSize(0, 50))
                self.jilu.setObjectName("jilu")
                self.verticalLayout.addWidget(self.jilu)
                self.horizontalLayout.addLayout(self.verticalLayout)
                self.cxqb1 = QtWidgets.QPushButton(self.shuji)
                self.cxqb1.setGeometry(QtCore.QRect(810, 490, 201, 131))
                self.cxqb1.setObjectName("cxqb1")
                self.tabWidget.addTab(self.shuji, "")
                self.xuesheng = QtWidgets.QWidget()
                self.xuesheng.setObjectName("xuesheng")
                self.tableWidget = QtWidgets.QTableWidget(self.xuesheng)
                self.tableWidget.setGeometry(QtCore.QRect(0, 0, 701, 481))
                self.tableWidget.setObjectName("tableWidget")
                self.tableWidget.setColumnCount(9)
                self.tableWidget.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(7, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(8, item)
                self.widget_2 = QtWidgets.QWidget(self.xuesheng)
                self.widget_2.setGeometry(QtCore.QRect(710, 10, 331, 471))
                self.widget_2.setObjectName("widget_2")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
                self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.sh_2 = QtWidgets.QLineEdit(self.widget_2)
                self.sh_2.setMinimumSize(QtCore.QSize(300, 40))
                self.sh_2.setText("")
                self.sh_2.setObjectName("sh_2")
                self.verticalLayout_4.addWidget(self.sh_2)
                self.sm_2 = QtWidgets.QLineEdit(self.widget_2)
                self.sm_2.setMinimumSize(QtCore.QSize(300, 40))
                self.sm_2.setText("")
                self.sm_2.setObjectName("sm_2")
                self.verticalLayout_4.addWidget(self.sm_2)
                self.zz_2 = QtWidgets.QLineEdit(self.widget_2)
                self.zz_2.setMinimumSize(QtCore.QSize(300, 40))
                self.zz_2.setText("")
                self.zz_2.setObjectName("zz_2")
                self.verticalLayout_4.addWidget(self.zz_2)
                self.xb_2 = QtWidgets.QComboBox(self.widget_2)
                self.xb_2.setMinimumSize(QtCore.QSize(300, 40))
                self.xb_2.setAccessibleName("")
                self.xb_2.setObjectName("xb_2")
                self.xb_2.addItem("")
                self.xb_2.addItem("")
                self.verticalLayout_4.addWidget(self.xb_2)
                self.xb = QtWidgets.QComboBox(self.widget_2)
                self.xb.setMinimumSize(QtCore.QSize(300, 40))
                self.xb.setObjectName("xb")
                self.xb.addItem("")
                self.xb.addItem("")
                self.xb.addItem("")
                self.xb.addItem("")
                self.xb.setItemText(3, "")
                self.verticalLayout_4.addWidget(self.xb)
                self.dh = QtWidgets.QLineEdit(self.widget_2)
                self.dh.setMinimumSize(QtCore.QSize(300, 40))
                self.dh.setObjectName("dh")
                self.verticalLayout_4.addWidget(self.dh)
                self.kj = QtWidgets.QLineEdit(self.widget_2)
                self.kj.setMinimumSize(QtCore.QSize(300, 40))
                self.kj.setObjectName("kj")
                self.verticalLayout_4.addWidget(self.kj)
                self.xy = QtWidgets.QLineEdit(self.widget_2)
                self.xy.setMinimumSize(QtCore.QSize(300, 40))
                self.xy.setObjectName("xy")
                self.verticalLayout_4.addWidget(self.xy)
                self.mm = QtWidgets.QLineEdit(self.widget_2)
                self.mm.setMinimumSize(QtCore.QSize(300, 40))
                self.mm.setObjectName("mm")
                self.verticalLayout_4.addWidget(self.mm)
                self.layoutWidget_2 = QtWidgets.QWidget(self.xuesheng)
                self.layoutWidget_2.setGeometry(QtCore.QRect(0, 490, 771, 131))
                self.layoutWidget_2.setObjectName("layoutWidget_2")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout()
                self.verticalLayout_5.setObjectName("verticalLayout_5")
                self.tainjia2 = QtWidgets.QPushButton(self.layoutWidget_2)
                self.tainjia2.setMinimumSize(QtCore.QSize(200, 50))
                self.tainjia2.setObjectName("tainjia2")
                self.verticalLayout_5.addWidget(self.tainjia2)
                self.xiugai2 = QtWidgets.QPushButton(self.layoutWidget_2)
                self.xiugai2.setMinimumSize(QtCore.QSize(200, 50))
                self.xiugai2.setObjectName("xiugai2")
                self.verticalLayout_5.addWidget(self.xiugai2)
                self.horizontalLayout_2.addLayout(self.verticalLayout_5)
                self.verticalLayout_6 = QtWidgets.QVBoxLayout()
                self.verticalLayout_6.setObjectName("verticalLayout_6")
                self.shanchu2 = QtWidgets.QPushButton(self.layoutWidget_2)
                self.shanchu2.setMinimumSize(QtCore.QSize(0, 50))
                self.shanchu2.setObjectName("shanchu2")
                self.verticalLayout_6.addWidget(self.shanchu2)
                self.jilu2 = QtWidgets.QPushButton(self.layoutWidget_2)
                self.jilu2.setMinimumSize(QtCore.QSize(0, 50))
                self.jilu2.setObjectName("jilu2")
                self.verticalLayout_6.addWidget(self.jilu2)
                self.horizontalLayout_2.addLayout(self.verticalLayout_6)
                self.cxqb2 = QtWidgets.QPushButton(self.xuesheng)
                self.cxqb2.setGeometry(QtCore.QRect(810, 490, 201, 131))
                self.cxqb2.setObjectName("cxqb2")
                self.tabWidget.addTab(self.xuesheng, "")
                self.jieyue = QtWidgets.QWidget()
                self.jieyue.setObjectName("jieyue")
                self.jieyuebiao = QtWidgets.QTableWidget(self.jieyue)
                self.jieyuebiao.setGeometry(QtCore.QRect(0, 0, 641, 481))
                self.jieyuebiao.setObjectName("jieyuebiao")
                self.jieyuebiao.setColumnCount(5)
                self.jieyuebiao.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.jieyuebiao.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.jieyuebiao.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.jieyuebiao.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.jieyuebiao.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.jieyuebiao.setHorizontalHeaderItem(4, item)
                self.pz = QtWidgets.QPushButton(self.jieyue)
                self.pz.setGeometry(QtCore.QRect(700, 140, 300, 40))
                self.pz.setMinimumSize(QtCore.QSize(300, 40))
                self.pz.setObjectName("pz")
                self.bh = QtWidgets.QPushButton(self.jieyue)
                self.bh.setGeometry(QtCore.QRect(700, 240, 300, 40))
                self.bh.setMinimumSize(QtCore.QSize(300, 40))
                self.bh.setObjectName("bh")
                self.sx = QtWidgets.QPushButton(self.jieyue)
                self.sx.setGeometry(QtCore.QRect(700, 330, 300, 40))
                self.sx.setMinimumSize(QtCore.QSize(300, 40))
                self.sx.setObjectName("sx")
                self.tabWidget.addTab(self.jieyue, "")
                self.drsj = QtWidgets.QWidget()
                self.drsj.setObjectName("drsj")
                self.shujibiao_2 = QtWidgets.QTableWidget(self.drsj)
                self.shujibiao_2.setGeometry(QtCore.QRect(20, 20, 1001, 441))
                self.shujibiao_2.setObjectName("shujibiao_2")
                self.shujibiao_2.setColumnCount(9)
                self.shujibiao_2.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao_2.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao_2.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao_2.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao_2.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao_2.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao_2.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao_2.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao_2.setHorizontalHeaderItem(7, item)
                item = QtWidgets.QTableWidgetItem()
                self.shujibiao_2.setHorizontalHeaderItem(8, item)
                self.cxqb3 = QtWidgets.QPushButton(self.drsj)
                self.cxqb3.setGeometry(QtCore.QRect(790, 480, 201, 131))
                self.cxqb3.setObjectName("cxqb3")
                self.mulu2 = QtWidgets.QLineEdit(self.drsj)
                self.mulu2.setGeometry(QtCore.QRect(20, 490, 651, 31))
                self.mulu2.setObjectName("mulu2")
                self.mulu1 = QtWidgets.QToolButton(self.drsj)
                self.mulu1.setGeometry(QtCore.QRect(670, 490, 51, 31))
                self.mulu1.setObjectName("mulu1")
                self.qd = QtWidgets.QPushButton(self.drsj)
                self.qd.setGeometry(QtCore.QRect(230, 540, 221, 71))
                self.qd.setObjectName("qd")
                self.tabWidget.addTab(self.drsj, "")
                self.drxs = QtWidgets.QWidget()
                self.drxs.setObjectName("drxs")
                self.tableWidget_2 = QtWidgets.QTableWidget(self.drxs)
                self.tableWidget_2.setGeometry(QtCore.QRect(20, 20, 1001, 441))
                self.tableWidget_2.setObjectName("tableWidget_2")
                self.tableWidget_2.setColumnCount(9)
                self.tableWidget_2.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(6, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(7, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setHorizontalHeaderItem(8, item)
                self.mulu4 = QtWidgets.QLineEdit(self.drxs)
                self.mulu4.setGeometry(QtCore.QRect(20, 490, 651, 31))
                self.mulu4.setObjectName("mulu4")
                self.mulu3 = QtWidgets.QToolButton(self.drxs)
                self.mulu3.setGeometry(QtCore.QRect(670, 490, 51, 31))
                self.mulu3.setObjectName("mulu3")
                self.qd_2 = QtWidgets.QPushButton(self.drxs)
                self.qd_2.setGeometry(QtCore.QRect(230, 540, 221, 71))
                self.qd_2.setObjectName("qd_2")
                self.cxqb4 = QtWidgets.QPushButton(self.drxs)
                self.cxqb4.setGeometry(QtCore.QRect(790, 480, 201, 131))
                self.cxqb4.setObjectName("cxqb4")
                self.tabWidget.addTab(self.drxs, "")
                self.manager_add = QtWidgets.QWidget()
                self.manager_add.setObjectName("manager_add")
                self.tongyi = QtWidgets.QPushButton(self.manager_add)
                self.tongyi.setGeometry(QtCore.QRect(120, 430, 111, 41))
                self.tongyi.setObjectName("tongyi")
                self.jujue = QtWidgets.QPushButton(self.manager_add)
                self.jujue.setGeometry(QtCore.QRect(120, 490, 111, 41))
                self.jujue.setObjectName("jujue")
                self.glypizhun = QtWidgets.QTableWidget(self.manager_add)
                self.glypizhun.setGeometry(QtCore.QRect(60, 90, 251, 311))
                self.glypizhun.setObjectName("glypizhun")
                self.glypizhun.setColumnCount(2)
                self.glypizhun.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.glypizhun.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.glypizhun.setHorizontalHeaderItem(1, item)
                self.glyzhuce = QtWidgets.QTableWidget(self.manager_add)
                self.glyzhuce.setGeometry(QtCore.QRect(370, 90, 251, 311))
                self.glyzhuce.setObjectName("glyzhuce")
                self.glyzhuce.setColumnCount(2)
                self.glyzhuce.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.glyzhuce.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.glyzhuce.setHorizontalHeaderItem(1, item)
                self.select_all = QtWidgets.QPushButton(self.manager_add)
                self.select_all.setGeometry(QtCore.QRect(410, 540, 141, 31))
                self.select_all.setObjectName("select_all")
                self.tjzhuce = QtWidgets.QPushButton(self.manager_add)
                self.tjzhuce.setGeometry(QtCore.QRect(410, 580, 141, 28))
                self.tjzhuce.setObjectName("tjzhuce")
                self.all = QtWidgets.QTableWidget(self.manager_add)
                self.all.setGeometry(QtCore.QRect(680, 90, 341, 311))
                self.all.setObjectName("all")
                self.all.setColumnCount(3)
                self.all.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.all.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.all.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.all.setHorizontalHeaderItem(2, item)
                self.single_choose = QtWidgets.QPushButton(self.manager_add)
                self.single_choose.setGeometry(QtCore.QRect(790, 540, 131, 31))
                self.single_choose.setObjectName("single_choose")
                self.update_password = QtWidgets.QPushButton(self.manager_add)
                self.update_password.setGeometry(QtCore.QRect(790, 580, 131, 31))
                self.update_password.setObjectName("update_password")
                self.chaxunall = QtWidgets.QPushButton(self.manager_add)
                self.chaxunall.setGeometry(QtCore.QRect(120, 547, 111, 41))
                self.chaxunall.setObjectName("chaxunall")
                self.id = QtWidgets.QLineEdit(self.manager_add)
                self.id.setGeometry(QtCore.QRect(400, 420, 171, 31))
                self.id.setText("")
                self.id.setObjectName("id")
                self.name1 = QtWidgets.QLineEdit(self.manager_add)
                self.name1.setGeometry(QtCore.QRect(400, 460, 171, 31))
                self.name1.setText("")
                self.name1.setObjectName("name1")
                self.mima1 = QtWidgets.QLineEdit(self.manager_add)
                self.mima1.setGeometry(QtCore.QRect(400, 500, 171, 31))
                self.mima1.setText("")
                self.mima1.setObjectName("mima1")
                self.ID2 = QtWidgets.QLineEdit(self.manager_add)
                self.ID2.setGeometry(QtCore.QRect(770, 420, 171, 31))
                self.ID2.setText("")
                self.ID2.setObjectName("ID2")
                self.name2 = QtWidgets.QLineEdit(self.manager_add)
                self.name2.setGeometry(QtCore.QRect(770, 460, 171, 31))
                self.name2.setText("")
                self.name2.setObjectName("name2")
                self.mima2 = QtWidgets.QLineEdit(self.manager_add)
                self.mima2.setGeometry(QtCore.QRect(770, 500, 171, 31))
                self.mima2.setText("")
                self.mima2.setObjectName("mima2")
                self.shanchugly = QtWidgets.QPushButton(self.manager_add)
                self.shanchugly.setGeometry(QtCore.QRect(580, 540, 81, 61))
                self.shanchugly.setObjectName("shanchugly")
                self.tabWidget.addTab(self.manager_add, "")
                self.dljl = QtWidgets.QWidget()
                self.dljl.setObjectName("dljl")
                self.denglulishi = QtWidgets.QTableWidget(self.dljl)
                self.denglulishi.setGeometry(QtCore.QRect(70, 50, 371, 411))
                self.denglulishi.setObjectName("denglulishi")
                self.denglulishi.setColumnCount(3)
                self.denglulishi.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.denglulishi.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.denglulishi.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.denglulishi.setHorizontalHeaderItem(2, item)
                self.qbcxlishi = QtWidgets.QPushButton(self.dljl)
                self.qbcxlishi.setGeometry(QtCore.QRect(170, 520, 141, 41))
                self.qbcxlishi.setObjectName("qbcxlishi")
                self.riqi = QtWidgets.QLineEdit(self.dljl)
                self.riqi.setGeometry(QtCore.QRect(570, 170, 191, 31))
                self.riqi.setObjectName("riqi")
                self.drriqi = QtWidgets.QPushButton(self.dljl)
                self.drriqi.setGeometry(QtCore.QRect(760, 170, 111, 31))
                self.drriqi.setObjectName("drriqi")
                self.dezheID = QtWidgets.QLineEdit(self.dljl)
                self.dezheID.setGeometry(QtCore.QRect(570, 380, 191, 31))
                self.dezheID.setObjectName("dezheID")
                self.dz = QtWidgets.QPushButton(self.dljl)
                self.dz.setGeometry(QtCore.QRect(760, 380, 111, 31))
                self.dz.setObjectName("dz")
                self.tabWidget.addTab(self.dljl, "")
                self.listWidget = QtWidgets.QListWidget(bookadmin)
                self.listWidget.setGeometry(QtCore.QRect(-10, -10, 1151, 741))
                self.listWidget.setStyleSheet("border-image: url(:/书2.jpg);")
                self.listWidget.setObjectName("listWidget")
                self.listWidget.raise_()
                self.tabWidget.raise_()

                self.retranslateUi(bookadmin)
                self.tabWidget.setCurrentIndex(6)
                QtCore.QMetaObject.connectSlotsByName(bookadmin)
                ########################################################################
                # 书籍模块
                self.jilu.clicked.connect(self.single_select)
                self.cxqb1.clicked.connect(self.show_all_books)
                self.tainjia1.clicked.connect(self.add_book)
                self.shanchu1.clicked.connect(self.drop_book)
                self.xiugai1.clicked.connect(self.update_book)
                # 学生模块
                self.jilu2.clicked.connect(self.user_select)  ###已解决
                self.cxqb2.clicked.connect(self.show_all_students)
                self.shanchu2.clicked.connect(self.user_drop)
                self.tainjia2.clicked.connect(self.add_user)
                self.xb.activated.connect(self.auto)
                self.xiugai2.clicked.connect(self.update_user)
                ###批准模块
                self.sx.clicked.connect(self.show_all_borrow)
                self.pz.clicked.connect(self.pizhun)
                self.bh.clicked.connect(self.bohui)
                ###导入书籍模块
                self.cxqb3.clicked.connect(self.select_all_books)
                self.mulu1.clicked.connect(self.open_file_dialog)
                self.qd.clicked.connect(self.get_bookinfo)
                ###导入读者模块
                self.cxqb4.clicked.connect(self.select_all_students)
                self.mulu3.clicked.connect(self.open_file_dialog1)
                self.qd_2.clicked.connect(self.get_readers_info)
                ###管理员管理页面
                self.chaxunall.clicked.connect(self.show_regestor)
                self.jujue.clicked.connect(self.refuse_add)
                self.tongyi.clicked.connect(self.accept_add)
                self.select_all.clicked.connect(self.show_all_managers)
                self.tjzhuce.clicked.connect(self.add_admin)
                self.single_choose.clicked.connect(self.select_single_admin)
                self.update_password.clicked.connect(self.update_admin_password)
                self.shanchugly.clicked.connect(self.delete_admin)
                ###登录记录界面
                self.qbcxlishi.clicked.connect(self.show_all_login)
                self.drriqi.clicked.connect(self.choose_date_select)
                self.dz.clicked.connect(self.reader_record)
        ########################################################################
        def retranslateUi(self, Form3):
                _translate = QtCore.QCoreApplication.translate
                Form3.setWindowTitle(_translate("Form3", "Form"))
                item = self.shujibiao.horizontalHeaderItem(0)
                item.setText(_translate("Form3", "ISBN号"))
                item = self.shujibiao.horizontalHeaderItem(1)
                item.setText(_translate("Form3", "书名"))
                item = self.shujibiao.horizontalHeaderItem(2)
                item.setText(_translate("Form3", "作者"))
                item = self.shujibiao.horizontalHeaderItem(3)
                item.setText(_translate("Form3", "出版社"))
                item = self.shujibiao.horizontalHeaderItem(4)
                item.setText(_translate("Form3", "被借次数"))
                item = self.shujibiao.horizontalHeaderItem(5)
                item.setText(_translate("Form3", "馆藏册数"))
                item = self.shujibiao.horizontalHeaderItem(6)
                item.setText(_translate("Form3", "在馆册数"))
                item = self.shujibiao.horizontalHeaderItem(7)
                item.setText(_translate("Form3", "书架号"))
                item = self.shujibiao.horizontalHeaderItem(8)
                item.setText(_translate("Form3", "书籍类别"))
                self.sm.setPlaceholderText(_translate("Form3", "书名："))
                self.sh.setPlaceholderText(_translate("Form3", "ISBN号："))
                self.zz.setPlaceholderText(_translate("Form3", "作者："))
                self.cb.setPlaceholderText(_translate("Form3", "出版社："))
                self.bj.setPlaceholderText(_translate("Form3", "被借次数："))
                self.jc.setPlaceholderText(_translate("Form3", "馆藏册数："))
                self.gc.setPlaceholderText(_translate("Form3", "在馆册数："))
                self.shujihao.setPlaceholderText(_translate("Form3", "书架号："))
                self.lineEdit.setPlaceholderText(_translate("Form3", "书籍类别："))
                self.tainjia1.setText(_translate("Form3", "添加"))
                self.xiugai1.setText(_translate("Form3", "修改"))
                self.shanchu1.setText(_translate("Form3", "删除"))
                self.jilu.setText(_translate("Form3", "查询"))
                self.cxqb1.setText(_translate("Form3", "查询全部"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.shuji), _translate("Form3", "书籍信息"))
                item = self.tableWidget.horizontalHeaderItem(0)
                item.setText(_translate("Form3", "ID号"))
                item = self.tableWidget.horizontalHeaderItem(1)
                item.setText(_translate("Form3", "姓名"))
                item = self.tableWidget.horizontalHeaderItem(2)
                item.setText(_translate("Form3", "学院"))
                item = self.tableWidget.horizontalHeaderItem(3)
                item.setText(_translate("Form3", "性别"))
                item = self.tableWidget.horizontalHeaderItem(4)
                item.setText(_translate("Form3", "读者类型"))
                item = self.tableWidget.horizontalHeaderItem(5)
                item.setText(_translate("Form3", "电话"))
                item = self.tableWidget.horizontalHeaderItem(6)
                item.setText(_translate("Form3", "可借次数"))
                item = self.tableWidget.horizontalHeaderItem(7)
                item.setText(_translate("Form3", "信用级别"))
                item = self.tableWidget.horizontalHeaderItem(8)
                item.setText(_translate("Form3", "密码"))
                self.sh_2.setPlaceholderText(_translate("Form3", "ID号："))
                self.sm_2.setPlaceholderText(_translate("Form3", "姓名："))
                self.zz_2.setPlaceholderText(_translate("Form3", "学院："))
                self.xb_2.setItemText(0, _translate("Form3", "男"))
                self.xb_2.setItemText(1, _translate("Form3", "女"))
                self.xb.setCurrentText(_translate("Form3", "本科生"))
                self.xb.setItemText(0, _translate("Form3", "本科生"))
                self.xb.setItemText(1, _translate("Form3", "研究生"))
                self.xb.setItemText(2, _translate("Form3", "教师"))
                self.dh.setPlaceholderText(_translate("Form3", "电话："))
                self.kj.setPlaceholderText(_translate("Form3", "可借次数："))
                self.xy.setPlaceholderText(_translate("Form3", "信用级别："))
                self.mm.setPlaceholderText(_translate("Form3", "密码："))
                self.tainjia2.setText(_translate("Form3", "添加"))
                self.xiugai2.setText(_translate("Form3", "修改"))
                self.shanchu2.setText(_translate("Form3", "删除"))
                self.jilu2.setText(_translate("Form3", "查询"))
                self.cxqb2.setText(_translate("Form3", "查询全部"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.xuesheng), _translate("Form3", "读者信息"))
                item = self.jieyuebiao.horizontalHeaderItem(0)
                item.setText(_translate("Form3", "ISBN号"))
                item = self.jieyuebiao.horizontalHeaderItem(1)
                item.setText(_translate("Form3", "读者ID"))
                item = self.jieyuebiao.horizontalHeaderItem(2)
                item.setText(_translate("Form3", "借书时间"))
                item = self.jieyuebiao.horizontalHeaderItem(3)
                item.setText(_translate("Form3", "还书时间"))
                item = self.jieyuebiao.horizontalHeaderItem(4)
                item.setText(_translate("Form3", "审批类型"))
                self.pz.setText(_translate("Form3", "批准"))
                self.bh.setText(_translate("Form3", "驳回"))
                self.sx.setText(_translate("Form3", "刷新"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.jieyue), _translate("Form3", "借还书审批"))
                item = self.shujibiao_2.horizontalHeaderItem(0)
                item.setText(_translate("Form3", "ISBN号"))
                item = self.shujibiao_2.horizontalHeaderItem(1)
                item.setText(_translate("Form3", "书名"))
                item = self.shujibiao_2.horizontalHeaderItem(2)
                item.setText(_translate("Form3", "作者"))
                item = self.shujibiao_2.horizontalHeaderItem(3)
                item.setText(_translate("Form3", "出版社"))
                item = self.shujibiao_2.horizontalHeaderItem(4)
                item.setText(_translate("Form3", "被借次数"))
                item = self.shujibiao_2.horizontalHeaderItem(5)
                item.setText(_translate("Form3", "馆藏册数"))
                item = self.shujibiao_2.horizontalHeaderItem(6)
                item.setText(_translate("Form3", "在馆册数"))
                item = self.shujibiao_2.horizontalHeaderItem(7)
                item.setText(_translate("Form3", "书架号"))
                item = self.shujibiao_2.horizontalHeaderItem(8)
                item.setText(_translate("Form3", "书籍类别"))
                self.cxqb3.setText(_translate("Form3", "查询全部"))
                self.mulu1.setText(_translate("Form3", "..."))
                self.qd.setText(_translate("Form3", "确定"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.drsj), _translate("Form3", "导入书籍信息"))
                item = self.tableWidget_2.horizontalHeaderItem(0)
                item.setText(_translate("Form3", "ID号"))
                item = self.tableWidget_2.horizontalHeaderItem(1)
                item.setText(_translate("Form3", "姓名"))
                item = self.tableWidget_2.horizontalHeaderItem(2)
                item.setText(_translate("Form3", "学院"))
                item = self.tableWidget_2.horizontalHeaderItem(3)
                item.setText(_translate("Form3", "性别"))
                item = self.tableWidget_2.horizontalHeaderItem(4)
                item.setText(_translate("Form3", "读者类型"))
                item = self.tableWidget_2.horizontalHeaderItem(5)
                item.setText(_translate("Form3", "电话"))
                item = self.tableWidget_2.horizontalHeaderItem(6)
                item.setText(_translate("Form3", "可借次数"))
                item = self.tableWidget_2.horizontalHeaderItem(7)
                item.setText(_translate("Form3", "信用级别"))
                item = self.tableWidget_2.horizontalHeaderItem(8)
                item.setText(_translate("Form3", "密码"))
                self.mulu3.setText(_translate("Form3", "..."))
                self.qd_2.setText(_translate("Form3", "确定"))
                self.cxqb4.setText(_translate("Form3", "查询全部"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.drxs), _translate("Form3", "导入学生信息"))
                self.tongyi.setText(_translate("Form3", "审批同意"))
                self.jujue.setText(_translate("Form3", "拒绝注册"))
                item = self.glypizhun.horizontalHeaderItem(0)
                item.setText(_translate("Form3", "ID"))
                item = self.glypizhun.horizontalHeaderItem(1)
                item.setText(_translate("Form3", "姓名"))
                item = self.glyzhuce.horizontalHeaderItem(0)
                item.setText(_translate("Form3", "ID"))
                item = self.glyzhuce.horizontalHeaderItem(1)
                item.setText(_translate("Form3", "姓名"))
                self.select_all.setText(_translate("Form3", "全部查询"))
                self.tjzhuce.setText(_translate("Form3", "添加注册"))
                item = self.all.horizontalHeaderItem(0)
                item.setText(_translate("Form3", "ID"))
                item = self.all.horizontalHeaderItem(1)
                item.setText(_translate("Form3", "姓名"))
                item = self.all.horizontalHeaderItem(2)
                item.setText(_translate("Form3", "password"))
                self.single_choose.setText(_translate("Form3", "个人查询"))
                self.update_password.setText(_translate("Form3", "修改密码"))
                self.chaxunall.setText(_translate("Form3", "全部查询"))
                self.id.setPlaceholderText(_translate("Form3", "ID："))
                self.name1.setPlaceholderText(_translate("Form3", "姓名"))
                self.mima1.setPlaceholderText(_translate("Form3", "密码："))
                self.ID2.setPlaceholderText(_translate("Form3", "ID："))
                self.name2.setPlaceholderText(_translate("Form3", "姓名"))
                self.mima2.setPlaceholderText(_translate("Form3", "密码："))
                self.shanchugly.setText(_translate("Form3", "删除管理员"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.manager_add), _translate("Form3", "管理员添加与注册审批"))
                item = self.denglulishi.horizontalHeaderItem(0)
                item.setText(_translate("Form3", "读者ID"))
                item = self.denglulishi.horizontalHeaderItem(1)
                item.setText(_translate("Form3", "登录日期"))
                item = self.denglulishi.horizontalHeaderItem(2)
                item.setText(_translate("Form3", "当日登录次数"))
                self.qbcxlishi.setText(_translate("Form3", "全部历史查询"))
                self.riqi.setPlaceholderText(_translate("Form3", "输入查询日期：年-月-日"))
                self.drriqi.setText(_translate("Form3", "当日查询"))
                self.dezheID.setPlaceholderText(_translate("Form3", "请输入读者ID："))
                self.dz.setText(_translate("Form3", "读者登录查询"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.dljl), _translate("Form3", "读者登录记录查看"))
        ##############################书籍##############################################
        def show_all_books(self):
                sql = 'select * from books'
                res = cursor.execute(sql)
                bookinfo = cursor.fetchall()
                self.shujibiao.setRowCount(res)
                for i in range(res):
                        book = bookinfo[i]
                        isbn = QTableWidgetItem(book[0])
                        bookname = QTableWidgetItem(book[1])
                        author = QTableWidgetItem(book[2])
                        publish = QTableWidgetItem(book[4])
                        beijie = QTableWidgetItem(str(book[5]))
                        totalnum = QTableWidgetItem(str(book[6]))
                        zaiguan = QTableWidgetItem(str(book[7]))
                        bookshelf = QTableWidgetItem(book[8])
                        classfy = QTableWidgetItem(book[3])
                        self.shujibiao.setItem(i, 0, isbn)
                        self.shujibiao.setItem(i, 1, bookname)
                        self.shujibiao.setItem(i, 2, author)
                        self.shujibiao.setItem(i, 3, publish)
                        self.shujibiao.setItem(i, 4, beijie)
                        self.shujibiao.setItem(i, 5, totalnum)
                        self.shujibiao.setItem(i, 6, zaiguan)
                        self.shujibiao.setItem(i, 7, bookshelf)
                        self.shujibiao.setItem(i, 8, classfy)

        def add_book(self):
                bookid = self.sh.text()
                bookname = self.sm.text()
                author = self.zz.text()
                bookpublisher = self.cb.text()
                beijiecishu = self.bj.text()
                bookshelf = self.shujihao.text()
                bookleibie = self.lineEdit.text()

                try:
                        totalnum = int(self.gc.text())
                        zaiguan = int(self.jc.text())
                        if totalnum > 0 and zaiguan > 0:  # 主要在馆册数>0才能录入
                                if (bookid and bookname and author and bookpublisher and totalnum and
                                        beijiecishu and zaiguan and bookshelf):
                                        value = (bookid, bookname, author, bookpublisher,bookleibie,
                                                 int(beijiecishu),int(totalnum),int(zaiguan), bookshelf)
                                        sql = ('insert into books(ISBN号,书名,作者,出版社,书籍类别,被借次数,馆藏册数,在馆册数,书架号) '
                                               'values(%s,%s,%s,%s,%s,%s,%s,%s,%s)')
                                        cursor.execute(sql, value)
                                        conn.commit()
                                        QMessageBox.warning(self, "提示", "插入成功！", QMessageBox.Yes)
                                        self.show_all_books()
                                else:
                                        QMessageBox.warning(self, "警告", "书目信息有误！", QMessageBox.Yes)
                        else:
                                QMessageBox.warning(self, "警告", "书目信息有误！", QMessageBox.Yes)
                except ValueError:
                        QMessageBox.warning(self, "警告", "馆藏册数和在馆册数必须是正整数！", QMessageBox.Yes)

        def drop_book(self):
                se = self.shujibiao.currentRow()#通过获取第几行（从0开始）
                bookid = self.shujibiao.item(se,0).text()
                sql = 'delete from books where ISBN号="%s"' % (bookid)
                cursor.execute(sql)
                conn.commit()
                QMessageBox.warning(self, "提示", "删除成功！", QMessageBox.Yes)
                self.show_all_books()

        def single_select(self):
                bookid = self.sh.text()
                bookname = self.sm.text()
                author = self.zz.text()
                publisher = self.cb.text()
                booktype = self.lineEdit.text()
                borrowtimes = self.bj.text()
                totalnum = self.gc.text()
                zaiguan = self.jc.text()
                bookshelf = self.shujihao.text()
                sql = ('select * from books where ISBN号=%s or 书名=%s or 作者=%s or '
                       '出版社=%s or 书架号=%s or 书籍类别=%s')
                res = cursor.execute(sql,(bookid,bookname,author,publisher,bookshelf,booktype))
                bookinfo = cursor.fetchall()
                n = len(bookinfo)
                self.shujibiao.setRowCount(n)
                for i in range(n):
                        book = bookinfo[i]
                        bookid2 = QTableWidgetItem(book[0])
                        bookname2 = QTableWidgetItem(book[1])
                        author2 = QTableWidgetItem(book[2])
                        bookpublisher2 = QTableWidgetItem(book[4])
                        beijiecishu2 = QTableWidgetItem(str(book[5]))
                        totalnum2 = QTableWidgetItem(str(book[6]))
                        zaiguan2 = QTableWidgetItem(str(book[7]))
                        bookshelf2 = QTableWidgetItem(book[8])
                        booktype2 = QTableWidgetItem(book[3])

                        self.shujibiao.setItem(i,0,bookid2)
                        self.shujibiao.setItem(i,1,bookname2)
                        self.shujibiao.setItem(i,2,author2)
                        self.shujibiao.setItem(i,3,bookpublisher2)
                        self.shujibiao.setItem(i,4,beijiecishu2)
                        self.shujibiao.setItem(i,5,totalnum2)
                        self.shujibiao.setItem(i,6,zaiguan2)
                        self.shujibiao.setItem(i,7,bookshelf2)
                        self.shujibiao.setItem(i, 8, booktype2)
        #更新书籍信息
        def update_book(self):
                bookid = self.sh.text()
                bookname = self.sm.text()
                author = self.zz.text()
                bookpublisher = self.cb.text()
                beijiecishu = self.bj.text()
                bookshelf = self.shujihao.text()
                booktype = self.lineEdit.text()
                try:
                        totalnum = int(self.gc.text())
                        zaiguan = int(self.jc.text())
                        if totalnum >= 0 and zaiguan >= 0:  # 主要在馆册数>0才能更新
                                if bookid and bookname and author and bookpublisher and bookshelf and booktype:
                                        text = (bookid, bookname,author, bookpublisher, bookshelf,booktype, bookid)
                                        sql = ('UPDATE books SET ISBN号=%s,书名=%s,作者=%s,出版社=%s,书架号=%s,书籍类别=%s '
                                               'WHERE ISBN号=%s')
                                        cursor.execute(sql, text)
                                        conn.commit()
                                        QMessageBox.warning(self, "提示", "修改成功！", QMessageBox.Yes)
                                        self.show_all_books()
                                else:
                                        QMessageBox.warning(self, "警告", "书目信息有误！", QMessageBox.Yes)
                        else:
                                QMessageBox.warning(self, "警告", "书目信息有误！", QMessageBox.Yes)
                except ValueError:
                        QMessageBox.warning(self, "警告", "馆藏册数和在馆册数必须是正整数！", QMessageBox.Yes)

        ##################################读者信息查询修改界面##########################

        def show_all_students(self):
                sql1 = 'select * from reader'
                res = cursor.execute(sql1)
                readerinfoma = cursor.fetchall()#以嵌套元组的形式获取表中元组
                self.tableWidget.setRowCount(res)
                for i in range(res):
                        reader = readerinfoma[i]
                        readerid = QTableWidgetItem(reader[0])
                        readername = QTableWidgetItem(reader[1])
                        readercollege = QTableWidgetItem(reader[2])
                        readersex = QTableWidgetItem(reader[3])
                        readertype = QTableWidgetItem(reader[4])
                        readerphone = QTableWidgetItem(str(reader[5]))
                        eborrowtimes = QTableWidgetItem(str(reader[6]))
                        creditlevel = QTableWidgetItem(str(reader[7]))
                        password = QTableWidgetItem(reader[8])

                        self.tableWidget.setItem(i,0, readerid)
                        self.tableWidget.setItem(i, 1, readername)
                        self.tableWidget.setItem(i, 2, readercollege)
                        self.tableWidget.setItem(i, 3, readersex)
                        self.tableWidget.setItem(i, 4, readertype)
                        self.tableWidget.setItem(i, 5, readerphone)
                        self.tableWidget.setItem(i, 6, eborrowtimes)
                        self.tableWidget.setItem(i, 7, creditlevel)
                        self.tableWidget.setItem(i, 8, password)


        #单个读者信息查询
        def user_select(self):
                username = self.sm_2.text()
                userid = self.sh_2.text()
                usercollege = self.zz_2.text()
                usergender = self.xb_2.currentText()
                userlevel = self.xb.currentText()
                userphone = self.dh.text()
                userkejie = self.kj.text()
                usercredit = self.xy.text()
                password = self.mm.text()
                # print(username)
                if userid:
                        sql = 'select * from reader where ID号 =%s'#-- or 姓名=%s or 性别 =%s or 单位 = %s or 读者类型=%s
                        cursor.execute(sql, (userid))#, username, usergender, usercollege, userlevel
                if username:
                        sql0 = 'select * from reader where 姓名=%s'
                        cursor.execute(sql0,username)
                userinfo = cursor.fetchall()
                n = len(userinfo)
                self.tableWidget.setRowCount(n)
                for i in range(n):
                        user = userinfo[i]
                        ID = QTableWidgetItem(user[0])
                        name = QTableWidgetItem(user[1])
                        gender = QTableWidgetItem(user[3])
                        college = QTableWidgetItem(user[2])
                        level = QTableWidgetItem(user[4])
                        phone = QTableWidgetItem(user[5])
                        kejie = QTableWidgetItem(str(user[6]))
                        secret = QTableWidgetItem(user[8])
                        credit = QTableWidgetItem(str(user[7]))

                        self.tableWidget.setItem(i,0,ID)
                        self.tableWidget.setItem(i,1,name)
                        self.tableWidget.setItem(i,2,college)
                        self.tableWidget.setItem(i,3,gender)
                        self.tableWidget.setItem(i,4,level)
                        self.tableWidget.setItem(i,5,phone)
                        self.tableWidget.setItem(i,6,kejie)
                        self.tableWidget.setItem(i,7,credit)
                        self.tableWidget.setItem(i,8,secret)
                # print(111)
        #删除读者
        def user_drop(self):
                se = self.tableWidget.currentRow()  # 通过获取第几行（从0开始）
                userid = self.tableWidget.item(se, 0).text()
                sql = 'delete from reader where ID号="%s"' % (userid)
                cursor.execute(sql)
                conn.commit()
                QMessageBox.warning(self, "提示", "删除成功！", QMessageBox.Yes)
                self.show_all_students()

        def add_user(self):
                readername = self.sm_2.text()
                readerid = self.sh_2.text()
                readercollege = self.zz_2.text()
                readergender = self.xb_2.currentText()
                readerlevel = self.xb.currentText()
                phonenum = self.dh.text()
                kejie = int(self.kj.text())
                credeit = int(self.xy.text())
                password = self.mm.text()
                sql = 'SELECT * FROM reader WHERE ID号="%s"' % readerid
                res = cursor.execute(sql)
                if res:
                        QMessageBox.warning(self, "警告", "该读者ID已被占用！", QMessageBox.Yes)
                else:
                        text = (readerid,readername,readercollege,readergender,
                                readerlevel,phonenum,kejie,credeit,password)
                        sql1 = ('INSERT INTO reader(ID号,姓名,学院,性别,读者类型,电话,可借册数,信用级别,password) '
                                'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)')
                        cursor.execute(sql1, text)
                        conn.commit()
                        self.show_all_students()
                        QMessageBox.warning(self, "提示", "添加成功！", QMessageBox.Yes)
        #           self.getreadersinfo()
        ##自动划分等级，来给定借书量
        def auto(self):
                if self.xb.currentText()=='本科生':
                        self.kj.setText('20')
                elif self.xb.currentText()=='研究生':
                        self.kj.setText('25')
                elif self.xb.currentText()=='教师':
                        self.kj.setText('30')

        #更新读者信息
        def update_user(self):
                rname = self.sm_2.text()
                rid = self.sh_2.text()
                rcollege = self.zz_2.text()
                rgender = self.xb_2.currentText()
                rlevel = self.xb.currentText()
                rphone = self.dh.text()
                rpass = self.mm.text()

                try:
                        rkejie = int(self.kj.text())
                        rcredit = int(self.xy.text())
                        if (rname and rid and rcollege and rgender and rlevel and rphone
                                and rkejie and rcredit and rpass):
                                text = (rid, rname, rgender,rphone, rcollege, rlevel, rpass, rid)
                                sql = ('update reader set ID号 = %s, 姓名 = %s, 性别 = %s, 电话=%s, '
                                       '学院=%s, 读者类型=%s, password=%s where ID号 = %s')
                                cursor.execute(sql, text)
                                conn.commit()
                                QMessageBox.warning(self, "提示", "修改成功！", QMessageBox.Yes)
                                self.show_all_students()
                        else:
                                QMessageBox.warning(self, "警告", "读者信息不完整！", QMessageBox.Yes)
                except ValueError:
                        QMessageBox.warning(self, "警告", "可借册数和信誉必须是正整数！", QMessageBox.Yes)

        #################################借书批准模块###########################################
        def show_all_borrow(self):
                sql = 'SELECT * FROM items'
                res = cursor.execute(sql)
                items = cursor.fetchall()
                self.jieyuebiao.setRowCount(res)
                for i in range(res):
                        item = items[i]
                        borrow1 = QTableWidgetItem(item[0])
                        borrow2 = QTableWidgetItem(item[1])
                        borrow3 = QTableWidgetItem(str(item[2]))
                        borrow4 = QTableWidgetItem(str(item[3]))
                        borrow5 = QTableWidgetItem(item[4])
                        self.jieyuebiao.setItem(i, 0, borrow1)
                        self.jieyuebiao.setItem(i, 1, borrow2)
                        self.jieyuebiao.setItem(i, 2, borrow3)
                        self.jieyuebiao.setItem(i, 3, borrow4)
                        self.jieyuebiao.setItem(i, 4, borrow5)

        def pizhun(self):
                s = self.jieyuebiao.currentRow()  # 通过获取第几行（从0开始）
                bookid = self.jieyuebiao.item(s, 0).text()
                readerid = self.jieyuebiao.item(s, 1).text()
                itemtime = str(self.jieyuebiao.item(s, 2).text())###借书时间
                returntime = str(self.jieyuebiao.item(s, 3).text())  ###表要加一列归还时间
                selecttype = self.jieyuebiao.item(s, 4).text()


                if selecttype == 'borrow':
                        # 从items中取出并放入borrow_record中
                        sql1 = 'delete from items where ISBN=%s and ID=%s and 借书时间=%s and 还书时间=%s'
                        cursor.execute(sql1, (bookid,readerid,itemtime,returntime))
                        conn.commit()
                        sql_check = 'select * from borrow_record where ISBN=%s and 读者ID=%s'
                        res = cursor.execute(sql_check,(bookid,readerid))
                        if res: #########续借处理
                                sql01 = 'update borrow_record set 借书时间=%s, 归还日期=%s where ISBN=%s and 读者ID=%s'
                                cursor.execute(sql01,(itemtime,returntime,bookid,readerid))
                                conn.commit()
                                #被借次数+1
                                sql04 = 'update books set 被借次数=被借次数+1 where ISBN号=%s'
                                cursor.execute(sql04, bookid)
                                conn.commit()
                        else:
                                sql2 = 'insert into borrow_record(ISBN,读者ID,借书时间,归还日期) values (%s,%s,%s,%s)'
                                cursor.execute(sql2, ( bookid,readerid, itemtime, returntime))
                                conn.commit()
                                # reader里面的在借册数加一，可借册数减一
                                sql3 = 'update reader set 可借册数=可借册数-1 where ID号=%s'
                                cursor.execute(sql3, readerid)
                                conn.commit()
                                # 图书被借次数数加一
                                sql4 = 'update books set 被借次数=被借次数+1,在馆册数=在馆册数-1 where ISBN号=%s'
                                cursor.execute(sql4, bookid)
                                conn.commit()
                else:       #还书
                        sql = 'select * from borrow_record where 读者ID=%s and ISBN=%s'
                        cursor.execute(sql,(readerid, bookid))
                        result = cursor.fetchall()
                        if result:
                                record = result[0]  ####无意义
                                borrowtime = str(record[2])  ###找出借书时间
                                rettime = str(record[3])  # 归还日期
                        borrowtime=itemtime
                        rettime = returntime

                        ######方便版本:获取给出的还书时间与借书时间相差的天数，计算 borrowtime 和 rettime 这两个日期之间相差的天数
                        borrowtime = time.strptime(borrowtime, "%Y-%m-%d")
                        rettime = time.strptime(rettime,"%Y-%m-%d")
                        time_array1 = int(time.mktime(borrowtime))
                        time_array2 = int(time.mktime(rettime))
                        result = (time_array2 - time_array1) // 60 // 60 // 24
                        print(result)
                        # # 获取当前时间与借书时间相差的天数，计算 borrowtime 和 itemtime 这两个日期之间相差的天数
                        # borrowtime = time.strptime(borrowtime, "%Y-%m-%d")
                        # time_array1 = int(time.mktime(borrowtime))
                        # itemtime = time.strptime(itemtime, "%Y-%m-%d")
                        # time_array2 = int(time.mktime(itemtime))
                        # result = (time_array2 - time_array1) // 60 // 60 // 24
                        # 读出该身份人员可借时间
                        sql7 = 'select * from reader where ID号=%s' % (readerid)
                        cursor.execute(sql7)
                        item = cursor.fetchall()
                        item = item[0]  ###########规定不同级别借书时间不同
                        if item[4] == '研究生':
                                readertime = 60
                        elif item[4] == '本科生':
                                readertime = 30
                        elif item[4] == '教师':
                                readertime = 90
                        time_to_cal = result - readertime
                        # 判断是否超期
                        if time_to_cal <= 0:
                                QMessageBox.warning(self, "谢谢惠顾", "还书成功！", QMessageBox.Yes)
                        else:
                                sql8 = 'update reader set 信用级别=信用级别-1 where ID号=%s' % (readerid)
                                cursor.execute(sql8)
                                conn.commit()
                                QMessageBox.warning(self, "注意", "该读者已逾期，信用级别降低！", QMessageBox.Yes)
                        sql5 = 'delete from borrow_record where ISBN="%s"' % (bookid)
                        cursor.execute(sql5)
                        conn.commit()
                        sql6 = 'delete from items where ISBN=%s' % (bookid)
                        cursor.execute(sql6)
                        conn.commit()
                        sql9 = 'update reader set 可借册数=可借册数+1 where ID号=%s'
                        cursor.execute(sql9,readerid)
                        conn.commit()
                        sql10 = 'update books set 在馆册数=在馆册数+1 where ISBN号=%s'
                        cursor.execute(sql10,(bookid))
                        conn.commit()
                self.show_all_borrow()

        def bohui(self):
                s=self.jieyuebiao.currentRow()#通过获取第几行（从0开始）
                bookid = self.jieyuebiao.item(s, 0).text()
                readerid = self.jieyuebiao.item(s, 1).text()
                itemtime = str(self.jieyuebiao.item(s, 2).text())  ###借书时间
                returntime = str(self.jieyuebiao.item(s, 3).text())  ###表要加一列归还时间
                sql1 = 'delete from items where ISBN=%s and ID=%s and 借书时间=%s and 还书时间=%s'
                cursor.execute(sql1, (bookid, readerid, itemtime, returntime))
                conn.commit()
                self.show_all_borrow()
        #######################################导入图书界面#############################
        def select_all_books(self):
                sql = 'select * from books'
                res = cursor.execute(sql)
                bookinfo = cursor.fetchall()
                self.shujibiao_2.setRowCount(res)
                for i in range(res):
                        book = bookinfo[i]
                        isbn = QTableWidgetItem(book[0])
                        bookname = QTableWidgetItem(book[1])
                        author = QTableWidgetItem(book[2])
                        publisher = QTableWidgetItem(book[4])
                        beijie = QTableWidgetItem(str(book[5]))
                        totalnum = QTableWidgetItem(str(book[6]))
                        zaiguan = QTableWidgetItem(str(book[7]))
                        bookshelf = QTableWidgetItem(book[8])
                        classfy = QTableWidgetItem(book[3])

                        self.shujibiao_2.setItem(i,0,isbn)
                        self.shujibiao_2.setItem(i,1,bookname)
                        self.shujibiao_2.setItem(i,2,author)
                        self.shujibiao_2.setItem(i,3,publisher)
                        self.shujibiao_2.setItem(i,4,beijie)
                        self.shujibiao_2.setItem(i,5,totalnum)
                        self.shujibiao_2.setItem(i,6,zaiguan)
                        self.shujibiao_2.setItem(i,7,bookshelf)
                        self.shujibiao_2.setItem(i, 8, classfy)
        def open_file_dialog(self):
                file_name, _ = QFileDialog.getOpenFileName(self, "Select File")
                if file_name:
                        self.mulu2.setText(file_name)
        #导入书籍信息
        def get_bookinfo(self):
                file_path = self.mulu2.text()
                book_items = [None] * 9
                tables = pd.read_excel(file_path)
                row_num = len(tables)
                rt = 0
                for index,row in tables.iterrows():
                        i = 0
                        for element in row:
                                book_items[i] = element
                                i = i+1
                        sql1 = ('insert into books(ISBN号,书名,作者,书籍类别,出版社,被借次数,馆藏册数,在馆册数,书架号) '
                                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s)')
                        cursor.execute(sql1,(book_items[0],book_items[1],book_items[2],book_items[3],
                                             book_items[4],book_items[5],book_items[6],book_items[7],book_items[8]))
                        rt = rt+1
                conn.commit()
                if rt==row_num:
                        QMessageBox.warning(self, "提示", "导入成功！", QMessageBox.Yes)
                else:
                        QMessageBox.warning(self, "警告", "导入有缺失！", QMessageBox.Yes)
                self.select_all_books()
        ####################################导入学生信息#######################
        def select_all_students(self):
                sql = 'select * from reader'
                res = cursor.execute(sql)
                readerinfoma = cursor.fetchall()  # 以嵌套元组的形式获取表中元组
                self.tableWidget_2.setRowCount(res)
                for i in range(res):
                        reader = readerinfoma[i]
                        readerid = QTableWidgetItem(reader[0])
                        readername = QTableWidgetItem(reader[1])
                        readercollege = QTableWidgetItem(reader[2])
                        readersex = QTableWidgetItem(reader[3])
                        readertype = QTableWidgetItem(reader[4])
                        readerphone = QTableWidgetItem(str(reader[5]))
                        eborrowtimes = QTableWidgetItem(str(reader[6]))
                        creditlevel = QTableWidgetItem(str(reader[7]))
                        password = QTableWidgetItem(reader[8])

                        self.tableWidget_2.setItem(i, 0, readerid)
                        self.tableWidget_2.setItem(i, 1, readername)
                        self.tableWidget_2.setItem(i, 2, readercollege)
                        self.tableWidget_2.setItem(i, 3, readersex)
                        self.tableWidget_2.setItem(i, 4, readertype)
                        self.tableWidget_2.setItem(i, 5, readerphone)
                        self.tableWidget_2.setItem(i, 6, eborrowtimes)
                        self.tableWidget_2.setItem(i, 7, creditlevel)
                        self.tableWidget_2.setItem(i, 8, password)
        def open_file_dialog1(self):
                file_name, _ = QFileDialog.getOpenFileName(self, "Select File")
                if file_name:
                        self.mulu4.setText(file_name)
        def get_readers_info(self):
                file_path = self.mulu4.text()
                reader_items = [None]*9
                tables = pd.read_excel(file_path)
                row_num = len(tables)
                cnt = 0
                for index,row in tables.iterrows():
                        i = 0
                        for elememt in row:
                                reader_items[i] = elememt
                                i = i+1
                        sql = ('INSERT INTO reader(ID号,姓名,学院,性别,读者类型,电话,可借册数,信用级别,password) '
                               'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)')
                        cursor.execute(sql,(reader_items[0],reader_items[1],reader_items[2],reader_items[3],
                                            reader_items[4],reader_items[5],reader_items[6],reader_items[7],reader_items[8]))
                        cnt = cnt+1
                conn.commit()
                if cnt == row_num:
                        QMessageBox.warning(self, "提示", "导入成功！", QMessageBox.Yes)
                else:
                        QMessageBox.warning(self, "警告", "导入有缺失！", QMessageBox.Yes)
                self.select_all_students()
        ############################管理员注册与审批界面################################
        def show_regestor(self):
                sql = 'select * from manager_registor'
                res = cursor.execute(sql)
                info = cursor.fetchall()
                self.glypizhun.setRowCount(res)
                for i in range(res):
                        administor = info[i]
                        admin_id = QTableWidgetItem(administor[0])
                        admin_name = QTableWidgetItem(administor[1])
                        self.glypizhun.setItem(i,0,admin_id)
                        self.glypizhun.setItem(i,1,admin_name)
        def accept_add(self):
                s = self.glypizhun.currentRow()
                ad_id = self.glypizhun.item(s, 0).text()
                ad_name = self.glypizhun.item(s, 1).text()
                sql0 = 'select password from manager_registor where ID = %s'
                cursor.execute(sql0,ad_id)
                password = cursor.fetchone()[0]
                txt = (ad_id,ad_name,password)
                sql2 = 'insert into book_manager(ID,姓名,password) values(%s,%s,%s)'
                cursor.execute(sql2,txt)
                sql1 = 'delete from manager_registor where ID = %s and 姓名 = %s'
                cursor.execute(sql1, (ad_id, ad_name))
                conn.commit()
                QMessageBox.warning(self, "提示", "批准添加管理员成功！", QMessageBox.Yes)
                self.show_regestor()
        def refuse_add(self):
                s = self.glypizhun.currentRow()
                ad_id = self.glypizhun.item(s,0).text()
                ad_name = self.glypizhun.item(s,1).text()
                sql = 'delete from manager_registor where ID = %s and 姓名 = %s'
                cursor.execute(sql,(ad_id,ad_name))
                conn.commit()
                QMessageBox.warning(self, "提示", "已驳回管理员申请！", QMessageBox.Yes)
                self.show_regestor()
        def show_all_managers(self):
                sql = 'select * from book_manager'
                res = cursor.execute(sql)
                info = cursor.fetchall()
                self.glyzhuce.setRowCount(res)
                for i in range(res):
                        administor = info[i]
                        admin_id = QTableWidgetItem(administor[0])
                        admin_name = QTableWidgetItem(administor[1])
                        self.glyzhuce.setItem(i, 0, admin_id)
                        self.glyzhuce.setItem(i, 1, admin_name)
        def add_admin(self):
                new_id = self.id.text()
                new_name = self.name1.text()
                new_password = self.mima1.text()
                if not new_id or not new_name or not new_password:
                        QMessageBox.warning(self, "警告", "ID,姓名和密码不能为空！", QMessageBox.Yes)
                sql = 'SELECT * FROM book_manager WHERE ID = %s'
                res = cursor.execute(sql,new_id)
                if res:
                        QMessageBox.warning(self, "警告", "该管理员ID已被占用！", QMessageBox.Yes)
                else:
                        text = (new_id,new_name,new_password)
                        sql1 = ('insert into book_manager(ID,姓名,password) '
                                'values(%s,%s,%s)')
                        cursor.execute(sql1,text)
                        conn.commit()
                        QMessageBox.warning(self, "提示", "添加管理员成功！", QMessageBox.Yes)
                        self.show_all_managers()
        def select_single_admin(self):
                admin_id = self.ID2.text()
                admin_name = self.name2.text()
                password = self.mima2.text()
                if admin_name or admin_id:
                        txt = (admin_id,admin_name)
                        sql = 'select * from book_manager where ID = %s or 姓名 = %s'
                        res = cursor.execute(sql,txt)
                        infoma = cursor.fetchall()
                        self.all.setRowCount(res)
                        for i in range(res):
                                managers = infoma[i]
                                show_id = QTableWidgetItem(managers[0])
                                show_name = QTableWidgetItem(managers[1])
                                show_mima = QTableWidgetItem(managers[2])
                                self.all.setItem(i,0,show_id)
                                self.all.setItem(i,1,show_name)
                                self.all.setItem(i,2,show_mima)
                        conn.commit()
                else:
                        QMessageBox.warning(self, "警告", "缺少ID或姓名信息！", QMessageBox.Yes)
        def update_admin_password(self):
                admin_id = self.ID2.text()
                admin_name = self.name2.text()
                password = self.mima2.text()
                try:
                        if (admin_name and admin_id and password):
                                text = (password,admin_id,admin_name)
                                sql = ('update book_manager set password = %s '
                                       'where ID = %s and 姓名 = %s')
                                cursor.execute(sql,text)
                                conn.commit()
                                QMessageBox.warning(self, "提示", "密码修改成功！", QMessageBox.Yes)
                                self.select_single_admin()
                        else:
                                QMessageBox.warning(self, "警告", "管理员信息不完整！", QMessageBox.Yes)
                except Exception as e:
                        QMessageBox.warning(self, "警告", "出现错误：" + str(e), QMessageBox.Yes)
        def delete_admin(self):
                de = self.glyzhuce.currentRow()
                ad_id = self.glyzhuce.item(de, 0).text()
                ad_name = self.glyzhuce.item(de, 1).text()
                txt = (ad_id,ad_name)
                QMessageBox.warning(self, "警告", "确定删除 "+str(ad_id)+" 的管理员信息吗？", QMessageBox.Yes)
                sql = 'delete from book_manager where ID = %s and 姓名 = %s'
                cursor.execute(sql,txt)
                conn.commit()
                QMessageBox.warning(self, "提示", "成功移除管理员信息！", QMessageBox.Yes)
                self.show_all_managers()
##################################读者登录信息查看
        def show_all_login(self):
                sql = 'select * from login_record'
                res = cursor.execute(sql)
                if res:
                        info = cursor.fetchall()
                        self.denglulishi.setRowCount(res)
                        for i in range(res):
                                record = info[i]
                                record_id = QTableWidgetItem(record[0])
                                record_date = QTableWidgetItem(str(record[1]))
                                record_times = QTableWidgetItem(str(record[2]))
                                self.denglulishi.setItem(i,0,record_id)
                                self.denglulishi.setItem(i,1,record_date)
                                self.denglulishi.setItem(i,2,record_times)
                else:
                        QMessageBox.warning(self, "提示", "系统无读者登录信息！", QMessageBox.Yes)
                conn.commit()
        def choose_date_select(self):
                date_choose = str(self.riqi.text())
                sql = 'select * from login_record where 日期 = %s'
                res = cursor.execute(sql,date_choose)
                if res:
                        dates = cursor.fetchall()
                        self.denglulishi.setRowCount(res)
                        for i in range(res):
                                records = dates[i]
                                id1 = QTableWidgetItem(records[0])
                                date1 = QTableWidgetItem(str(records[1]))
                                times1 = QTableWidgetItem(str(records[2]))
                                self.denglulishi.setItem(i,0,id1)
                                self.denglulishi.setItem(i,1,date1)
                                self.denglulishi.setItem(i,2,times1)
                else:
                        QMessageBox.warning(self, "提示", "系统在 "+str(date_choose)+" 无读者登录！", QMessageBox.Yes)
                conn.commit()
        def reader_record(self):
                reader_id = self.dezheID.text()
                sql0 = 'select * from reader where ID号 = %s'
                ret = cursor.execute(sql0,reader_id)
                if ret:
                        sql = 'select * from login_record where ID号 = %s'
                        res = cursor.execute(sql,reader_id)
                        if res:
                                infoma = cursor.fetchall()
                                self.denglulishi.setRowCount(res)
                                for i in range(res):
                                        records = infoma[i]
                                        id2 = QTableWidgetItem(records[0])
                                        date2 = QTableWidgetItem(str(records[1]))
                                        times2 = QTableWidgetItem(str(records[2]))
                                        self.denglulishi.setItem(i,0,id2)
                                        self.denglulishi.setItem(i,1,date2)
                                        self.denglulishi.setItem(i,2,times2)
                        else:
                                QMessageBox.warning(self, "提示","读者 "+ str(reader_id) + " 无登录记录",QMessageBox.Yes)
                else:
                        QMessageBox.warning(self, "提示", "读者不存在！", QMessageBox.Yes)