import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc 
from PyQt5 import QtGui as qtg 
from PyQt5 import uic
from PyQt5.uic import loadUi
Ui_Start,baseClass=uic.loadUiType('Start.ui')
Ui_Login,baseClass2=uic.loadUiType('Login.ui')

class MainW(baseClass):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        #code start
        self.ui=Ui_Start()
        self.ui.setupUi(self)
        self.ui.LoginB.clicked.connect(lambda : self.LnW())
        #code end
        self.show()
    def LnW(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        #code start
        loadUi("Login.ui",self)
        self.ui=Ui_Login()
        self.ui.setupUi(self)
        self.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w=MainW(windowTitle='hello')
    sys.exit(app.exec_())



