from PyQt5 import uic
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5.QtCore import pyqtSlot

from DBViewPwd import viewShd
from DBaddpasswords import db
from encrypt import *
from autologin import *
from DialogMsg import Msg

Ui_Table,baseClass=uic.loadUiType('UI/sharedpwdview.ui')

class SpwdView(baseClass):
    def __init__(self,username):
        super(SpwdView,self).__init__()
        self.username = username
        #code start
        self.row=""
        self.col=""
        self.ui=Ui_Table()
        self.ui.setupUi(self)
        self.get=viewShd(self.username)
        self.ui.Pwd_table.hideColumn(2)
        self.ui.Pwd_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.Sha_Show.clicked.connect(lambda :self.showpwd())
        self.rows,self.key=self.get.getPasses(self.username)
        self.ui.Pwd_table.cellClicked.connect(self.cellClick)
        self.ui.Sha_Login.clicked.connect(lambda : self.checkAL())
        for x in range(len(self.rows)):
            for y in range(len(self.rows[x])):
                if(y==2):
                    ek=self.rows[x][y]
                    usr1=self.rows[x][0]
                    pk=self.decrypt(ek,usr1)
                    self.ui.Pwd_table.setItem(x,y,QTableWidgetItem(pk))    
                elif(y==0):
                    self.ui.Pwd_table.setItem(x,y,QTableWidgetItem(self.rows[x][1]))    
                elif(y==1):
                    self.ui.Pwd_table.setItem(x,y,QTableWidgetItem(self.rows[x][0])) 
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
    def cellClick(self, row, col):
        self.row = row
        self.col = col
        print(self.row,self.col)
    def showpwd(self):
        self.ui.Pwd_table.showColumn(2)
        self.ui.Sha_Show.setText("Hide Password")
        self.ui.Sha_Show.clicked.connect(lambda :self.hidepwd())
    def hidepwd(self):
        self.ui.Pwd_table.hideColumn(2)
        self.ui.Sha_Show.setText("Show Password")
        self.ui.Sha_Show.clicked.connect(lambda :self.showpwd())
    def decrypt(self,str,usr1):
        self.user1=usr1
        self.key=db(self.user1).getkey()
        self.str=str
        self.pwd=AESCipher(self.key)
        return self.pwd.decrypt(self.str)
    def upd(self):
        print("cell value changed")