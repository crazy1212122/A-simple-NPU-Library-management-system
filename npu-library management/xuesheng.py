
import bjxs
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox
from connect import *
from jieshuyemian import Ui_jieshumian
from huanshuyemian import Ui_huanshumian
import  pymysql
cursor,conn=connect()     #连接数据库

class jieshuui(QtWidgets.QMainWindow, Ui_jieshumian):
    def __init__(self, parent=None):
        super(jieshuui, self).__init__(parent)
        self.setupUi(self)

class huanshuui(QtWidgets.QMainWindow, Ui_huanshumian):
    def __init__(self, parent=None):
        super(huanshuui, self).__init__(parent)
        self.setupUi(self)

class Ui_Form3(object):
    def setupUi(self, Form3):
        Form3.setObjectName("Form3")
        Form3.resize(1152, 749)
        self.label = QtWidgets.QLabel(Form3)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form3)
        self.widget.setGeometry(QtCore.QRect(780, 40, 331, 441))
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
        self.lb = QtWidgets.QLineEdit(self.widget)
        self.lb.setMinimumSize(QtCore.QSize(300, 40))
        self.lb.setStyleSheet("")
        self.lb.setText("")
        self.lb.setCursorPosition(0)
        self.lb.setObjectName("lb")
        self.verticalLayout_3.addWidget(self.lb)
        self.tableWidget = QtWidgets.QTableWidget(Form3)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 711, 471))
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
        self.layoutWidget = QtWidgets.QWidget(Form3)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 540, 711, 169))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chaquanbu = QtWidgets.QPushButton(self.layoutWidget)
        self.chaquanbu.setMinimumSize(QtCore.QSize(0, 50))
        self.chaquanbu.setObjectName("chaquanbu")
        self.verticalLayout.addWidget(self.chaquanbu)
        self.chaxun = QtWidgets.QPushButton(self.layoutWidget)
        self.chaxun.setMinimumSize(QtCore.QSize(200, 50))
        self.chaxun.setObjectName("chaxun")
        self.verticalLayout.addWidget(self.chaxun)
        self.listWidget = QtWidgets.QListWidget(Form3)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 1151, 751))
        self.listWidget.setStyleSheet("border-image: url(:/书1.jpg);")
        self.listWidget.setObjectName("listWidget")
        self.guihuan = QtWidgets.QPushButton(Form3)
        self.guihuan.setGeometry(QtCore.QRect(780, 610, 329, 80))
        self.guihuan.setMinimumSize(QtCore.QSize(0, 80))
        self.guihuan.setObjectName("guihuan")
        self.jieshu = QtWidgets.QPushButton(Form3)
        self.jieshu.setGeometry(QtCore.QRect(780, 500, 329, 80))
        self.jieshu.setMinimumSize(QtCore.QSize(0, 80))
        self.jieshu.setObjectName("jieshu")
        self.listWidget.raise_()
        self.layoutWidget.raise_()
        self.widget.raise_()
        self.label.raise_()
        self.tableWidget.raise_()
        self.guihuan.raise_()
        self.jieshu.raise_()

        self.retranslateUi(Form3)
        self.loginID = self.getreaderid()
        QtCore.QMetaObject.connectSlotsByName(Form3)
        self.chaxun.clicked.connect(self.borrowidcheck)
        self.guihuan.clicked.connect(self.returnbook)
        self.chaquanbu.clicked.connect(self.selectallbook)
        self.jieshu.clicked.connect(self.borrowbook)

    def retranslateUi(self, Form3):
        _translate = QtCore.QCoreApplication.translate
        Form3.setWindowTitle(_translate("Form3", "Form"))
        self.label.setText(_translate("Form3",
                                      "<html><head/><body><p><span style=\" font-size:14pt;\">"
                                      "书籍信息</span></p></body></html>"))
        self.sm.setPlaceholderText(_translate("Form3", "书名："))
        self.sh.setPlaceholderText(_translate("Form3", "ISBN号："))
        self.zz.setPlaceholderText(_translate("Form3", "作者："))
        self.lb.setPlaceholderText(_translate("Form3", "类别："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form3", "ISBN号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form3", "书名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form3", "作者"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form3", "书籍类别"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form3", "出版社"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form3", "被借次数"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form3", "馆藏次数"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form3", "在馆册数"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form3", "书架号"))
        self.chaquanbu.setText(_translate("Form3", "查询全部"))
        self.chaxun.setText(_translate("Form3", "查询"))
        self.guihuan.setText(_translate("Form3", "前往还书页面"))
        self.jieshu.setText(_translate("Form3", "前往借书页面"))

    #借书信息查询
    def borrowidcheck(self):
        bookisbn=self.sh.text()
        bookname=self.sm.text()
        bookauthor=self.zz.text()
        booktype=self.lb.text()
        sql='select * from books where ISBN号="%s" ' \
            'or 书名="%s" or 作者="%s" or 书籍类别="%s"'% \
            (bookisbn,bookname,bookauthor,booktype)
        sql1 = 'select * from books where ISBN号="%s" ' \
              'or 书名="%s" or 作者="%s" or 书籍类别="%s"' % \
              (bookisbn, bookname, bookauthor, booktype)
        res = cursor.execute(sql)
        bookinfo=cursor.fetchall()
        n=len(bookinfo)
        self.tableWidget.setRowCount(n)
        for i in range(n):
            book=bookinfo[i]
            bookid1 = QTableWidgetItem(book[0])
            bookname1 = QTableWidgetItem(book[1])
            bookauthor1 = QTableWidgetItem(book[2])
            booktype1 = QTableWidgetItem(book[3])
            bookpress1 = QTableWidgetItem(book[4])
            bookborrowednum1 = QTableWidgetItem(str(book[5]))
            booklibhavenum1 = QTableWidgetItem(str(book[6]))
            booklibstillhavenum1 = QTableWidgetItem(str(book[7]))
            booknumber1 = QTableWidgetItem(book[8])
            bookid = QTableWidgetItem(book[0])
            bookname = QTableWidgetItem(book[1])
            bookauthor = QTableWidgetItem(book[2])
            booktype = QTableWidgetItem(book[3])
            bookpress = QTableWidgetItem(book[4])
            bookborrowednum = QTableWidgetItem(str(book[5]))
            booklibhavenum = QTableWidgetItem(str(book[6]))
            booklibstillhavenum = QTableWidgetItem(str(book[7]))
            booknumber = QTableWidgetItem(book[8])
            self.tableWidget.setItem(i,0, bookid)
            self.tableWidget.setItem(i,1, bookname)
            self.tableWidget.setItem(i,2, bookauthor)
            self.tableWidget.setItem(i,3, booktype)
            self.tableWidget.setItem(i,4, bookpress)
            self.tableWidget.setItem(i,5, bookborrowednum)
            self.tableWidget.setItem(i,6, booklibhavenum)
            self.tableWidget.setItem(i,7, booklibstillhavenum)
            self.tableWidget.setItem(i,8, booknumber)

    #获取当前读者ID
    def getreaderid(self):
        nowtime = time.strftime("%Y-%m-%d", time.localtime())
        sql='SELECT * FROM login_record where 日期 = ' \
            '"%s" order by 单日登录次数' %nowtime
        sql1 = 'SELECT * FROM login_record where 日期 = ' \
              '"%s" order by 单日登录次数' % nowtime
        cursor.execute(sql)
        todaylogin=cursor.fetchall()
        readerlogin=todaylogin[-1]
        ID=readerlogin[0]
        return ID

    #查询所有书籍
    def selectallbook(self):
        sql='SELECT * FROM books'
        cursor.execute(sql)
        books=cursor.fetchall()
        booknumber=len(books)
        self.tableWidget.setRowCount(booknumber)
        for i in range(booknumber):
            book=books[i]
            bookid1 = QTableWidgetItem(book[0])
            bookname1 = QTableWidgetItem(book[1])
            bookauthor1 = QTableWidgetItem(book[2])
            booktype1 = QTableWidgetItem(book[3])
            bookpress1 = QTableWidgetItem(book[4])
            bookborrowednum1 = QTableWidgetItem(str(book[5]))
            booklibhavenum1 = QTableWidgetItem(str(book[6]))
            booklibstillhavenum1 = QTableWidgetItem(str(book[7]))
            booknumber1 = QTableWidgetItem(book[8])
            bookid = QTableWidgetItem(book[0])
            bookname = QTableWidgetItem(book[1])
            bookauthor = QTableWidgetItem(book[2])
            booktype = QTableWidgetItem(book[3])
            bookpress = QTableWidgetItem(book[4])
            bookborrowednum = QTableWidgetItem(str(book[5]))
            booklibhavenum = QTableWidgetItem(str(book[6]))
            booklibstillhavenum = QTableWidgetItem(str(book[7]))
            booknumber = QTableWidgetItem(book[8])
            self.tableWidget.setItem(i, 0, bookid)
            self.tableWidget.setItem(i, 1, bookname)
            self.tableWidget.setItem(i, 2, bookauthor)
            self.tableWidget.setItem(i, 3, booktype)
            self.tableWidget.setItem(i, 4, bookpress)
            self.tableWidget.setItem(i, 5, bookborrowednum)
            self.tableWidget.setItem(i, 6, booklibhavenum)
            self.tableWidget.setItem(i, 7, booklibstillhavenum)
            self.tableWidget.setItem(i, 8, booknumber)

    def borrowbook(self):
        self.read = jieshuui()
        self.read.show()

    def returnbook(self):
        self.read = huanshuui()
        self.read.show()