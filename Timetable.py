from datetime import datetime
import pyttsx3
import speech_recognition as sr

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
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 4)
    try:
        print(": Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f": Your Command : {query}\n")
    except:
        return ""
    return query.lower()

def TimeTable():
    hour = int(datetime.now().strftime("%H"))

    if 5 <= hour < 6:
        Speak('''
        In This Time , You Have To Get up & pray and read Quran.
        5:00 AM to 6:00 AM
        Thanks.
        ''')
    elif 6 <= hour < 9:
        Speak('''
        In This Time , You have To study.
        6:00 AM To 9:00 AM.
        ''')
    elif 9 <= hour < 12:
        Speak('''
        In This Time , You Have to code.
        Thanks.
        ''')
    elif 12 <= hour < 15:
        Speak('''
        In This Time, You Have To Gain Some knowledge from Internet or from books.
        12:00 PM to 3:00 PM.
        Thanks.
        ''')
    elif 15 <= hour < 21:
        Speak('''
        In This Time , You Have To Code.
        3:00 PM To 9:00 PM
        Thanks.
        ''')
    elif 21 <= hour < 22:
        Speak('''
        In This Time , You Have to Sleep.
        9:00 PM to 10:00 PM.
        Thanks.
        ''')
    else:
        Speak('In This Time, You Have To Sleep')

def handle_custom_command():
    Speak("Sure, what task would you like to add?")
    task = TakeCommand()

    if not task:
        Speak("No task detected.")
        return

    while True:
        Speak("On which day would you like to add this task?")
        day = TakeCommand()

        if day.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            Speak(f"Added task to your {day.capitalize()} schedule: {task}")
            break
        else:
            Speak("I'm sorry, I couldn't recognize the day. Please try again.")

def main():
    Speak("Welcome to Jarvis Time Manager!")

    while True:
        print("\nListening for commands...")
        command = TakeCommand()

        if "exit" in command:
            Speak("Goodbye!")
            break
        elif "time table" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            Speak(f"The current time is {current_time}. Here is your timetable for today:")
            TimeTable()
            Speak("Would you like to know the timetable for another day?")
            response = TakeCommand()
            if "yes" in response:
                Speak("Sure, on which day would you like to know the timetable?")
                requested_day = TakeCommand()
                TimeTable()
            else:
                Speak("Okay, let me know if you need anything else.")
        elif "task" in command:
            handle_custom_command()
        else:
            Speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
