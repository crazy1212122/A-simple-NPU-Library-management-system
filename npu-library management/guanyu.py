
import bjjs
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox
from connect import *
import  pymysql
cursor,conn=connect()     #连接数据库

class Ui_guanyu(object):
    def setupUi(self, guanyu):
        guanyu.setObjectName("guanyu")
        guanyu.resize(800, 600)
        guanyu.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.centralwidget = QtWidgets.QWidget(guanyu)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 50, 231, 41))
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(460, 240, 281, 163))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 140, 391, 371))
        self.listWidget.setStyleSheet("border-image: url(:/唐小天.jpg);")
        self.listWidget.setObjectName("listWidget")
        guanyu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(guanyu)
        self.statusbar.setObjectName("statusbar")
        guanyu.setStatusBar(self.statusbar)

        self.retranslateUi(guanyu)
        QtCore.QMetaObject.connectSlotsByName(guanyu)

    def retranslateUi(self, guanyu):
        _translate = QtCore.QCoreApplication.translate
        guanyu.setWindowTitle(_translate("guanyu", "MainWindow"))
        self.label_3.setText(_translate("guanyu", "<html><head/><body><p><span style=\" font-size:20pt; color:#ff0000;\">关于我们</span></p></body></html>"))
        self.label.setText(_translate("guanyu", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffaa00;\">图书管理系统v1.0</span></p></body></html>"))
        self.label_2.setText(_translate("guanyu", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffaa00;\">沈文恺   张超  赵赟骥</span></p></body></html>"))
