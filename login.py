import sys
import resources_rc
from PyQt5 import QtWidgets 
from PyQt5 import QtCore  
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.uic import loadUi
from logindb import *
from hasher import *
from gplus import *

Ui_Form,baseClass=uic.loadUiType('Start.ui')
Ui_Msg,baseClass1=uic.loadUiType('ErrorTemplates/Message.ui')
class Start(baseClass):
    rw=QtCore.pyqtSignal()
    mw=QtCore.pyqtSignal(str)
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
            self.mw.emit(self.ui.UsernameText.text())
        else:
            self.error=Msg("Username or Password incorrect").exec_()
    def gplogin(self):
        self.log=glogin()
        self.close()
        self.label.setText("haa yeh bhi kr lete hai")
        self.label.show()
        print("bruh")
    def register(self):
        self.rw.emit()

class Msg(baseClass1):
    def __init__(self, str):
        super(Msg,self).__init__()
        #code start
        self.str = str
        self.ui=Ui_Msg()
        self.ui.setupUi(self)
        self.ui.OkBtn.clicked.connect(self.done)
        self.ui.CancelBtn.clicked.connect(self.done)
        self.ui.Err_msg.setText(self.str)

        