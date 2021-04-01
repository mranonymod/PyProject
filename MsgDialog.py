from PyQt5 import uic
from PyQt5.uic import loadUi

Ui_Message,baseClass2=uic.loadUiType('ErrorTemplates/Message.ui')

class Msg(baseClass2):
    def __init__(self, str):
        super(Msg,self).__init__()
        #code start
        self.ui=Ui_Message()
        self.ui.setupUi(self)
        self.ui.OkBtn.clicked.connect(self.done)
        self.ui.CancelBtn.clicked.connect(self.done)
        self.str=str
        self.ui.Err_msg.setText(self.str)