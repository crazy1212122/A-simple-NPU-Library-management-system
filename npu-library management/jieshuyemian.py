import bjjs
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox
from connect import *
import  pymysql
from datetime import datetime, timedelta
cursor,conn=connect()     #连接数据库

class Ui_jieshumian(object):
    def setupUi(self, jieshumian):
        jieshumian.setObjectName("jieshumian")
        jieshumian.resize(709, 515)
        self.centralwidget = QtWidgets.QWidget(jieshumian)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, -120, 711, 591))
        self.listWidget.setStyleSheet("border-image: url(:/唐小天.jpg);")
        self.listWidget.setObjectName("listWidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 130, 302, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ISBN = QtWidgets.QLineEdit(self.layoutWidget)
        self.ISBN.setMinimumSize(QtCore.QSize(300, 40))
        self.ISBN.setObjectName("ISBN")
        self.verticalLayout.addWidget(self.ISBN)
        self.sm = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm.setMinimumSize(QtCore.QSize(300, 40))
        self.sm.setObjectName("sm")
        self.verticalLayout.addWidget(self.sm)
        self.jy = QtWidgets.QPushButton(self.centralwidget)
        self.jy.setGeometry(QtCore.QRect(100, 370, 200, 70))
        self.jy.setMinimumSize(QtCore.QSize(200, 70))
        self.jy.setObjectName("jy")
        self.xj = QtWidgets.QPushButton(self.centralwidget)
        self.xj.setGeometry(QtCore.QRect(400, 370, 200, 70))
        self.xj.setMinimumSize(QtCore.QSize(200, 70))
        self.xj.setObjectName("xj")
        jieshumian.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(jieshumian)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 26))
        self.menubar.setObjectName("menubar")
        jieshumian.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(jieshumian)
        self.statusbar.setObjectName("statusbar")
        jieshumian.setStatusBar(self.statusbar)

        self.loginID = self.getreaderid()
        self.retranslateUi(jieshumian)
        QtCore.QMetaObject.connectSlotsByName(jieshumian)
        self.jy.clicked.connect(self.jieyue)
        self.xj.clicked.connect(self.xujie)

    def retranslateUi(self, jieshumian):
        _translate = QtCore.QCoreApplication.translate
        jieshumian.setWindowTitle(_translate("jieshumian", "MainWindow"))
        self.ISBN.setPlaceholderText(_translate("jieshumian", "ISBN号："))
        self.sm.setPlaceholderText(_translate("jieshumian", "书名："))
        self.jy.setToolTip(_translate("jieshumian", "<html><head/><body>"
                                                    "<p><br/></p></body></html>"))
        self.jy.setText(_translate("jieshumian", "借阅"))
        self.xj.setText(_translate("jieshumian", "续借"))

    #获取当前读者ID
    def getreaderid(self):
        nowtime = time.strftime("%Y-%m-%d", time.localtime())
        sql='SELECT * FROM login_record where 日期 = "%s" ' \
            'order by 单日登录次数' %nowtime
        cursor.execute(sql)
        todaylogin=cursor.fetchall()
        readerlogin=todaylogin[-1]
        ID=readerlogin[0]
        return ID


    def jieyue(self):
        sql7 = 'select * from reader where ID号=%s' % (self.loginID)
        cursor.execute(sql7)
        ite = cursor.fetchall()
        item = ite[0]  ###########规定不同级别借书时间不同
        if item[4] == '研究生':
            readertime = 25
        elif item[4] == '本科生':
            readertime = 20
        elif item[4] == '教授':
            readertime = 30
        bookid=self.ISBN.text()
        bookname=self.sm.text()
        readerid=self.loginID;
        begintime=time.strftime("%Y-%m-%d", time.localtime())
        endtime=datetime.now() + timedelta(days=readertime)
        endtime=endtime.strftime('%Y-%m-%d')
        if bookname == '' and bookid == '':
            QMessageBox.warning(self, "警告", "请输入ISBN号/书名！", QMessageBox.Yes)
        elif bookid == '':
            sql = 'select * from books where 书名="%s"' % (bookname)
            res = cursor.execute(sql)
            bookinfo = cursor.fetchall()
            if res:
                bookid = bookinfo[0][0]
                sql = 'select * from reader where ID号="%s"' % (readerid)
                res = cursor.execute(sql)
                if res:
                    sql = 'select * from books where ISBN号="%s"' % (bookid)
                    res = cursor.execute(sql)
                    bookinfo = cursor.fetchall()
                    if bookinfo[0][7]:
                        sql = 'select * from items where ISBN="%s" and ID="%s" ' \
                              'and 借书时间="%s" and 还书时间="%s"' % (
                            bookid, readerid, begintime, endtime)
                        res = cursor.execute(sql)
                        if res:
                            QMessageBox.warning(self, "警告", "请勿重复提交！", QMessageBox.Yes)
                        else:
                            sql = 'insert into items(ISBN,ID,借书时间,type,还书时间) ' \
                                  'VALUES ("%s","%s","%s","borrow","%s")' % (
                                bookid, readerid, begintime, endtime)
                            cursor.execute(sql)
                            conn.commit()
                            QMessageBox.warning(self, "提示", "借阅请求提交成功！", QMessageBox.Yes)
                    else:
                        QMessageBox.warning(self, "警告", "这本书已经被借光啦！", QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, "警告", "学号输入错误！请重新输入！", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "警告", "书名输入错误！请重新输入！", QMessageBox.Yes)
        elif bookname == '':
            sql = 'select * from books where ISBN号="%s"' % (bookid)
            res = cursor.execute(sql)
            if res:
                sql = 'select * from reader where ID号="%s"' % (readerid)
                res = cursor.execute(sql)
                if res:
                    sql = 'select * from books where ISBN号="%s"' % (bookid)
                    res = cursor.execute(sql)
                    bookinfo = cursor.fetchall()
                    if bookinfo[0][7]:
                        sql = 'select * from items where ISBN="%s" and ID="%s" ' \
                              'and 借书时间="%s" and 还书时间="%s"' % (
                            bookid, readerid, begintime, endtime)
                        res = cursor.execute(sql)
                        if res:
                            QMessageBox.warning(self, "警告", "请勿重复提交！", QMessageBox.Yes)
                        else:
                            sql = 'insert into items(ISBN,ID,借书时间,type,还书时间) ' \
                                  'VALUES ("%s","%s","%s","borrow","%s")' % (
                                bookid, readerid, begintime, endtime)
                            cursor.execute(sql)
                            conn.commit()
                            QMessageBox.warning(self, "提示", "借阅请求提交成功！", QMessageBox.Yes)
                    else:
                        QMessageBox.warning(self, "警告", "这本书已经被借光啦！", QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, "警告", "学号输入错误！请重新输入！", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "警告", "ISBN号输入错误！请重新输入！", QMessageBox.Yes)
        else:
            sql = 'select * from books where ISBN号="%s" and 书名="%s"' % (bookid,bookname)
            res = cursor.execute(sql)
            if res:
                sql = 'select * from reader where ID号="%s"' % (readerid)
                res = cursor.execute(sql)
                if res:
                    sql = 'select * from books where ISBN号="%s"' % (bookid)
                    res = cursor.execute(sql)
                    bookinfo = cursor.fetchall()
                    if bookinfo[0][7]:
                        sql = 'select * from items where ISBN="%s" and ID="%s" ' \
                              'and 借书时间="%s" and 还书时间="%s"' % (
                            bookid, readerid, begintime, endtime)
                        res = cursor.execute(sql)
                        if res:
                            QMessageBox.warning(self, "警告", "请勿重复提交！", QMessageBox.Yes)
                        else:
                            sql = 'insert into items(ISBN,ID,借书时间,type,还书时间) ' \
                                  'VALUES ("%s","%s","%s","borrow","%s")' % (
                                bookid, readerid, begintime, endtime)
                            cursor.execute(sql)
                            conn.commit()
                            QMessageBox.warning(self, "提示", "借阅请求提交成功！", QMessageBox.Yes)
                    else:
                        QMessageBox.warning(self, "警告", "这本书已经被借光啦！", QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, "警告", "学号输入错误！请重新输入！", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "警告", "ISBN号与书名不匹配！请重新输入！", QMessageBox.Yes)

    def xujie(self):
        sql7 = 'select * from reader where ID号=%s' % (self.loginID)
        cursor.execute(sql7)
        ite = cursor.fetchall()
        item = ite[0]  ###########规定不同级别借书时间不同
        if item[4] == '研究生':
            readertime = 25
        elif item[4] == '本科生':
            readertime = 20
        elif item[4] == '教授':
            readertime = 30
        bookid = self.ISBN.text()
        bookname = self.sm.text()
        readerid = self.loginID;
        begintime = time.strftime("%Y-%m-%d", time.localtime())
        endtime = datetime.now() + timedelta(days=readertime)
        endtime = endtime.strftime('%Y-%m-%d')
        if bookname == '' and bookid == '':
            QMessageBox.warning(self, "警告", "请输入ISBN号/书名！", QMessageBox.Yes)
        elif bookid == '':
            sql = 'select * from books where 书名="%s"' % (bookname)
            res = cursor.execute(sql)
            bookinfo = cursor.fetchall()
            if res:
                bookid = bookinfo[0][0]
                sql = 'select * from reader where ID号="%s"' % (readerid)
                res = cursor.execute(sql)
                if res:
                    sql = 'select * from borrow_record where ' \
                          'ISBN="%s" and 读者ID="%s"' % (bookid, readerid)
                    res = cursor.execute(sql)
                    if res:
                        sql = 'select * from items where ISBN="%s" ' \
                              'and ID="%s" and 借书时间="%s" and 还书时间="%s"' % (
                            bookid, readerid, begintime, endtime)
                        res = cursor.execute(sql)
                        if res:
                            QMessageBox.warning(self, "警告", "请勿重复提交！", QMessageBox.Yes)
                        else:
                            sql = 'insert into items(ISBN,ID,借书时间,type,还书时间) ' \
                                  'VALUES ("%s","%s","%s","borrow","%s")' % (
                                bookid, readerid, begintime, endtime)
                            cursor.execute(sql)
                            conn.commit()
                            QMessageBox.warning(self, "提示", "续借请求提交成功！", QMessageBox.Yes)
                    else:
                        QMessageBox.warning(self, "警告", "您未借过这本书！", QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, "警告", "学号输入错误！请重新输入！", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "警告", "书名输入错误！请重新输入！", QMessageBox.Yes)
        elif bookname == '':
            sql = 'select * from books where ISBN号="%s"' % (bookid)
            res = cursor.execute(sql)
            if res:
                sql = 'select * from reader where ID号="%s"' % (readerid)
                res = cursor.execute(sql)
                if res:
                    sql = 'select * from borrow_record where ISBN="%s" ' \
                          'and 读者ID="%s"' % (bookid, readerid)
                    res = cursor.execute(sql)
                    if res:
                        sql = 'select * from items where ISBN="%s" and ID="%s" ' \
                              'and 借书时间="%s" and 还书时间="%s"' % (
                            bookid, readerid, begintime, endtime)
                        res = cursor.execute(sql)
                        if res:
                            QMessageBox.warning(self, "警告", "请勿重复提交！", QMessageBox.Yes)
                        else:
                            sql = 'insert into items(ISBN,ID,借书时间,type,还书时间) ' \
                                  'VALUES ("%s","%s","%s","borrow","%s")' % (
                                bookid, readerid, begintime, endtime)
                            cursor.execute(sql)
                            conn.commit()
                            QMessageBox.warning(self, "提示", "续借请求提交成功！", QMessageBox.Yes)
                    else:
                        QMessageBox.warning(self, "警告", "您未借过这本书！", QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, "警告", "学号输入错误！请重新输入！", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "警告", "ISBN号输入错误！请重新输入！", QMessageBox.Yes)
        else:
            sql = 'select * from books where ISBN号="%s" and 书名="%s"' % (bookid,bookname)
            res = cursor.execute(sql)
            if res:
                sql = 'select * from reader where ID号="%s"' % (readerid)
                res = cursor.execute(sql)
                if res:
                    sql = 'select * from borrow_record ' \
                          'where ISBN="%s" and 读者ID="%s"' % (bookid, readerid)
                    res = cursor.execute(sql)
                    if res:
                        sql = 'select * from items where ISBN="%s" and ID="%s" ' \
                              'and 借书时间="%s" and 还书时间="%s"' % (
                            bookid, readerid, begintime, endtime)
                        res = cursor.execute(sql)
                        if res:
                            QMessageBox.warning(self, "警告", "请勿重复提交！", QMessageBox.Yes)
                        else:
                            sql = 'insert into items(ISBN,ID,借书时间,type,还书时间) ' \
                                  'VALUES ("%s","%s","%s","borrow","%s")' % (
                                bookid, readerid, begintime, endtime)
                            cursor.execute(sql)
                            conn.commit()
                            QMessageBox.warning(self, "提示", "续借请求提交成功！", QMessageBox.Yes)
                    else:
                        QMessageBox.warning(self, "警告", "您未借过这本书！", QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, "警告", "学号输入错误！请重新输入！", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "警告", "ISBN号与书名不匹配！请重新输入！", QMessageBox.Yes)