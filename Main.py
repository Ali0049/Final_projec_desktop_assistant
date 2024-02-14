from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import webbrowser as web
import pyttsx3 #for speak
import speech_recognition  #for take command
#from win10toast import ToastNotifier
from Features import greetMe
import requests
import os
from datetime import datetime
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from PIL import Image
import random
from bs4 import BeautifulSoup


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
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
        
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
def TaskExe():
    Speak("Jarvis Here How Can I Assist You Sir!....")
    
    while True:

        query = TakeCommand().lower()

        if "google search" in query:
            from Features import GoogleSearch
            query = query.replace('jarvis',"")
            query = query.replace("google search","")
            query = query.replace(" ","+")
            GoogleSearch(query)

        elif 'how to' in query:
            from Features import How_To
            How_To(query)

        elif 'youtube' in query:
            Query = query.replace("jaxrvis","")
            query = Query.replace("youtube search","")
            from Features import YouTubeSearch
            YouTubeSearch(query)

        elif 'set alarm' in query:
            from Features import Alarm
            Alarm(query)

        elif 'download' in query:
            Speak('download funtion is started')
            from Features import Downloadyoutube
            Downloadyoutube()
        
        elif 'speed test' in query:
            from Features import SpeedTest
            SpeedTest()

        elif 'temperature' in query:
            from Features import Temp
            Temp(query)

        elif 'calculator' in query:
            from Features import Calculator
            Speak('kindly write your calculations')
            query=input()
            Calculator(query)
        
        elif 'whatsapp message' in query:

            name = query.replace('whatsapp message ',"")
            name = name.replace('send ',"")
            name = name.replace('to ',"")
            Name = str(name)
            Speak(f"whats the message for {Name}")
            MSG = TakeCommand()
            from Automation import WhasappMsg
            WhasappMsg(Name,MSG)
        
        elif 'call' in query:
            from Automation import whatsappCall
            name = query.replace("call","")
            name = name.replace("jarvis","")
            name = name.replace("whatsapp","")
            Name = str(name).lower()
            whatsappCall(Name)
        
        
        elif 'new tab' in query:
            press_and_release('ctrl + t')

        elif 'close tab' in query:
            press_and_release('ctrl + w')

        elif 'new window' in query:
            press_and_release('ctrl + n')

        elif 'history' in query:
            press_and_release('ctrl + h')

        elif 'downloads' in query:
            press_and_release('ctrl + j')
            
        elif 'bookmark' in query:
                
            press_and_release('ctrl + d')

            press('enter')
                
        elif 'incognito' in query:

            press_and_release("ctrl + Shift + n")

        elif 'open' in query:

            name = query.replace("open","")

            NameA = str(name)

            if 'youtube' in NameA:

                web.open("https://www.youtube.com/")
                
            elif 'instagram' in NameA:

                startfile("C:\\Users\\alij7\\OneDrive\\Desktop\\Instagram.lnk")

            elif 'facebook' in NameA:

                startfile("C:\\Users\\alij7\\OneDrive\\Desktop\\Facebook.lnk")

            elif 'blackboard' in NameA:

                web.open('https://iqra.blackboard.com/')

            else:

                web_string = "https://www."+ NameA + ".com"

                web_string2 = web_string.replace(" ","")

                web.open(web_string2)

        elif 'pause' in query:

            press('space bar')

        elif 'resume' in query:

            press('space bar')

        elif 'full screen' in query:

            press('f')

        elif 'film screen' in query:

            press('t')

        elif 'forward' in query:

            press('l')
        
        elif 'back' in query:

            press('j')

        elif 'decrease' in query:
        
            press_and_release('shift+ ,')

        elif 'speed up' in query:

            press_and_release('shift+ .')
        
        elif 'pichhali' in query:

            press_and_release('shift + p')

        elif 'next video' in query:

            press_and_release('shift + n')

        elif 'mute' in query:

            press('m')

        elif 'unmute' in query:

            press('m')

        elif 'search' in query:

            click(x=1245, y=173)

            Speak('What to Search sir ?')

            search = TakeCommand()

            write(search)

            sleep(0.8)

            press('enter')

        elif 'skip' in query:

            click(x=1023, y=649)

        elif 'space news' in query:

            Speak('Tell Me The Date For News Extraction, kindly write year first then month number and day number(year-month-day)')
            
            Date = input("write date (year-month-day):")
            from Features import DateConverter

            Value = DateConverter(Date)

            from Nasa import NasaNews

            NasaNews(Value)

        elif 'about' in query:
            from Nasa import Summary
            query = query.replace("jarvis ","")
            query = query.replace("about ","")
            Summary(query)

        elif  'mars images' in query:
            Speak('please sir write the date yy-mm-dd')
            Date = input("write date (year-month-day):")
            from Features import DateConverter
            Value = DateConverter(Date)
            from Nasa import MarsImage
            MarsImage(Value)

        elif 'track iss' in query:
            Speak('I am tracking sir.....')
            from Nasa import trackISS
            trackISS()

        elif 'near earth' in query:

            from Nasa import Astro
            from Features import DateConverter
            Speak('write The Starting Date in format year//month//date.')
            start = input("starting date : ")
            start_date = DateConverter(start)
            Speak("Write The End Date Date in format year//month//date.")
            end = input("end date : ")
            end_date = DateConverter(end)

            Astro(start_date,end_date)
        
        elif 'solar system' in query:
            from Nasa import SolarBodies
            Speak("Tell Me The Name Of Body .")
            bod =TakeCommand()
            body = bod.replace(" ","")
            body = body.replace(" ","")
            Body = str(body)
            SolarBodies(body=Body)

        elif 'my location' in query:
            from Features import My_location
            My_location()

        elif 'where is' in query:
            from Features import GoogleMaps
            Place = query.replace('where is ',"")
            Place = Place.replace("jarvis","")
            Place = Place.replace(" ","+")
            print(Place)

            GoogleMaps(Place)

        elif 'write a note' in query:

            from Automation import Notepad
            Notepad()

        elif 'dismiss' in query:
            from Automation import CloseNotepad
            CloseNotepad()

        elif 'time table' in query:
            from Timetable import main
            main()

        elif "quran" in query:
            from quran import Quran
            Speak ("Welcome To Heaven Sir")
            Quran()
        
        elif "kuran" in query:
            from quran import Quran
            Speak ("Welcome To Heaven Sir")
            Quran()

        elif 'screenshot' in query:
            from Features import Screenshot
            Screenshot()

        elif 'music' in query:
            from Features import Music
            Music()

        elif 'joke' in query:
            from Features import joke
            joke()

        elif 'wiki'in query:
            query=query.replace(" ","")
            query = query.replace(" ","+")
            from Features import wikipediaa
            wikipediaa(query)
        
        elif 'remember that' in query:
            file_path = 'dataa.txt'
            remember_msg = query.replace('remember that', '').replace('jarvis', '').strip()
            
            with open(file_path, 'a') as remember_file:
                remember_file.write(remember_msg)
            
            Speak(f'You told me to remind you that: {remember_msg}')
        
        elif 'what do you remember' in query:
            file_path = 'dataa.txt'
            try:
                with open(file_path, 'r') as remember_file:
                    remember_msg = remember_file.read().strip()
                    Speak(f'You told me that: {remember_msg}')
            except FileNotFoundError:
                Speak('I do not have any specific information to remember.')

        elif 'start' in query:
            from Features import Open
            Speak('Opening app sir')
            Open(query)

        elif 'volume up' in query:
            from Features import volumeup
            volumeup()
            Speak('volume increased sir!')

        elif 'volume down' in query:
            from Features import volumedown
            volumedown()
            Speak('volume decreased sir!')

        elif 'you need a break jarvis' in query:
            Speak('Ok sir have a good day')
            break        

        elif 'bye' in query:
            Speak('bye bye sir')

            break
        
        elif 'exit'in query:
            Speak('Ok Boss')

            break


