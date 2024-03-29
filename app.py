import sys
from PyQt5 import QtWidgets,QtCore,uic,QtGui
from PyQt5.QtWidgets import QWidget,QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QCoreApplication,pyqtSignal, pyqtSlot,Qt,QTimer
from PyQt5.uic import loadUi
from register import *
from main import MainWindow
from login import *
from icecream import install
install()
class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,300)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.label_animation=QLabel(self)
        self.movie=QMovie("images/loading.gif")
        self.label_animation.setMovie(self.movie)
        timer=QTimer(self)
        timer.singleShot(3000,self.stopAnimation)
        self.startAnimation()
    def startAnimation(self):
        self.movie.start()
        self.show()
    def stopAnimation(self):
        self.movie.stop()
        self.close()
class Controller():
    finished=pyqtSignal()
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)
        self.window=Start(windowTitle='Choose')
    def show_start(self):
        self.window.rw.connect(self.show_register)
        self.window.mw.connect(self.show_main)
        self.window.show()
    def show_register(self):
        self.reg = Register()
        self.reg.sw.connect(self.start2)
        self.window.close()
        self.reg.show()
    def show_main(self,str):
        self.window.close()
        self.main=MainWindow(str)
        self.main.lw.connect(self.signout)
        self.main.setWindowTitle(f"Welcome {str}")
        self.main.show()
    def load(self):
        self.L=LoadingScreen()
    def start2(self):
        self.reg.close()
        self.window=Start(windowTitle='Choose')
        self.window.rw.connect(self.show_register)
        self.window.mw.connect(self.show_main)
        self.window.show()
    def signout(self):
        self.main.close()
        self.window=Start(windowTitle='Choose')
        self.window.rw.connect(self.show_register)
        self.window.mw.connect(self.show_main)
        self.window.show()
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    w=Controller()
    w.show_start()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

