from PyQt5 import uic
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from DBaddpasswords import db
import pyperclip
from DBViewPwd import viewPers
from DBdelpwd import db1
from DialogMsg import Msg
from autologin import *

from encrypt import *

Ui_Table,baseClass=uic.loadUiType('UI/personalviewpwd.ui')

class PpwdView(baseClass):
    def __init__(self,username):
        super(PpwdView,self).__init__()
        self.username = username
        self.row=""
        self.col=""
        #code start
        self.ui=Ui_Table()
        self.ui.setupUi(self)
        self.ui.Pwd_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.get=viewPers(self.username)
        self.ui.Pwd_table.hideColumn(2)
        self.ui.Per_Show.clicked.connect(lambda :self.showpwd())
        self.ui.Per_Copy.clicked.connect(lambda:self.copied())
        self.ui.Per_Delete.clicked.connect(lambda:self.delete())
        self.ui.Pwd_table.cellClicked.connect(self.cellClick)
        self.ui.Per_Login.clicked.connect(lambda : self.checkAL())
        for x in range(len(self.get.find())):
            for y in range(len(self.get.find()[x])):
                if(y==2):
                    self.ui.Pwd_table.setItem(x,1,QTableWidgetItem(self.get.find()[x][y]))
                elif(y==6):
                    date=(self.get.find()[x][y]).strftime("%m-%d-%Y, %H:%M:%S")
                    self.ui.Pwd_table.setItem(x,3,QTableWidgetItem(date))
                elif(y==5):
                    ek=self.get.find()[x][y]
                    pk=self.decrypt(ek)
                    self.ui.Pwd_table.setItem(x,2,QTableWidgetItem(pk))
                elif(y==3):
                    self.ui.Pwd_table.setItem(x,0,QTableWidgetItem(self.get.find()[x][y]))
                else:
                    pass
    def checkAL(self):
        if(self.row!=""):
            if(self.ui.Pwd_table.item(self.row,self.col).text()!=""):
                if(AutoLogin(self.ui.Pwd_table.item(self.row,0).text(),self.ui.Pwd_table.item(self.row,1).text(),self.ui.Pwd_table.item(self.row,2).text())):
                    pass
                else:
                    Msg("Service Doesn't Support Autologin").exec_()
            else:
                Msg("Select an Account").exec_()
        else:
            Msg("Select an Account").exec_()
    def delete(self):
        self.user=self.ui.Pwd_table.item(self.row,1).text()
        self.serv=self.ui.Pwd_table.item(self.row,0).text()
        self.delt=db1(self.user,self.serv)
        if(self.delt.delete()):
            self.suc=Msg("Deletion complete").exec_()
            for i in range(4):
                self.ui.Pwd_table.setItem(self.row,i,QTableWidgetItem(""))

        else:
            self.fai=Msg("Unshare Password First").exec_()

    def cellClick(self, row, col):
        self.row = row
        self.col = col
        #print(self.row,self.col)
    def copied(self):
        print(self.row,self.col)
        if(self.row!=""):
            if(self.ui.Pwd_table.item(self.row,self.col).text()!=""):
                z=self.ui.Pwd_table.item(self.row,self.col).text()
                #print(z)
                pyperclip.copy(z)
                self.cpy=Msg("Password has been copied").exec_()
            else:
                Msg("Select an Account").exec_()
        else:
            Msg("Select an Account").exec_()
    def showpwd(self):
        self.ui.Pwd_table.showColumn(2)
        self.ui.Per_Show.setText("Hide Password")
        self.ui.Per_Show.clicked.connect(lambda :self.hidepwd())
    def hidepwd(self):
        self.ui.Pwd_table.hideColumn(2)
        self.ui.Per_Show.setText("Show Password")
        self.ui.Per_Show.clicked.connect(lambda :self.showpwd())

    def decrypt(self,str):
        self.key=db(self.username).getkey()
        self.str=str
        self.pwd=AESCipher(self.key)
        return self.pwd.decrypt(self.str)
    def upd(self):
        print("cell value changed")