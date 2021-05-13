from PyQt5 import uic
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5.QtCore import pyqtSlot

from DBViewPwd import viewShd
from DBAddShdU import shd

from encrypt import *

from DialogMsg import Msg
Ui_Table,baseClass=uic.loadUiType('UI/viewusers.ui')

class SusrView(baseClass):
    def __init__(self,username):
        super(SusrView,self).__init__()
        self.username = username
        self.row=""
        self.col=""
        #code start
        self.ui=Ui_Table()
        self.ui.setupUi(self)
        self.get=viewShd(self.username)
        self.ui.Pwd_table.cellClicked.connect(self.cellClick)
        self.ui.Usr_Delete.clicked.connect(self.unshare)
        self.z=self.get.getusers()
        for y in range(len(self.z)):
            self.ui.Pwd_table.setItem(y,0,QTableWidgetItem(self.z[y][2]))
            self.ui.Pwd_table.setItem(y,1,QTableWidgetItem(self.z[y][0]))
    
    def cellClick(self, row, col):
        self.row = row
        self.col = col

    def unshare(self):
        if(self.row!=""):
            if(self.ui.Pwd_table.item(self.row,self.col).text()!=""):
                usr2=self.ui.Pwd_table.item(self.row,1).text()
                service=self.ui.Pwd_table.item(self.row,0).text()
                self.unsh=shd()
                self.unsh.unshare(self.username,usr2,service)
                Msg("Password has been unshared").exec_()
                for i in range(2):
                    self.ui.Pwd_table.setItem(self.row,i,QTableWidgetItem(""))
            else:
                Msg("Select a User").exec_()
        else:
            Msg("Select a User").exec_()




