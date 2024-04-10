import sys
import pymysql
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from denglu import Ui_MainWindow
from xuesheng import Ui_Form3
from guanyu import Ui_guanyu
from manager import Ui_Admin
from zhuceduzhe import Ui_zhuce1
from zhucegaunliyuan import Ui_zhuce3
from xiugai import Ui_Form
from connect import *

cursor,conn=connect()

class guanyuui(QtWidgets.QMainWindow,Ui_guanyu):
    def __init__(self, parent=None):
        super(guanyuui, self).__init__(parent)
        self.setupUi(self)
class Readerui(QtWidgets.QMainWindow,Ui_Form3):
    def __init__(self, parent=None):
        super(Readerui, self).__init__(parent)
        self.setupUi(self)
class Adminui(QtWidgets.QMainWindow,Ui_Admin):
    def __init__(self, parent=None):
        super(Adminui, self).__init__(parent)
        self.setupUi(self)
class duzheui(QtWidgets.QMainWindow,Ui_zhuce1):
    def __init__(self, parent=None):
        super(duzheui, self).__init__(parent)
        self.setupUi(self)
class guanliui(QtWidgets.QMainWindow,Ui_zhuce3):
    def __init__(self, parent=None):
        super(guanliui, self).__init__(parent)
        self.setupUi(self)
class xiugaiui(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self, parent=None):
        super(xiugaiui, self).__init__(parent)
        self.setupUi(self)

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.tc.clicked.connect(self.exit)
        self.dl.clicked.connect(self.login)
        self.log1.triggered.connect(self.register1)
        self.log2.triggered.connect(self.register2)
        self.cp.triggered.connect(self.update)
        self.actioninfomation.triggered.connect(self.guanyuyu)
    def guanyuyu(self):
        self.read = guanyuui()
        self.read.show()
    def exit(self):    #退出
        rec_code=QMessageBox.question(self, "确认", "您确认要退出吗？", QMessageBox.Yes | QMessageBox.No)
        if rec_code != 65536:
            self.close()
    def register1(self):    #注册为读者
        self.zhuce1 = duzheui()
        self.zhuce1.show()
        self.close()
    def register2(self):    #注册为管理员
        self.zhuce2 = guanliui()
        self.zhuce2.show()
        self.close()
    def update(self):    #读者修改密码
        self.update = xiugaiui()
        self.update.show()
        self.close()
    def login(self):   #登陆
        ID=self.xh.text()
        PW=self.mm.text()
        if ID=='' or PW=='':
            QMessageBox.warning(self, "警告", "请输入用户名/密码", QMessageBox.Yes)
        else:
            if self.cb1.currentText()=='读者':
                sql = 'select * from reader where ID号 = %s and password=%s'
                res = cursor.execute(sql,(ID, PW))
                if res:
                    logintime=time.strftime("%Y-%m-%d", time.localtime())
                    sql='select * from login_record where 日期="%s"' %logintime
                    res=cursor.execute(sql)
                    logined = cursor.fetchall()
                    if  res:
                        last=logined[-1]
                        number=last[-1]
                        num=number+1
                        sql='INSERT INTO login_record(ID号,日期,单日登录次数) VALUES(%s,"%s",%d)' %(ID,logintime,num)
                        cursor.execute(sql)
                        conn.commit()
                    else:
                        sql = 'INSERT INTO login_record(ID号,日期,单日登录次数) VALUES(%s,"%s",%d)' % (ID, logintime, 1)
                        cursor.execute(sql)
                        conn.commit()
                    self.read = Readerui()
                    self.read.show()
                    self.close()
                else:
                    QMessageBox.warning(self, "警告", "密码错误，请重新输入！", QMessageBox.Yes)
            elif self.cb1.currentText()=='管理员':
                sql = 'select * from book_manager where ID = %s and password=%s'
                res = cursor.execute(sql,(ID, PW))
                # cursor.close()
                # conn.close()
                # 进行判断
                if res:
                    self.bookadmin = Adminui()
                    self.bookadmin.show()
                    self.close()
                    pass
                else:
                    QMessageBox.warning(self, "警告", "密码错误，请重新输入！", QMessageBox.Yes)

#固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
app = QApplication(sys.argv)
#初始化
myWin = MyMainForm()
#将窗口控件显示在屏幕上
myWin.show()
#程序运行，sys.exit方法确保程序完整退出。
sys.exit(app.exec_())