import pywhatkit
import wikipedia
import pyttsx3
from pywikihow import WikiHow , search_wikihow
import os
import webbrowser as web
import wolframalpha 
import requests 
from requests import get
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import pyjokes
import pyautogui
import pyttsx3
from bs4 import BeautifulSoup
import datetime
from pynput.keyboard import Key,Controller
from time import sleep
import speech_recognition as sr 
from keyboard import press_and_release#for speak
#for take command
#from Features import GoogleSearch


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

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        Speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        Speak("Good Afternoon ,sir")

    else:
        Speak("Good Evening,sir")

def GoogleSearch(term):
    try:
        query = term.replace("jarvis", "").replace("what is", "").replace("how to", "").replace("what do you mean by", "")

        #writeab = str(query)

        Query = str(term)
        pywhatkit.search(Query)
        search = wikipedia.summary(Query, 2)
        Speak(f": According to Your Search : {search}")
        '''
        if 'how to' in Query:
            max_result = 1
            how_to_func = search_wikihow(query=Query, max_results=max_result)
            assert len(how_to_func) == 1  # for in one line
            how_to_func[0].print()
            Speak(how_to_func[0].summary)

        else:
            pywhatkit.search(Query)
            search = wikipedia.summary(Query, 2)
            Speak(f": According to Your Search : {search}")
        '''
    except Exception as e:
        Speak(f"An error occurred during the search: {e}")

def How_To(term):

    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace("what do you mean by","")
    query = query.replace("jarvis","")
    Query = str(term)

    max_result = 1
    how_to_func = search_wikihow(query=Query,max_results=max_result)
    assert len(how_to_func) == 1 #for in one line
    #how_to_func[0].print()
    Speak(how_to_func[0].summary)

def YouTubeSearch(term):
    try:
        result = "https://www.youtube.com/results?search_query=" + term
        web.open(result)
        Speak("This Is What I Found For Your Search.")
        pywhatkit.playonyt(term)
        Speak("This May Also Help You Sir.")

    except Exception as e:
        Speak(f"An error occurred during the YouTube search: {e}")

def Alarm(query):
    #a file path where your time in query stored
    TimeHere = open("C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\data.txt",'a')
    #in write form it store query in that file
    TimeHere.write(query)
    #now it close the file
    TimeHere.close()
    #it open the py script of alarm file
    os.startfile("C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\ExtraPro\\Alarm.py")

def Downloadyoutube():
    #module use for downloading video form youtube
    from pytube import YouTube
    #to control gui or windows gui
    from pyautogui import click
    from pyautogui import hotkey
    #for paste the value 
    import pyperclip
    from time import sleep
    
    try:
        sleep(2)
        #click on position where the link of video is
        click(x=425, y=93)
        #by uing copy
        hotkey('ctrl','a')
        hotkey('ctrl','c')
        #and paste
        value = pyperclip.paste()
        print(value)
        
        #now link is ready to download
        Link = str(value)

        def Download(link):#now link is provides to that func

            url = YouTube(link)
            #video on first will download
            video = url.streams.first()
            #path where video is going to download
            video.download("C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\Youtube Download")

        Download(Link)

        Speak('Done Sir, I Have Donloaded The Video')
        Speak('You can Go and Check It Out')
        #open that path
        os.startfile("C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\Youtube Download")
    except:
        Speak('some thing went wrong,try again')
def SpeedTest():
    os.startfile("C:\\Users\\alij7\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\GUI programs\\Speed_Test_Gui.py")
    
def Wolfram(query):

    api_key = "PUGTVE-UGAUTTV3L2"

    requester = wolframalpha.Client(api_key)

    requested = requester.query(query)

    

    try:

        Answer = next(requested.results).text

        return Answer
    
    except:
        Speak('An String Value Is Not Answerable')

def Calculator(query):

    Term = str(query)

    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("equals to","=")
    Term = Term.replace('square',"^")


    Final = str(Term)
    try:
        result = Wolfram(Final)
        Speak(f"{result}")

    except:
        Speak("An String Value Is Not Answerable")

