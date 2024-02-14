from Desktop_Assistant_Ui import Ui_Jarvis
from PyQt5 import QtCore, QtGui ,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from PyQt5.uic import loadUiType
import Main
import sys
import warnings
import os

# Set environment variables for handling screen scaling
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
os.environ["QT_SCALE_FACTOR"] = "1"

# Rest of your code here

# Suppress DeprecationWarnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class MainThread(QThread):
 
    def __init__(self):

        super(MainThread,self).__init__()
    
    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        Main.greetMe()
        Main.TaskExe()
        
    

startFuntions = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):

        super().__init__()

        self.gui = Ui_Jarvis()
        
        self.gui.setupUi(self)

        self.gui.pushButton_start.clicked.connect(self.startFunc)
        self.gui.pushButton_exit.clicked.connect(self.close)

    def startFunc(self):

        self.gui.movies_gif = QtGui.QMovie("C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\database\\GUI material\\Personal Artificial Intelligence Assistant.gif")
        self.gui.label_1_gif.setMovie(self.gui.movies_gif)
        self.gui.movies_gif.start()


        startFuntions.start()

GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())

