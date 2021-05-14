import sys
from PyQt5 import uic
from PyQt5.uic import loadUi
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QDialog

Ui_OTP,baseClass2=uic.loadUiType('UI/otp.ui')

class Otp(baseClass2):
    def __init__(self):
        super(Otp,self).__init__()
        #code start
        self.ui=Ui_OTP()
        self.ui.setupUi(self)
        self.ui.OkBtn.clicked.connect(self.accept)
        self.ui.CancelBtn.clicked.connect(self.reject)
    def ret(self):
        return(self.ui.AccText.text())
    @staticmethod
    def getOtp(parent = None):
        dialog = Otp()
        result = dialog.exec_()
        Account = dialog.ret()
        return (Account, result == QDialog.Accepted)