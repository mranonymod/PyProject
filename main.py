import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime)
from PySide2.QtWidgets import QMainWindow,QTableWidget
from PySide2.QtWidgets import QLabel

from PyQt5 import uic
from PyQt5.uic import loadUi

# GUI FILE
from ui_main_menu import Ui_MainWindow
from MsgDialog import Msg
from PwdDialog import Error2

# IMPORT FUNCTIONS
from ui_functions import *
from addpasswordsDB import *
from encrypt import AESCipher
from validator import *
from ViewPwdDB import *


class MainWindow(QMainWindow):
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
        self.ui.view_pwd.clicked.connect(self.viewPwd)
        self.tableWidget = QTableWidget()

    def check(self):
        if(self.ui.per_password.text() and self.ui.per_Acc_name.text() and self.ui.per_username.text() != ""):
            if(password_check(self.ui.per_password.text())):
                if(self.ui.checkBox.checkState()):
                    self.ppwd_add()
                else:
                    self.check=Msg("Check The Box").exec_()
            else:
                self.pError=Error2().exec_()
        else:
            self.fill=Msg("Fill all the Details").exec_()
    def ppwd_add(self):
        self.Pwd=self.encrypt(self.ui.per_password.text())
        self.service=self.ui.per_Acc_name.text()
        self.AccUsrName=self.ui.per_username.text()
        self.add=db(self.username)
        if(self.add.add(self.AccUsrName,self.Pwd,self.service)):
            self.ui.per_password.clear()
            self.ui.per_Acc_name.clear()
            self.ui.per_username.clear()
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
            for row in self.get.find():
                print(row[0])
                print(row[1])
                print(row[2])
                print(row[3])
                print(row[4])
                print(self.decrypt(row[5]))
                print(row[6])

        else:
            self.noUsr=Msg("No Passwords registered").exec_()
    


