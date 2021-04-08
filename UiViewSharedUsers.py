from PyQt5 import uic
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5.QtCore import pyqtSlot

from DBViewPwd import viewShd

from encrypt import *

Ui_Table,baseClass=uic.loadUiType('UI/viewusers.ui')

class SusrView(baseClass):
    def __init__(self,username):
        super(SusrView,self).__init__()
        self.username = username
        #code start
        self.ui=Ui_Table()
        self.ui.setupUi(self)
        self.get=viewShd(self.username)
        self.z=self.get.getusers()
        for y in range(len(self.z)):
            self.ui.Pwd_table.setItem(y,0,QTableWidgetItem(self.z[y][2]))
            self.ui.Pwd_table.setItem(y,1,QTableWidgetItem(self.z[y][0]))

