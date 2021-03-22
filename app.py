import sys
import resources_rc
from PyQt5 import QtWidgets 
from PyQt5 import QtCore  
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.uic import loadUi
from register import Register
from encrypt import *
Ui_Form,baseClass=uic.loadUiType('Start.ui')

class Start(baseClass):
    sw=QtCore.pyqtSignal()
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
        self.username=enc(self.ui.UsernameText.text())
        self.username.check()
        self.password=enc(self.ui.PasswordText.text())
        self.password.check()

    def gplogin(self):
        self.close()
        self.label.setText("haa yeh bhi kr lete hai")
        self.label.show()
        print("bruh")
    def register(self):
        self.sw.emit()


class Controller:

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)
    def show_start(self):
        self.window=Start(windowTitle='Choose')
        self.window.sw.connect(self.show_register)
        self.window.show()
    def show_register(self):
        self.reg = Register()
        self.window.close()
        self.reg.show()
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    w=Controller()
    w.show_start()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

