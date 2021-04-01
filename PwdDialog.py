from PyQt5 import uic
from PyQt5.uic import loadUi

Ui_Error2,baseClass2=uic.loadUiType('ErrorTemplates/PassDet.ui')

class Error2(baseClass2):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)
        #code start
        self.ui=Ui_Error2()
        self.ui.setupUi(self)
        self.ui.OkBtn.clicked.connect(self.done)
        self.ui.CancelBtn.clicked.connect(self.done)