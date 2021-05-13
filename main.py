import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, QPropertyAnimation,pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel,QInputDialog,QTableWidget
from qrcode import *

from PyQt5 import uic
from PyQt5.uic import loadUi

# GUI FILE
from ui_main_menu import Ui_MainWindow
from DialogMsg import Msg
from DialogPwd import Error2
from DialogGetAcc import Other
from UiViewPwdPers import PpwdView
from UiViewPwdSha import SpwdView
from UiViewSharedUsers import SusrView
# IMPORT FUNCTIONS'
from qrdet import *
from ui_functions import *
from DBaddpasswords import *
from DBAddShdU import *
from encrypt import AESCipher
from validator import *
from DBViewPwd import *
from generator import *


class MainWindow(QMainWindow):
    lw=pyqtSignal()
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
        self.ui.AddUser.clicked.connect(self.check2)
        self.ui.DeleteUser.clicked.connect(self.check3)
        self.ui.qr.clicked.connect(self.check4)
        self.ui.view_pwd.clicked.connect(self.viewPwd)
        self.ui.ViewShaPwd.clicked.connect(self.viewPwd2)
        self.ui.ViewUsers.clicked.connect(self.viewUsers)
        self.ui.another_pwd.clicked.connect(self.gen_pwd)
        self.ui.another_pwd_3.clicked.connect(self.gen_pwd3)
        self.ui.qr_2.clicked.connect(self.qrcheck)
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
        if(self.ui.sha_username.text() != ""):
            if(self.ui.AccSelect.currentText()!="Select"):
                    if(self.ui.checkBox_2.checkState()):
                        self.spwd_add()
                    else:
                        self.check=Msg("Check The Box").exec_()
            else:
                self.fill=Msg("Select an Account").exec_()
        else:
            self.fill=Msg("Fill all the Details").exec_()

    def check3(self):
        if(self.ui.sha_username.text() != ""):
            if(self.ui.AccSelect.currentText()!="Select"):
                    if(self.ui.checkBox_2.checkState()):
                        self.spwd_del()
                    else:
                        self.check=Msg("Check The Box").exec_()
            else:
                self.fill=Msg("Select an Account").exec_()
        else:
            self.fill=Msg("Fill all the Details").exec_()
    
    def check4(self):
        if(self.ui.AccSelect.currentText()!="Select"):
            if(self.ui.checkBox_2.checkState()):
                self.qrgen()
            else:
                self.check=Msg("Check The Box").exec_()
        else:
            self.fill=Msg("Select an Account").exec_()
    def ppwd_add(self):
        self.Pwd=self.encrypt(self.ui.per_password.text())
        self.service=self.getItem()
        self.AccUsrName=self.ui.per_username.text()
        self.shdid=genpwd()
        self.add=db(self.username)
        if(self.add.add(self.AccUsrName,self.Pwd,self.service,self.shdid)):
            self.ui.per_password.clear()
            self.ui.per_username.clear()
            self.success=Msg("Password Stored").exec_()
            self.AccSelectAdd()
        else:
            self.failed=Msg("Service already exists").exec_()

    def spwd_add(self):
        self.service=self.getItem2()
        self.UsrName=self.ui.sha_username.text()
        self.add=shd()
        if(self.add.share(self.username,self.UsrName,self.service)):
            self.ui.sha_username.clear()
            self.success=Msg("Password Shared").exec_()
        else:
            self.failed=Msg("User does not exist").exec_()

    def spwd_del(self):
        self.service=self.getItem2()
        self.UsrName=self.ui.sha_username.text()
        self.add=shd()
        if(self.add.unshare(self.username,self.UsrName,self.service)):
            self.ui.sha_username.clear()
            self.success=Msg("Password Unshared").exec_()
        else:
            self.failed=Msg("User does not exist").exec_()
    def qrgen(self):
        self.service=self.getItem2()
        self.qr1=shd()
        self.sid=self.qr1.qr1(self.username,self.service)
        genqr(self.sid)
        Msg("QR Generated").exec()
    def qrcheck(self):
        self.shdid1=qrdet()
        self.ad=shd()
        if(self.ad.qrsh(self.shdid1,self.username)):
            Msg("Password Added").exec()
        else:
            Msg("Can't Share To Yourself").exec()

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

    def viewUsers(self):
        self.get=viewShd(self.username)
        if(self.get.getusers()):
            self.view=SusrView(self.username)
            self.view.show()
        else:
            self.noUsr=Msg("No Passwords shared").exec_()
    def gen_pwd(self):
        self.pwdgen=genpwd()
        self.ui.per_password.setText(self.pwdgen)
    def gen_pwd2(self):
        self.pwdgen=genpwd()
        self.ui.sha_password.setText(self.pwdgen)
    def gen_pwd3(self):
        self.pwdgen=genpwd()
        self.ui.bank_pwd.setText(self.pwdgen)
    def getItem(self):
        self.content = self.ui.AccSelect_2.currentText()
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
        self.content = self.ui.AccSelect.currentText()
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