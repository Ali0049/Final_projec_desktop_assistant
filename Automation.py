from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import pyttsx3 #for speak
import speech_recognition as sr #for take command
import webbrowser as web
from datetime import datetime
import os
from notifypy import Notify
import pyautogui
engine = pyttsx3.init('sapi5')#to activiate sapi5 driver
voices = engine.getProperty('voices')#it will get all voices
engine.setProperty('voices',voices[0].id)#which voices to be use
engine.setProperty('rate',170)#speed rate of voices
def Speak(audio):
    print("    ")
    print(f": {audio}")
    print("    ")
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_thershold = 1
        audio = r.listen(source,0,4)
    try:
        print(": Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f": Your Command : {query}\n")
    except:
        return ""
    return query.lower()
    ayesha
def WhasappMsg(name,message):
    '''
    startfile_= 'Whatsapp'
    pyautogui.press("super")
    pyautogui.typewrite(startfile_)
    pyautogui.sleep(2)
    pyautogui.press("enter")      
    '''

    press_and_release('Windows + S')
    pyautogui.sleep(1)
    pyautogui.typewrite('WhatApp')
    pyautogui.sleep(1)
    pyautogui.press("enter")      
    
    sleep(5)

    click(x=159, y=181)

    sleep(2)

    write(name)

    sleep(2)

    click(x=287, y=284)

    sleep(2)

    click(x=857, y=967)

    sleep(2)

    write(message)

    press('enter')

    sleep(2)
    Speak(f'the message {message} is send to {name} I am closing whatsapp')
    click(x=1885, y=18)


def whatsappCall(name):
    press_and_release('Windows + S')
    pyautogui.sleep(1)
    pyautogui.typewrite('WhatApp')
    pyautogui.sleep(1)
    pyautogui.press("enter")   

    sleep(5)

    click(x=159, y=181)

    sleep(2)

    write(name)

    sleep(2)

    click(x=287, y=284)

    sleep(2)

    click(x=1773, y=105)


def whatsappChat(name):

    press_and_release('Windows + S')
    pyautogui.sleep(1)
    pyautogui.typewrite('WhatApp')
    pyautogui.sleep(1)
    pyautogui.press("enter")  
          

    sleep(5)

    click(x=132, y=122)

    sleep(2)

    write(name)

    sleep(2)

    click(x=197, y=181)

    sleep(2)

    click(x=562, y=695)

    sleep(2)

def whatsappVideoCall(name):

    press_and_release('Windows + S')
    pyautogui.sleep(1)
    pyautogui.typewrite('WhatApp')
    pyautogui.sleep(1)
    pyautogui.press("enter")   

    sleep(5)

    click(x=159, y=181)

    sleep(2)

    write(name)

    sleep(2)

    click(x=287, y=284)

    sleep(2)

    click(x=1685, y=95)


def Notepad():
    try:
        Speak("Tell me the query.")
        Speak("I am ready to write.")
        
        # Assuming TakeCommand is a function that takes user input
        writes = TakeCommand()

        time = datetime.now().strftime('%H-%M')
        filename = f"{time}-note.txt"

        with open(filename, 'w') as file:
            file.write(writes)

        desktop_path = "C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant"
        source_path = os.path.join(desktop_path, filename)
        destination_path = os.path.join(desktop_path, "database", "Notepad", filename)

        os.rename(source_path, destination_path)
        os.startfile(destination_path)

    except Exception as e:
        print(f"An error occurred: {e}")
        Speak("Sorry, I encountered an error while processing your request.")

def CloseNotepad():

    os.system("TASkKILL /F /im Notepad.exe")
