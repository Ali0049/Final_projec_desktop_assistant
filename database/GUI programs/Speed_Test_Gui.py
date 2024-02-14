from PyQt5.QtGui import * 
from Speed_Test_Ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUiType
import sys
import pyttsx3  # for speak

engine = pyttsx3.init('sapi5')  # to activate sapi5 driver
voices = engine.getProperty('voices')  # it will get all voices
engine.setProperty('voices', voices[0].id)  # which voices to be used
engine.setProperty('rate', 170)  # speed rate of voices


def Speak(audio):
    print("    ")
    print(f": {audio}")
    print("    ")
    engine.say(audio)
    engine.runAndWait()


def run_uit():
    #module for speed test function
    import speedtest
    #to get speed of internet 
    speed = speedtest.Speedtest()
    #geting uploading speed 
    upload = speed.upload()
    #now converet mpks value in mbs
    correct_up = int(int(upload) / 800000)

    download = speed.download()

    correct_down = int(int(download) / 800000)

    Speak(f"Downloading Speed is {correct_down} M B Per Second .")
    Speak(f"Uploading Speed is {correct_up} M B Per Second .")

    exit()
    
class MainThread(QThread):
    def __init__(self):#constructor that call function asa self
        super(MainThread, self).__init__()

    def run(self):
        run_uit()

StartExe = MainThread()
        #main window in ui file
class StartExecution(QMainWindow):
    def __init__(self):
        Speak("I am checking speed sir, wait for a while.")

        super().__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.label = QtGui.QMovie("C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\GUI material\\hsv-check-your-internet-peed.gif")

        self.ui.gif.setMovie(self.ui.label)

        self.ui.label.start()

        self.start_execution()

    def start_execution(self):
        StartExe.start()
        StartExe.finished.connect(self.speed_test_completed)

    def speed_test_completed(self):
        Speak("Speed test completed.")
        self.close()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Speedtest = StartExecution()
    Speedtest.show()
    sys.exit(App.exec_())
