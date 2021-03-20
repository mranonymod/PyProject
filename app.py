import sys
import resources_rc
from PyQt5 import QtWidgets 
from PyQt5 import QtCore  
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.uic import loadUi
Ui_Form,baseClass=uic.loadUiType('Start.ui')
Ui_Register,baseClass2=uic.loadUiType('Register.ui')

class Start(baseClass):
    sw=QtCore.pyqtSignal()
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)
        #code start
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.RegisterButton.clicked.connect(self.closeW)
        #code end
    def closeW(self):
        self.sw.emit()
class Register(baseClass2):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)
        #code start
        self.ui=Ui_Register()
        self.ui.setupUi(self)
        #code end

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

