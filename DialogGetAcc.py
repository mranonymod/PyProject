import sys
from PyQt5 import uic
from PyQt5.uic import loadUi
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QDialog

Ui_Other,baseClass2=uic.loadUiType('UI/accname.ui')

class Other(baseClass2):
    def __init__(self):
        super(Other,self).__init__()
        #code start
        self.ui=Ui_Other()
        self.ui.setupUi(self)
        self.ui.OkBtn.clicked.connect(self.accept)
        self.ui.CancelBtn.clicked.connect(self.reject)
    def ret(self):
        return(self.ui.AccText.text())
    @staticmethod
    def getAcc(parent = None):
        dialog = Other()
        result = dialog.exec_()
        Account = dialog.ret()
        return (Account, result == QDialog.Accepted)   