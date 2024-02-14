import os
from playsound import playsound
import datetime
 
#it extract time from query where we save in rt(read text) form
extracted_time = open("C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\data.txt",'rt')
#now the extracted time store in ne varriable in str form 
time = extracted_time.read()
Time = str(time)

#that delete time from that particular file r+ to read and write form
delete_time = open("C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\data.txt",'r+')
#any thing in that file will remove
delete_time.truncate(0)
#close file 
delete_time.close()


def RingerNow(time):
    #time that we give as query
    time_to_set = str(time)
    time_now = time_to_set.replace("jarvis ","")
    time_now = time_now.replace("set alarm for ","")
    time_now = time_now.replace("set ","")
    time_now = time_now.replace("alarm ","")
    time_now = time_now.replace("for ","")
    time_now = time_now.replace(" and ",":")
    #it removes all extras in time just take time(filter)
    Alarm_Time = str(time_now)

    while True:
        #check time continously untill alaram time same as current time
        #by using date time module
        current_time = datetime.datetime.now().strftime('%H:%M')
        if current_time == Alarm_Time:
            print("Wake Up Sir, It's Time to Work .")
            #by using playsound it play audio from that path
            playsound("C:\\Users\\alij7\\OneDrive\\Desktop\\Final_projec_desktop_assistant\\database\\Sounds\\Jarvis Wake Up Iron Man Edition.mp3")

        elif current_time > Alarm_Time:
            #when current time increased more than 
            #Alarm time it will break loop and stops
            break


RingerNow(Time)
