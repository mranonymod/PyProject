import sys
import resources_rc
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore  
from PyQt5 import QtGui as qtg 
from PyQt5 import uic
from PyQt5.uic import loadUi
Ui_Start,baseClass=uic.loadUiType('Start.ui')
Ui_Login,baseClass2=uic.loadUiType('Login.ui')

class Start(baseClass):
    sw=QtCore.pyqtSignal()
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)
        #code start
        self.ui=Ui_Start()
        self.ui.setupUi(self)
        #code end
    def closeW(self):
        self.sw.emit()
class Login(baseClass2):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)
        #code start
        self.ui=Ui_Login()
        self.ui.setupUi(self)
        #code end

class Controller:

    def __init__(self):
        pass 
    def show_start(self):
        self.window=Start(windowTitle='Choose')
        self.window.sw.connect(self.show_login)
        self.window.show()
    def show_login(self):
        self.login = Login()
        self.window.close()
        self.login.show()
        
def main():
    app = qtw.QApplication(sys.argv)
    w=Controller()
    w.show_start()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

