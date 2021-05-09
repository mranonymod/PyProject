from PyQt5 import uic
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from DBaddpasswords import db
import pyperclip
from DBViewPwd import viewPers
from DialogMsg import Msg

from encrypt import *

Ui_Table,baseClass=uic.loadUiType('UI/personalviewpwd.ui')

class PpwdView(baseClass):
    def __init__(self,username):
        super(PpwdView,self).__init__()
        self.username = username
        #code start
        self.ui=Ui_Table()
        self.ui.setupUi(self)
        self.get=viewPers(self.username)
        self.ui.Pwd_table.hideColumn(2)
        self.ui.Per_Show.clicked.connect(lambda :self.showpwd())
        self.ui.Per_Copy.clicked.connect(lambda:self.copied())
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
    def copied(self):
        pyperclip.copy('The text to be copied to the clipboard.')
        self.error=Msg("Password has been copied").exec_()
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