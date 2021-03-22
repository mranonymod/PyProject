import sys
import resources_rc
from PyQt5 import QtWidgets 
from PyQt5 import QtCore  
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.uic import loadUi
from validator import *

Ui_Register,baseClass2=uic.loadUiType('Register.ui')

class Register(baseClass2):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)
        #code start
        self.ui=Ui_Register()
        self.ui.setupUi(self)
        self.ui.RegisterButton.clicked.connect(self.verify)
        
        #code end
    def verify(self):
        if self.ui.NameText.text() and self.ui.UsernameText.text() and self.ui.PasswordText.text() and self.ui.ConfirmPasswordText.text() != "" :
            if self.ui.PasswordText.text() == self.ui.ConfirmPasswordText.text():
                if password_check(self.ui.PasswordText.text()):
                    print ("bete moj krdi wapas se")
            else:
                print ("password and confirm password fields should be same")
        else:
            print('Fill all the details')

                
    