def Temp(query):

    Term = str(query)

    Term = Term.replace("jarvis","")
    Term = Term.replace("in","")
    Term = Term.replace("what is the","")
    Term = Term.replace("temperature","")

    temp_query = str(Term)

    if 'outside' in temp_query:

        var1 = 'Temperature in Islamabad'

        answer = Wolfram(var1)

        Speak(f"{var1} is {answer} .")

    else:

        var2 = 'Temperature in '+ temp_query

        answ = Wolfram(var2)

        Speak(f"{var2} Is {answ}")

def DateConverter(Query):

    Date =  Query.replace(" and ",'-')
    Date =  Date.replace(" and ",'-')
    Date =  Date.replace("and",'-')
    Date =  Date.replace("and",'-')
    Date = Date.replace(" ","")

    return str(Date)

def My_location():
    url='https://www.google.com/maps/place/Islamabad,+Islamabad+Capital+Territory,+Pakistan/@33.6162509,72.7564424,10z/data=!3m1!4b1!4m6!3m5!1s0x38dfbfd07891722f:0x6059515c3bdb02b6!8m2!3d33.6844202!4d73.0478848!16zL20vMGRoZDU?entry=ttu'
    
    url_iqra = 'https://www.google.com/maps/place/Iqra+University+-+Islamabad+Campus+(IUIC)/@33.6643366,73.0427766,17z/data=!3m1!4b1!4m6!3m5!1s0x38df9577272c08cd:0x41b519c0202b7d5c!8m2!3d33.6643322!4d73.0453515!16s%2Fg%2F12qg141hx?entry=ttu'
    Speak('cheking.......')
    
    web.open(url_iqra)
    ip_add = 	'154.91.164.177'

    url = 'http://get.geojs.io/v1/ip/geo/'+ip_add+'.json'


    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    Speak(f"sir , You Are Now In {state , country}")

def GoogleMaps(Place):

    try:

        Url_Place = "https://www.google.com/maps/place/" + str(Place)

        geolocator = Nominatim(user_agent="myGeocoder")

        location = geolocator.geocode(Place , addressdetails= True)

        target_latlon = location.latitude , location.longitude

        web.open(url=Url_Place)

        location = location.raw['address']

        target = {'city' : location.get('city',''),
                    'state' : location.get('state',''),
                    'country' : location.get('country','')}

        current_loca = geocoder.ip('me')

        current_latlon = current_loca.latlng

        distance = str(great_circle(current_latlon,target_latlon))
        distance = str(distance.split(' ',1)[0])
        distance = round(float(distance),2)


        Speak(target)
        Speak(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")

    except:
        Speak("sir you need to call me later,server is down now")

def Music():
            
        Speak('tell me the name of the song')
        musicname=TakeCommand()

        if 'maa ki shan' in musicname:
            os.startfile('"C:\\Users\\alij7\\Music\\maa-ki-shan.mp3"')
        else:
            pywhatkit.playonyt(musicname)

        Speak("your song has been started! ,Enjoy Sir!")          

def Screenshot():
    try:
        Speak("Ok Boss , What Should I Name That File ?")
        path = TakeCommand()
        path1name = path + ".png"
        path1 = "C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\Screenshot\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile(path1)
        Speak("Here Is Your ScreenShot")
    except:
        Speak('i could not take screenshot you can call me again')

def joke():
    try:

        get = pyjokes.get_joke()
        Speak (get)
    except:
        Speak('you are joke')

def wikipediaa(query):
    try:
        Speak('Searching Wikipedia....')
        query = query.replace("wikipedia","")
        query = query.replace("jarvis","")
        wiki  = wikipedia.summary(query,2)
        Speak(wiki)
    except:
        print('an error occured')

def remember(query):
    file_path = 'dataa.txt'
    
    if 'remember that' in query:
        remember_msg = query.replace('remember that', '').replace('jarvis', '').strip()
        
        with open(file_path, 'w') as remember_file:
            remember_file.write(remember_msg)
        
        Speak(f'You told me to remind you that: {remember_msg}')

def Open(query):    
        
        query = query.replace("open","")
        query = query.replace("start","")
        query = query.replace("jarvis","")
        query = query.replace(" ",'')
        press_and_release('windows + s')
        pyautogui.sleep(1)
        pyautogui.typewrite(query)
        pyautogui.sleep(1)
        pyautogui.press("enter") 

def volumeup():
    keyboard = Controller()

    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
        
def volumedown():
    keyboard = Controller()

    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

