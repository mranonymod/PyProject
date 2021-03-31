import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QLabel

from PyQt5 import uic
from PyQt5.uic import loadUi

# GUI FILE
from ui_main_menu import Ui_MainWindow
Ui_Success,baseClass4=uic.loadUiType('ErrorTemplates/Message.ui')

# IMPORT FUNCTIONS
from ui_functions import *
from addpasswordsDB import *
from encrypt import AESCipher


class MainWindow(QMainWindow):
    def __init__(self,username):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.username = username

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.toggle.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 150, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.Personal.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Personal_Page))

        # PAGE 2
        self.ui.Shared.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Shared_Page))

        # PAGE 3
        self.ui.Banking.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Banking_Page))

        self.ui.Enter.clicked.connect(self.check)

    def check(self):
        if(self.ui.checkBox.checkState()):
            self.ppwd_add()
        else:
            self.l4 = QLabel()
            self.l4.setText("check the box")
            self.l4.show()
    def ppwd_add(self):
        self.Pwd=self.encrypt(self.ui.per_password.text())
        self.service=self.ui.per_Acc_name.text()
        self.AccUsrName=self.ui.per_username.text()
        self.add=db(self.username)
        if(self.add.add(self.AccUsrName,self.Pwd,self.service)):
            self.ui.per_password.clear()
            self.ui.per_Acc_name.clear()
            self.ui.per_username.clear()
            self.success=Success().exec_()
        else:
            self.failed=Failed().exec_()

    def encrypt(self,str):
        self.key=db(self.username).getkey()
        self.str=str
        self.pwd=AESCipher(self.key)
        return self.pwd.encrypt(str)


class Success(baseClass4):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)
        #code start
        self.ui=Ui_Success()
        self.ui.setupUi(self)
        self.ui.OkBtn.clicked.connect(self.done)
        self.ui.CancelBtn.clicked.connect(self.done)

class Failed(baseClass4):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)
        #code start
        self.ui=Ui_Success()
        self.ui.setupUi(self)
        self.ui.OkBtn.clicked.connect(self.done)
        self.ui.CancelBtn.clicked.connect(self.done)
        



