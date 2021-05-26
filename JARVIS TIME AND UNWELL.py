# -*- coding: utf-8 -*-
"""
JARVIS MyWORK
"""
import speech_recognition as speech
import pyttsx3
import datetime
import webbrowser
#import os
from playsound import playsound
now = datetime.datetime.now()
engine=pyttsx3.init()
engine.setProperty("RATE",75)
r=speech.Recognizer()
with speech.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source)
   
r=speech.Recognizer()
with speech.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Speak:")
    engine.say("Speak")
    engine.runAndWait()
    audio=r.listen(source)
    command=r.recognize_google(audio)


    
    
    if 'time' in command :
       
        engine.say("The time is:")
        engine.runAndWait()
        engine.say(now.strftime("%H:%M:%S"))
        engine.runAndWait()
        
    
    
    if 'unwell'or 'doctors' in command :
         engine.runAndWait()
         engine.say("Here are some clinics nearby:-")
         engine.runAndWait()
         webbrowser.open("https://www.google.com/search?q=doctors+near+me&source=hp&ei=zSCeYM7LNt6H4-EPrpWv6Ak&iflsig=AINFCbYAAAAAYJ4u3b1m6yl5YZglXzNhCoeK2dJqyuZT&oq=doctors+&gs_lcp=Cgdnd3Mtd2l6EAEYADIICAAQsQMQyQMyBQgAEJIDMgUIABCxAzIFCC4QsQMyBQgAELEDMggIABCxAxCDATIFCAAQsQMyCAguEMcBEK8BMggIABCxAxCDATICCAA6CwguELEDEMcBEKMCOggILhCxAxCDAToCCC5QrgZYjh1gvC1oAHAAeACAAcQBiAGJC5IBAzAuOJgBAKABAaoBB2d3cy13aXo&sclient=gws-wiz")


    if 'alarm' in command :
       # os.system('clear')
        alarmH = int(input("What hour do you want the alarm to ring? "))
        alarmM = int(input("What minute do you want the alarm to ring? "))
        amPm = str(input("am or pm? "))
       # os.system('clear')
        print("Waiting for alarm",alarmH,alarmM,amPm)
        if (amPm == "pm"):
                alarmH = alarmH + 12
        while(1 == 1):
            if(alarmH == datetime.datetime.now().hour and
                alarmM == datetime.datetime.now().minute) :
                engine.say("Time to wake up")
                engine.runAndWait()
                playsound('C:\\Users\\abc\\Desktop\\PYTHON COURSE\\d.mp3')
                break
    
         

    if 'youtube' in command :
        engine.say("Opening Youtube")
        engine.runAndWait()
        webbrowser.open("https://www.youtube.com/")
        
    if 'google' in command :
        engine.say("opening Google")
        engine.runAndWait()
        webbrowser.open("https://www.google.com/")
        
    if 'news' in command :
        engine.say("Opening times of India for latest news :")
        engine.runAndWait()
        webbrowser.open("https://timesofindia.indiatimes.com/defaultinterstitial.cms")
