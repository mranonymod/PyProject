import sys
import resources_rc
from PyQt5 import QtWidgets 
from PyQt5 import QtCore  
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.uic import loadUi
from logindb import *
from hasher import *

Ui_Form,baseClass=uic.loadUiType('Start.ui')

class Start(baseClass):
    rw=QtCore.pyqtSignal()
    mw=QtCore.pyqtSignal()
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)
        #code start
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.label=QtWidgets.QLabel('bruh')
        self.ui.LoginButton.clicked.connect(self.login)
        self.ui.RegisterButton.clicked.connect(self.register)
        self.ui.GPButton.clicked.connect(self.gplogin)
        #code end
    def login(self):
        logincheck=getdbpwd(self.ui.UsernameText.text(),hashit(self.ui.PasswordText.text())).check()
        if(logincheck):
            self.mw.emit()
        else:
            print("wrong password/username ")
    def gplogin(self):
        self.close()
        self.label.setText("haa yeh bhi kr lete hai")
        self.label.show()
        print("bruh")
    def register(self):
        self.rw.emit()