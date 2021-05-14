from PyQt5 import uic
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
import pyperclip
from DBbanking import bdb
from encrypt import *
from DBaddpasswords import db

from DialogMsg import Msg
Ui_Table,baseClass=uic.loadUiType('UI/viewbnkpwds.ui')

class BusrView(baseClass):
    def __init__(self,username):
        super(BusrView,self).__init__()
        self.username = username
        self.row=""
        self.col=""
        #code start
        self.ui=Ui_Table()
        self.ui.setupUi(self)
        self.ui.Pwd_table.hideColumn(2)
        self.ui.Pwd_table.hideColumn(3)
        self.get=bdb(self.username)
        self.ui.Pwd_table.cellClicked.connect(self.cellClick)
        self.ui.Copy1.clicked.connect(self.copy1)
        self.ui.Copy2.clicked.connect(self.copy2)
        self.ui.Delete.clicked.connect(self.delete)
        self.ui.Pwd_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.Show.clicked.connect(lambda :self.showpwd())
        #qtable
        for x in range(len(self.get.view1())):
            for y in range(1,len(self.get.view1()[x])):
                if(y==1):
                    self.ui.Pwd_table.setItem(x,0,QTableWidgetItem(self.get.view1()[x][y]))
                elif (y==2):
                    self.ui.Pwd_table.setItem(x,1,QTableWidgetItem(self.get.view1()[x][y]))
                elif (y==3):
                    pwd1=self.decrypt(self.get.view1()[x][y])
                    self.ui.Pwd_table.setItem(x,2,QTableWidgetItem(pwd1))
                elif (y==4):
                    pwd2=self.decrypt(self.get.view1()[x][y])
                    self.ui.Pwd_table.setItem(x,3,QTableWidgetItem(pwd2))
    def showpwd(self):
        self.ui.Pwd_table.showColumn(2)
        self.ui.Pwd_table.showColumn(3)
        self.ui.Show.setText("Hide Password")
        self.ui.Show.clicked.connect(lambda :self.hidepwd())
    def hidepwd(self):
        self.ui.Pwd_table.hideColumn(2)
        self.ui.Pwd_table.hideColumn(3)
        self.ui.Show.setText("Show Password")
        self.ui.Show.clicked.connect(lambda :self.showpwd())
    def cellClick(self, row, col):
        self.row = row
        self.col = col
    def copy1(self):
        if(self.row!=""):
            if(self.ui.Pwd_table.item(self.row,self.col).text()!=""):
                z=self.ui.Pwd_table.item(self.row,2).text()
                #print(z)
                pyperclip.copy(z)
                self.cpy=Msg("Login Password has been copied").exec_()
            else:
                Msg("Select a Password Field").exec_()
        else:
            Msg("Select a Password Field").exec_()
    def copy2(self):
        if(self.row!=""):
            if(self.ui.Pwd_table.item(self.row,self.col).text()!=""):
                z=self.ui.Pwd_table.item(self.row,3).text()
                #print(z)
                pyperclip.copy(z)
                self.cpy=Msg("Login Password has been copied").exec_()
            else:
                Msg("Select a Password Field").exec_()
        else:
            Msg("Select a Password Field").exec_()
    
    def decrypt(self,str):
        self.key=db(self.username).getkey()
        self.str=str
        self.pwd=AESCipher(self.key)
        return self.pwd.decrypt(self.str)
    def delete(self):
        self.cid=self.ui.Pwd_table.item(self.row,1).text()
        self.delt=bdb(self.username)
        if(self.delt.delete(self.cid)):
            self.suc=Msg("Deletion complete").exec_()
            for i in range(4):
                self.ui.Pwd_table.setItem(self.row,i,QTableWidgetItem(""))
        else:
            self.fai=Msg("Unable to Delete").exec_()

