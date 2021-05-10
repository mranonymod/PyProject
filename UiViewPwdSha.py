from PyQt5 import uic
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5.QtCore import pyqtSlot

from DBViewPwd import viewShd

from encrypt import *

Ui_Table,baseClass=uic.loadUiType('UI/sharedpwdview.ui')

class SpwdView(baseClass):
    def __init__(self,username):
        super(SpwdView,self).__init__()
        self.username = username
        #code start
        self.ui=Ui_Table()
        self.ui.setupUi(self)
        self.get=viewShd(self.username)
        self.ui.Pwd_table.hideColumn(2)
        self.ui.Sha_Show.clicked.connect(lambda : self.ui.Pwd_table.showColumn(2))
        self.rows,self.key=self.get.getPasses(self.username)
        for x in range(len(self.rows)):
            for y in range(len(self.rows[x])):
                if(y==2):
                    ek=self.rows[x][y]
                    pk=self.decrypt(ek)
                    self.ui.Pwd_table.setItem(x,y,QTableWidgetItem(ek))    
                else:
                    pass
                    self.ui.Pwd_table.setItem(x,y,QTableWidgetItem(self.rows[x][y]))     
    def decrypt(self,str):
        self.key=db(self.username).getkey()
        self.str=str
        self.pwd=AESCipher(self.key)
        return self.pwd.decrypt(self.str)
    def upd(self):
        print("cell value changed")