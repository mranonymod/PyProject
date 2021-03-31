import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_main_menu import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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



