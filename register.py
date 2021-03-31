import sys
import resources_rc
from PyQt5 import QtWidgets 
from PyQt5 import QtCore  
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.uic import loadUi
from registerdb import *
from hasher import *
from validator import *

Ui_Register,baseClass=uic.loadUiType('Register.ui')
Ui_Error2,baseClass2=uic.loadUiType('ErrorTemplates/PassDet.ui')
Ui_Msg,baseClass1=uic.loadUiType('ErrorTemplates/Message.ui')
class Register(baseClass):
    sw=QtCore.pyqtSignal()
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)
        #code start
        self.ui=Ui_Register()
        self.ui.setupUi(self)
        self.ui.RegisterButton.clicked.connect(self.verify)
        self.ui.BackBtn.clicked.connect(lambda: self.sw.emit())
        
        #code end
    def verify(self):
        if self.ui.NameText.text() and self.ui.UsernameText.text() and self.ui.PasswordText.text() and self.ui.ConfirmPasswordText.text() != "" :
            if self.ui.PasswordText.text() == self.ui.ConfirmPasswordText.text():
                if password_check(self.ui.PasswordText.text()):
                    email=self.ui.UsernameText.text()+"@gmail.com"
                    password=hashit(self.ui.PasswordText.text())
                    self.i=Reg(self.ui.UsernameText.text(),self.ui.NameText.text(),email,password)
                    if(self.i.insert()):
                        self.success=Msg("Registration successful").exec_()
                        self.sw.emit()
                    else:
                        self.failed=Msg("Username already in use").exec_()
                    
                else:
                    self.passdet=Error2().exec_()
            else:
                self.cnfpass=Msg("Passwords do not match").exec_()
        else:
            self.empty=Msg("Fill all the fields").exec_()


class Error2(baseClass2):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)
        #code start
        self.ui=Ui_Error2()
        self.ui.setupUi(self)
        self.ui.OkBtn.clicked.connect(self.done)
        self.ui.CancelBtn.clicked.connect(self.done)
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
    