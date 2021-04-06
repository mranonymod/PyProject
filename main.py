import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QCoreApplication, QPropertyAnimation,Signal
from PySide2.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel,QInputDialog,QTableWidget

from PyQt5 import uic
from PyQt5.uic import loadUi

# GUI FILE
from ui_main_menu import Ui_MainWindow
from DialogMsg import Msg
from DialogPwd import Error2
from DialogGetAcc import Other
from UiViewPwdPers import PpwdView
from UiViewPwdSha import SpwdView
# IMPORT FUNCTIONS
from ui_functions import *
from DBaddpasswords import *
from DBAddShdU import *
from encrypt import AESCipher
from validator import *
from DBViewPwd import *
from generator import *


class MainWindow(QMainWindow):
    lw=Signal()
    def __init__(self,username):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.username = username
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.toggle.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 150, True))
        ## PAGES
        ########################################################################
        # PAGE 1
        self.ui.Personal.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Personal_Page))
        # PAGE 2
        self.ui.Shared.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Shared_Page))
        # PAGE 3
        self.ui.Banking.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Banking_Page))
        self.ui.Enter.clicked.connect(self.check)
        self.ui.Enter_2.clicked.connect(self.check2)
        self.ui.view_pwd.clicked.connect(self.viewPwd)
        self.ui.view_pwd_2.clicked.connect(self.viewPwd2)
        self.ui.another_pwd.clicked.connect(self.gen_pwd)
        self.ui.another_pwd_2.clicked.connect(self.gen_pwd2)
        self.ui.another_pwd_3.clicked.connect(self.gen_pwd3)
        self.AccSelectAdd()
        self.ui.Signout.clicked.connect(lambda : self.lw.emit())
    def check(self):
        if(self.ui.per_password.text() and self.ui.per_username.text() != ""):
            if(self.ui.AccSelect_2.currentText()!="Select"):
                if(password_check(self.ui.per_password.text())):
                    if(self.ui.checkBox.checkState()):
                        self.ppwd_add()
                    else:
                        self.check=Msg("Check The Box").exec_()
                else:
                    self.pError=Error2().exec_()
            else:
                self.fill=Msg("Select an Account").exec_()
        else:
            self.fill=Msg("Fill all the Details").exec_()
    def check2(self):
        if(self.ui.sha_password.text() and self.ui.sha_username.text() != ""):
            if(self.ui.AccSelect.currentText()!="Select"):
                if(password_check(self.ui.sha_password.text())):
                    if(self.ui.checkBox_2.checkState()):
                        self.spwd_add()
                    else:
                        self.check=Msg("Check The Box").exec_()
                else:
                    self.pError=Error2().exec_()
            else:
                self.fill=Msg("Select an Account").exec_()
        else:
            self.fill=Msg("Fill all the Details").exec_()
    
   
    def ppwd_add(self):
        self.Pwd=self.encrypt(self.ui.per_password.text())
        self.service=self.getItem()
        self.AccUsrName=self.ui.per_username.text()
        self.add=db(self.username)
        if(self.add.add(self.AccUsrName,self.Pwd,self.service)):
            self.ui.per_password.clear()
            self.ui.per_username.clear()
            self.success=Msg("Password Stored").exec_()
            self.AccSelectAdd()
        else:
            self.failed=Msg("Service already exists").exec_()
    def spwd_add(self):
        self.Pwd=self.encrypt(self.ui.sha_password.text())
        self.service=self.getItem2()
        self.UsrName=self.ui.sha_username.text()
        self.add=shd()
        if(self.add.share(self.UsrName,self.Pwd,self.service)):
            self.ui.sha_password.clear()
            self.ui.sha_username.clear()
            self.success=Msg("Password Stored").exec_()
        else:
            self.failed=Msg("Service already exists").exec_()
    
    def encrypt(self,str):
        self.key=db(self.username).getkey()
        self.str=str
        self.pwd=AESCipher(self.key)
        return self.pwd.encrypt(str)
    def decrypt(self,str):
        self.key=db(self.username).getkey()
        self.str=str
        self.pwd=AESCipher(self.key)
        return self.pwd.decrypt(str)
    def viewPwd(self):
        self.get=viewPers(self.username)
        if(self.get.find()):
            self.view=PpwdView(self.username)
            self.view.show()
        else:
            self.noUsr=Msg("No Passwords registered").exec_()
    def viewPwd2(self):
        self.get=shd()
        if(self.get.getPasses(self.username)):
            self.view=SpwdView(self.username)
            self.view.show()
        else:
            self.noUsr=Msg("No Passwords registered").exec_()
    def gen_pwd(self):
        self.pwdgen=genpwd()
        print(self.pwdgen)
        self.ui.per_password.setText(self.pwdgen)
    def gen_pwd2(self):
        self.pwdgen=genpwd()
        print(self.pwdgen)
        self.ui.sha_password.setText(self.pwdgen)
    def gen_pwd3(self):
        self.pwdgen=genpwd()
        print(self.pwdgen)
        self.ui.bank_pwd.setText(self.pwdgen)
    def getItem(self):
        print("here")
        self.content = self.ui.AccSelect_2.currentText()
        print(self.content)
        if(self.content=="Other"):
#text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter text:')
            self.content, ok = Other.getAcc(self)
            self.ui.AccSelect_2.addItem(self.content)
            return self.content
        elif(self.content=="Select"):
            return False
        else:
            return self.content
    def getItem2(self):
        print("here")
        self.content = self.ui.AccSelect.currentText()
        print(self.content)
        if(self.content=="Select"):
            return False
        else:
            return self.content
    def AccSelectAdd(self):
        self.ui.AccSelect.clear()
        self.ui.AccSelect_2.clear()
        self.ui.AccSelect.addItem("Select")
        self.ui.AccSelect_2.addItems(["Select","Other"])
        a=len(db(self.username).getServices())
        for y in range(a):
            if(a!=0):
                self.s="".join(db(self.username).getServices()[y])
                self.ui.AccSelect_2.addItem(self.s)
        z=len(db(self.username).getServicesU())
        for x in range(z):
            if(z!=0):
                self.s1="".join(db(self.username).getServicesU()[x])
                self.ui.AccSelect.addItem(self.s1)

"""for row in self.get.find():
print(row[0])
print(row[1])
print(row[2])
print(row[3])
print(row[4])
print(self.decrypt(row[5]))
print(row[6])"""