import pyttsx3
import speech_recognition as sr
import webbrowser
import urllib.parse
import pywhatkit

# Constants for URLs
SURAH_AL_FATIHA_URL = "https://www.youtube.com/watch?v=sjS8vkvycmw&list=PLF-AzhmyjY8xEojcjawrgQ8P21MJRuVfM&index=1"
SURAH_AL_BAQARA_URL = "https://www.youtube.com/watch?v=Hvo4NeUxLdc&list=PLF-AzhmyjY8xEojcjawrgQ8P21MJRuVfM&index=2"
SURAH_AL_IMRAN_URL = "https://www.youtube.com/watch?v=JAdx6tR1WnQ&list=PLF-AzhmyjY8xEojcjawrgQ8P21MJRuVfM&index=3"
SURAH_AL_NISA_URL = "https://www.youtube.com/watch?v=QER4JTHn-0E&list=PLF-AzhmyjY8xEojcjawrgQ8P21MJRuVfM&index=4"
SURAH_AL_MAIDA_URL = "https://www.youtube.com/watch?v=lH-siAW6qgI&list=PLF-AzhmyjY8xEojcjawrgQ8P21MJRuVfM&index=5"
SURAH_AL_ANAM_URL = "https://www.youtube.com/watch?v=Hqt9lIFndko&list=PLF-AzhmyjY8xEojcjawrgQ8P21MJRuVfM&index=6"
SURAH_AL_ARAF_URL = "https://www.youtube.com/watch?v=3Wmf9YH3jE0&list=PLF-AzhmyjY8xEojcjawrgQ8P21MJRuVfM&index=7&pp=iAQB"
SURAH_AL_ANFAL_URL = "https://www.youtube.com/watch?v=NuhowPIwQnY&list=PLF-AzhmyjY8xEojcjawrgQ8P21MJRuVfM&index=8"
SURAH_AL_TAUBA_URL = "https://www.youtube.com/watch?v=WEkenhA5mPU&list=PLF-AzhmyjY8xEojcjawrgQ8P21MJRuVfM&index=9"
SURAH_YUNUS_URL = "https://www.youtube.com/watch?v=Lu-n16Dvn_U&list=PLF-AzhmyjY8xEojcjawrgQ8P21MJRuVfM&index=10"
SURAH_DOHA_URL = "https://www.youtube.com/watch?v=U22bA-lsCX0"
SURAH_RAHMAN_URL = "https://www.youtube.com/watch?v=6VoSqfQZ_TQ"
SURAH_YASEEN_URL = "https://www.youtube.com/watch?v=mlHtrrFSYk0"

# Surah information dictionary
SURAH_INFO = {
    'surah al fatiha': {
        'description': "Opening chapter of the Quran...",
        'url': SURAH_AL_FATIHA_URL
    },
    'surah al baqara': {
        'description': "Second and longest chapter of the Quran...",
        'url': SURAH_AL_BAQARA_URL
    },
    'surah al imran': {
        'description': "Chapter 3 of the Quran...",
        'url': SURAH_AL_IMRAN_URL
    },
    'surah al nisa': {
        'description': "Surah An-Nisa, also known as 'The Women'...",
        'url': SURAH_AL_NISA_URL
    },
    'surah al maida': {
        'description': "Surah Al-Ma'idah is the fifth chapter of the Quran...",
        'url': SURAH_AL_MAIDA_URL
    },
    'surah al anam': {
        'description': "Surah Al-An'am is the sixth chapter of the Quran...",
        'url': SURAH_AL_ANAM_URL
    },
    'surah al araf': {
        'description': "Surah Al-A'raf is the seventh chapter of the Quran...",
        'url': SURAH_AL_ARAF_URL
    },
    'surah al anfal': {
        'description': "Surah Al-Anfal is the eighth chapter of the Quran...",
        'url': SURAH_AL_ANFAL_URL
    },
    'surah al tauba': {
        'description': "Surah At-Tawbah is the ninth chapter of the Quran...",
        'url': SURAH_AL_TAUBA_URL
    },
    'surah yunus': {
        'description': "Surah Yunus is the tenth chapter of the Quran...",
        'url': SURAH_YUNUS_URL
    },
    'surah doha': {
        'description': "Surah Ad-Duha is the 93rd chapter of the Quran...",
        'url': SURAH_DOHA_URL
    },
    'surah rahman': {
        'description': "Surah Ar Rahman is the 55th chapter of the Quran...",
        'url': SURAH_RAHMAN_URL
    },
    'surah yaseen': {
        'description': "Surah Yaseen is the 36th chapter of the Quran...",
        'url': SURAH_YASEEN_URL
    }
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 170)


def Speak(audio):
    print("    ")
    print(f": {audio}")
    print("    ")
    engine.say(audio)
    engine.runAndWait()


def TakeCommand():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(": Listening....")
            r.pause_threshold = 1
            audio = r.listen(source, 0, 4)
        try:
            print(": Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f": Your Command : {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            print(": Sorry, I could not understand the audio. Please try again.")
        except sr.RequestError as e:
            print(f": Could not request results from Google Speech Recognition service; {e}")


def Quran():
    Speak("Which Surah would you like to listen to?")
    query = TakeCommand()
    surah = query.lower()
    if surah in SURAH_INFO:
        info = SURAH_INFO[surah]
        Speak(f'Playing {info["description"]}')
        try:
            webbrowser.open(info['url'])
        except Exception as e:
            print(f"Error opening URL: {e}")
        Speak('Peace be upon you!')
    else:
        Speak(f"Sorry, I couldn't find {surah} in my database. Let me search it for you on YouTube.")
        search_query = f"Quran {surah} recitation"
        youtube_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(search_query)}"
        try:
            pywhatkit.playonyt(youtube_url)
        except Exception as e:
            print(f"Error opening YouTube search: {e}")
        Speak(f"Here is the YouTube search results for {surah}. Peace Your Mind Sir.")


