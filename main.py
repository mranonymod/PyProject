import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5 import uic
from ui_functions import *
from PyQt5.uic import loadUi


# GUI FILE
Ui_Main,baseClass3=uic.loadUiType('main_menu.ui')

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(baseClass3):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)
        self.ui=Ui_Main()
        self.ui.setupUi(self)
        ## TOGGLE/BURGUER MENU
        ########################################################################
        
        self.ui.toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.Personal.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1_frame))

        # PAGE 2
        self.ui.Shared.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page2_frame))

        # PAGE 3
        self.ui.Banking.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page3_frame))
        