# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menufXHCIL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1062, 603)
        MainWindow.setStyleSheet(u"*{\n"
                                 "font-family: 'Open Sans', sans-serif;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
                                         "color:#fff2;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMaximumSize(QSize(16777215, 45))
        self.main_header.setStyleSheet(u"")
        self.main_header.setFrameShape(QFrame.StyledPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_bar_container = QFrame(self.main_header)
        self.title_bar_container.setObjectName(u"title_bar_container")
        self.title_bar_container.setFrameShape(QFrame.StyledPanel)
        self.title_bar_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.title_bar_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle = QFrame(self.title_bar_container)
        self.left_menu_toggle.setObjectName(u"left_menu_toggle")
        self.left_menu_toggle.setMinimumSize(QSize(50, 0))
        self.left_menu_toggle.setMaximumSize(QSize(50, 16777215))
        self.left_menu_toggle.setStyleSheet(u"")
        self.left_menu_toggle.setFrameShape(QFrame.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggle = QPushButton(self.left_menu_toggle)
        self.toggle.setObjectName(u"toggle")
        self.toggle.setMinimumSize(QSize(0, 0))
        self.toggle.setMaximumSize(QSize(50, 16777215))
        self.toggle.setStyleSheet(u"QFrame{\n"
                                  "background-color: rgb(35, 35, 35);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton{\n"
                                  "padding:5px 10px;\n"
                                  "border:none;\n"
                                  "\n"
                                  "background-color:transparent;\n"
                                  "color:#fff;\n"
                                  "\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:rgb(85,255,255);\n"
                                  "}\n"
                                  "")
        icon = QIcon()
        icon.addFile(u"images/Menu.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.toggle.setIcon(icon)
        self.toggle.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.toggle)

        self.horizontalLayout_5.addWidget(self.left_menu_toggle)

        self.title_bar = QFrame(self.title_bar_container)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.title_bar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(770, 0, 101, 41))
        self.label_4.setStyleSheet(u"color:#fffff2;\n"
                                   "font-family:'Open Sans', sans-serif;\n"
                                   "font-size:30px;")

        self.horizontalLayout_5.addWidget(self.title_bar)

        self.horizontalLayout_2.addWidget(self.title_bar_container)

        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMinimumSize(QSize(0, 0))
        self.left_side_menu.setMaximumSize(QSize(50, 16777215))
        self.left_side_menu.setStyleSheet(u"QFrame{\n"
                                          "background-color: rgb(35, 35, 35);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton{\n"
                                          "padding:5px 10px;\n"
                                          "border:none;\n"
                                          "border-bottom:1px solid;\n"
                                          "\n"
                                          "background-color:transparent;\n"
                                          "color:#fff;\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "background-color:rgb(85,255,255);\n"
                                          "\n"
                                          "}")
        self.left_side_menu.setFrameShape(QFrame.StyledPanel)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(11, 0, 0, 0)
        self.left_menu_top_buttons = QFrame(self.left_side_menu)
        self.left_menu_top_buttons.setObjectName(u"left_menu_top_buttons")
        self.left_menu_top_buttons.setFrameShape(QFrame.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QFrame.Raised)
        self.Shared = QPushButton(self.left_menu_top_buttons)
        self.Shared.setObjectName(u"Shared")
        self.Shared.setGeometry(QRect(0, 90, 141, 91))
        self.Shared.setMinimumSize(QSize(100, 0))
        self.Shared.setStyleSheet(u"background-image: url(images/Shared.png);\n"
                                  "background-repeat:none;\n"
                                  "padding-left:30px;\n"
                                  "background-position:center left;")
        self.Personal = QPushButton(self.left_menu_top_buttons)
        self.Personal.setObjectName(u"Personal")
        self.Personal.setGeometry(QRect(0, 0, 141, 91))
        self.Personal.setMinimumSize(QSize(0, 0))
        self.Personal.setStyleSheet(u"background-image: url(images/personal.png);\n"
                                    "background-repeat:none;\n"
                                    "padding-left:30px;\n"
                                    "background-position:center left;")
        self.Banking = QPushButton(self.left_menu_top_buttons)
        self.Banking.setObjectName(u"Banking")
        self.Banking.setGeometry(QRect(0, 180, 141, 91))
        self.Banking.setMinimumSize(QSize(100, 0))
        self.Banking.setStyleSheet(u"background-image: url(images/banking.png);\n"
                                   "background-repeat:none;\n"
                                   "padding-left:30px;\n"
                                   "background-position:center left;")
        self.Signout = QPushButton(self.left_menu_top_buttons)
        self.Signout.setObjectName(u"Signout")
        self.Signout.setGeometry(QRect(0, 450, 141, 91))
        self.Signout.setStyleSheet(u"background-image: url(images/exit.png);\n"
                                   "background-repeat:none;\n"
                                   "padding-left:30px;\n"
                                   "background-position:center left;")

        self.verticalLayout_2.addWidget(self.left_menu_top_buttons)

        self.horizontalLayout.addWidget(self.left_side_menu)

        self.center_side_menu = QFrame(self.main_body)
        self.center_side_menu.setObjectName(u"center_side_menu")
        self.center_side_menu.setStyleSheet(
            u"background-color: rgb(75, 75, 75);")
        self.center_side_menu.setFrameShape(QFrame.StyledPanel)
        self.center_side_menu.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.center_side_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -1, 1021, 581))
        self.Personal_Page = QWidget()
        self.Personal_Page.setObjectName(u"Personal_Page")
        self.page1_frame = QFrame(self.Personal_Page)
        self.page1_frame.setObjectName(u"page1_frame")
        self.page1_frame.setGeometry(QRect(-1, -1, 1021, 571))
        self.page1_frame.setStyleSheet(u"#page1_frame{\n"
                                       "	\n"
                                       "	background-image: url(images/blusky.jpg);\n"
                                       "}")
        self.page1_frame.setFrameShape(QFrame.StyledPanel)
        self.page1_frame.setFrameShadow(QFrame.Raised)
        self.PasswordBox = QFrame(self.page1_frame)
        self.PasswordBox.setObjectName(u"PasswordBox")
        self.PasswordBox.setGeometry(QRect(20, 30, 871, 501))
        self.PasswordBox.setStyleSheet(u"QLineEdit{\n"
                                       "background:transparent;\n"
                                       "border:none;\n"
                                       "font-size:20px;\n"
                                       "color:#717072;\n"
                                       "border-bottom:1px solid #717072;\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "QFrame{\n"
                                       "background-color: rgb(30, 40, 51) ;\n"
                                       "font-size:23px;\n"
                                       "border-radius:40px;\n"
                                       "color:#fffff2;\n"
                                       "}\n"
                                       "QPushButton{\n"
                                       "background:#1df2ef;\n"
                                       "font-size:18px;\n"
                                       "border-radius:15px;\n"
                                       "color:black;}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "background:#fffff2;\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.PasswordBox.setFrameShape(QFrame.StyledPanel)
        self.PasswordBox.setFrameShadow(QFrame.Raised)
        self.Passwordtext = QLabel(self.PasswordBox)
        self.Passwordtext.setObjectName(u"Passwordtext")
        self.Passwordtext.setGeometry(QRect(40, 0, 281, 81))
        self.Passwordtext.setStyleSheet(u"font-size:25px;\n"
                                        "")
        self.per_Acc_name = QLineEdit(self.PasswordBox)
        self.per_Acc_name.setObjectName(u"per_Acc_name")
        self.per_Acc_name.setGeometry(QRect(230, 100, 531, 41))
        self.per_username = QLineEdit(self.PasswordBox)
        self.per_username.setObjectName(u"per_username")
        self.per_username.setGeometry(QRect(230, 170, 531, 41))
        self.per_password = QLineEdit(self.PasswordBox)
        self.per_password.setObjectName(u"per_password")
        self.per_password.setGeometry(QRect(230, 250, 531, 41))
        self.per_password.setEchoMode(QLineEdit.Password)
        self.Enter = QPushButton(self.PasswordBox)
        self.Enter.setObjectName(u"Enter")
        self.Enter.setGeometry(QRect(360, 400, 180, 40))
        self.checkBox = QCheckBox(self.PasswordBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(250, 320, 511, 20))
        self.checkBox.setStyleSheet(u"background-color:transparent;\n"
                                    "color:#fffff2;\n"
                                    "font-size:15px;")
        self.label = QLabel(self.PasswordBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 110, 151, 31))
        self.label.setStyleSheet(u"font-size:20px;")
        self.label_2 = QLabel(self.PasswordBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 180, 121, 31))
        self.label_2.setStyleSheet(u"font-size:20px;")
        self.label_3 = QLabel(self.PasswordBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 260, 121, 31))
        self.label_3.setStyleSheet(u"font-size:20px;")
        self.view_pwd = QPushButton(self.PasswordBox)
        self.view_pwd.setObjectName(u"view_pwd")
        self.view_pwd.setGeometry(QRect(620, 400, 180, 40))
        self.view_pwd.setStyleSheet(u"#view_pwd{\n"
                                    "background-color:#DB4437;\n"
                                    "}\n"
                                    "#view_pwd:hover{\n"
                                    "background-color:#fffff2;}")
        self.another_pwd = QPushButton(self.PasswordBox)
        self.another_pwd.setObjectName(u"another_pwd")
        self.another_pwd.setGeometry(QRect(60, 400, 211, 40))
        self.stackedWidget.addWidget(self.Personal_Page)
        self.Shared_Page = QWidget()
        self.Shared_Page.setObjectName(u"Shared_Page")
        self.tempframe = QFrame(self.Shared_Page)
        self.tempframe.setObjectName(u"tempframe")
        self.tempframe.setGeometry(QRect(-1, -1, 1021, 561))
        self.tempframe.setFrameShape(QFrame.StyledPanel)
        self.tempframe.setFrameShadow(QFrame.Raised)
        self.page2_frame = QFrame(self.tempframe)
        self.page2_frame.setObjectName(u"page2_frame")
        self.page2_frame.setGeometry(QRect(0, 0, 1021, 571))
        self.page2_frame.setStyleSheet(u"#page2_frame{\n"
                                       "	background-image: url(images/blusky.jpg);\n"
                                       "}")
        self.page2_frame.setFrameShape(QFrame.StyledPanel)
        self.page2_frame.setFrameShadow(QFrame.Raised)
        self.PasswordBox_2 = QFrame(self.page2_frame)
        self.PasswordBox_2.setObjectName(u"PasswordBox_2")
        self.PasswordBox_2.setGeometry(QRect(20, 30, 871, 501))
        self.PasswordBox_2.setStyleSheet(u"QLineEdit{\n"
                                         "background:transparent;\n"
                                         "border:none;\n"
                                         "font-size:20px;\n"
                                         "color:#717072;\n"
                                         "border-bottom:1px solid #717072;\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QFrame{\n"
                                         "background-color: rgb(30, 40, 51) ;\n"
                                         "font-size:23px;\n"
                                         "border-radius:40px;\n"
                                         "color:#fffff2;\n"
                                         "}\n"
                                         "QPushButton{\n"
                                         "background:#1df2ef;\n"
                                         "font-size:18px;\n"
                                         "border-radius:15px;\n"
                                         "color:black;}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background:#fffff2;\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.PasswordBox_2.setFrameShape(QFrame.StyledPanel)
        self.PasswordBox_2.setFrameShadow(QFrame.Raised)
        self.Passwordtext_2 = QLabel(self.PasswordBox_2)
        self.Passwordtext_2.setObjectName(u"Passwordtext_2")
        self.Passwordtext_2.setGeometry(QRect(40, 0, 281, 81))
        self.Passwordtext_2.setStyleSheet(u"font-size:25px;\n"
                                          "")
        self.sha_acc_name = QLineEdit(self.PasswordBox_2)
        self.sha_acc_name.setObjectName(u"sha_acc_name")
        self.sha_acc_name.setGeometry(QRect(230, 100, 531, 41))
        self.sha_username = QLineEdit(self.PasswordBox_2)
        self.sha_username.setObjectName(u"sha_username")
        self.sha_username.setGeometry(QRect(230, 170, 531, 41))
        self.sha_password = QLineEdit(self.PasswordBox_2)
        self.sha_password.setObjectName(u"sha_password")
        self.sha_password.setGeometry(QRect(230, 250, 531, 41))
        self.sha_password.setEchoMode(QLineEdit.Password)
        self.Enter_2 = QPushButton(self.PasswordBox_2)
        self.Enter_2.setObjectName(u"Enter_2")
        self.Enter_2.setGeometry(QRect(360, 400, 180, 40))
        self.checkBox_2 = QCheckBox(self.PasswordBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(250, 320, 511, 20))
        self.checkBox_2.setStyleSheet(u"background-color:transparent;\n"
                                      "color:#fffff2;\n"
                                      "font-size:15px;")
        self.label_5 = QLabel(self.PasswordBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 110, 151, 31))
        self.label_5.setStyleSheet(u"font-size:20px;")
        self.label_6 = QLabel(self.PasswordBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 180, 121, 31))
        self.label_6.setStyleSheet(u"font-size:20px;")
        self.label_7 = QLabel(self.PasswordBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 260, 121, 31))
        self.label_7.setStyleSheet(u"font-size:20px;")
        self.view_pwd_2 = QPushButton(self.PasswordBox_2)
        self.view_pwd_2.setObjectName(u"view_pwd_2")
        self.view_pwd_2.setGeometry(QRect(620, 400, 180, 40))
        self.view_pwd_2.setStyleSheet(u"#view_pwd_2{\n"
                                      "background-color:#DB4437;\n"
                                      "}\n"
                                      "#view_pwd_2:hover{\n"
                                      "background-color:#fffff2;}")
        self.another_pwd_2 = QPushButton(self.PasswordBox_2)
        self.another_pwd_2.setObjectName(u"another_pwd_2")
        self.another_pwd_2.setGeometry(QRect(60, 400, 211, 40))
        self.stackedWidget.addWidget(self.Shared_Page)
        self.Banking_Page = QWidget()
        self.Banking_Page.setObjectName(u"Banking_Page")
        self.tempframe2 = QFrame(self.Banking_Page)
        self.tempframe2.setObjectName(u"tempframe2")
        self.tempframe2.setGeometry(QRect(-1, -1, 1021, 561))
        self.tempframe2.setFrameShape(QFrame.StyledPanel)
        self.tempframe2.setFrameShadow(QFrame.Raised)
        self.page3_frame = QFrame(self.tempframe2)
        self.page3_frame.setObjectName(u"page3_frame")
        self.page3_frame.setGeometry(QRect(0, -10, 1021, 571))
        self.page3_frame.setStyleSheet(u"#page3_frame{\n"
                                       "	background-image: url(images/blusky.jpg);\n"
                                       "\n"
                                       "}")
        self.page3_frame.setFrameShape(QFrame.StyledPanel)
        self.page3_frame.setFrameShadow(QFrame.Raised)
        self.PasswordBox_3 = QFrame(self.page3_frame)
        self.PasswordBox_3.setObjectName(u"PasswordBox_3")
        self.PasswordBox_3.setGeometry(QRect(20, 40, 871, 501))
        self.PasswordBox_3.setStyleSheet(u"QLineEdit{\n"
                                         "background:transparent;\n"
                                         "border:none;\n"
                                         "font-size:20px;\n"
                                         "color:#717072;\n"
                                         "border-bottom:1px solid #717072;\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QFrame{\n"
                                         "background-color: rgb(30, 40, 51) ;\n"
                                         "font-size:23px;\n"
                                         "border-radius:40px;\n"
                                         "color:#fffff2;\n"
                                         "}\n"
                                         "QPushButton{\n"
                                         "background:#1df2ef;\n"
                                         "font-size:18px;\n"
                                         "border-radius:15px;\n"
                                         "color:black;}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background:#fffff2;\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.PasswordBox_3.setFrameShape(QFrame.StyledPanel)
        self.PasswordBox_3.setFrameShadow(QFrame.Raised)
        self.Passwordtext_3 = QLabel(self.PasswordBox_3)
        self.Passwordtext_3.setObjectName(u"Passwordtext_3")
        self.Passwordtext_3.setGeometry(QRect(40, 0, 281, 81))
        self.Passwordtext_3.setStyleSheet(u"font-size:25px;\n"
                                          "")
        self.Bank_AccNo = QLineEdit(self.PasswordBox_3)
        self.Bank_AccNo.setObjectName(u"Bank_AccNo")
        self.Bank_AccNo.setGeometry(QRect(230, 100, 531, 41))
        self.bank_custID = QLineEdit(self.PasswordBox_3)
        self.bank_custID.setObjectName(u"bank_custID")
        self.bank_custID.setGeometry(QRect(230, 170, 531, 41))
        self.bank_pwd = QLineEdit(self.PasswordBox_3)
        self.bank_pwd.setObjectName(u"bank_pwd")
        self.bank_pwd.setGeometry(QRect(230, 250, 531, 41))
        self.bank_pwd.setEchoMode(QLineEdit.Password)
        self.Enter_3 = QPushButton(self.PasswordBox_3)
        self.Enter_3.setObjectName(u"Enter_3")
        self.Enter_3.setGeometry(QRect(360, 400, 180, 40))
        self.checkBox_3 = QCheckBox(self.PasswordBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(250, 320, 511, 20))
        self.checkBox_3.setStyleSheet(u"background-color:transparent;\n"
                                      "color:#fffff2;\n"
                                      "font-size:15px;")
        self.label_8 = QLabel(self.PasswordBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 110, 151, 31))
        self.label_8.setStyleSheet(u"font-size:20px;")
        self.label_9 = QLabel(self.PasswordBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 180, 121, 31))
        self.label_9.setStyleSheet(u"font-size:20px;")
        self.label_10 = QLabel(self.PasswordBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(70, 260, 121, 31))
        self.label_10.setStyleSheet(u"font-size:20px;")
        self.view_pwd_3 = QPushButton(self.PasswordBox_3)
        self.view_pwd_3.setObjectName(u"view_pwd_3")
        self.view_pwd_3.setGeometry(QRect(620, 400, 180, 40))
        self.view_pwd_3.setStyleSheet(u"#view_pwd_3{\n"
                                      "background-color:#DB4437;\n"
                                      "}\n"
                                      "#view_pwd_3:hover{\n"
                                      "background-color:#fffff2;}")
        self.another_pwd_3 = QPushButton(self.PasswordBox_3)
        self.another_pwd_3.setObjectName(u"another_pwd_3")
        self.another_pwd_3.setGeometry(QRect(60, 400, 211, 40))
        self.stackedWidget.addWidget(self.Banking_Page)

        self.horizontalLayout.addWidget(self.center_side_menu)

        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.toggle.setText("")
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Protekt", None))
        self.Shared.setText(QCoreApplication.translate(
            "MainWindow", u"Shared", None))
        self.Personal.setText(QCoreApplication.translate(
            "MainWindow", u"Personal", None))
        self.Banking.setText(QCoreApplication.translate(
            "MainWindow", u"Banking", None))
        self.Signout.setText(QCoreApplication.translate(
            "MainWindow", u"Sign-Out", None))
        self.Passwordtext.setText(QCoreApplication.translate(
            "MainWindow", u"Personal Passwords", None))
        self.per_Acc_name.setText("")
        self.per_Acc_name.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"AppName/Website", None))
        self.per_username.setText("")
        self.per_username.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"UserName/E-Mail", None))
        self.per_password.setText("")
        self.per_password.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Password", None))
        self.Enter.setText(QCoreApplication.translate(
            "MainWindow", u"Enter", None))
        self.checkBox.setText(QCoreApplication.translate(
            "MainWindow", u"I hereby confirm all the details entered are correct.", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Account Name:", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Username:", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Password:", None))
        self.view_pwd.setText(QCoreApplication.translate(
            "MainWindow", u"View Passwords", None))
        self.another_pwd.setText(QCoreApplication.translate(
            "MainWindow", u"Add Another Password", None))
        self.Passwordtext_2.setText(QCoreApplication.translate(
            "MainWindow", u"Shared Passwords", None))
        self.sha_acc_name.setText("")
        self.sha_acc_name.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"AppName/Website", None))
        self.sha_username.setText("")
        self.sha_username.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"UserName/E-Mail", None))
        self.sha_password.setText("")
        self.sha_password.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Password", None))
        self.Enter_2.setText(QCoreApplication.translate(
            "MainWindow", u"Enter", None))
        self.checkBox_2.setText(QCoreApplication.translate(
            "MainWindow", u"I hereby confirm all the details entered are correct.", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Account Name:", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Username:", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Password:", None))
        self.view_pwd_2.setText(QCoreApplication.translate(
            "MainWindow", u"View Passwords", None))
        self.another_pwd_2.setText(QCoreApplication.translate(
            "MainWindow", u"Add Another Password", None))
        self.Passwordtext_3.setText(QCoreApplication.translate(
            "MainWindow", u"Banking Passwords", None))
        self.Bank_AccNo.setText(QCoreApplication.translate(
            "MainWindow", u"Accno.", None))
        self.Bank_AccNo.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"AppName/Website", None))
        self.bank_custID.setText(
            QCoreApplication.translate("MainWindow", u"CustID", None))
        self.bank_custID.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"UserName/E-Mail", None))
        self.bank_pwd.setText("")
        self.bank_pwd.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Password", None))
        self.Enter_3.setText(QCoreApplication.translate(
            "MainWindow", u"Enter", None))
        self.checkBox_3.setText(QCoreApplication.translate(
            "MainWindow", u"I hereby confirm all the details entered are correct.", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"Account No.", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"Cust ID:", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"Password:", None))
        self.view_pwd_3.setText(QCoreApplication.translate(
            "MainWindow", u"View Passwords", None))
        self.another_pwd_3.setText(QCoreApplication.translate(
            "MainWindow", u"Add Another Password", None))
    # retranslateUi
