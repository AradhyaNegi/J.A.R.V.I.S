# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:35:38 2021

@author: abc
"""

import speech_recognition as speech
import pyttsx3
import datetime
import webbrowser
import os
from playsound import playsound
now = datetime.datetime.now()
engine=pyttsx3.init()
engine.setProperty("RATE",175)
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


    zx = {'The time is:' , '%H:%M:%S' , 'Here are some clinics nearby:-' , 'https://www.google.com/search?q=doctors+near+me&source=hp&ei=zSCeYM7LNt6H4-EPrpWv6Ak&iflsig=AINFCbYAAAAAYJ4u3b1m6yl5YZglXzNhCoeK2dJqyuZT&oq=doctors+&gs_lcp=Cgdnd3Mtd2l6EAEYADIICAAQsQMQyQMyBQgAEJIDMgUIABCxAzIFCC4QsQMyBQgAELEDMggIABCxAxCDATIFCAAQsQMyCAguEMcBEK8BMggIABCxAxCDATICCAA6CwguELEDEMcBEKMCOggILhCxAxCDAToCCC5QrgZYjh1gvC1oAHAAeACAAcQBiAGJC5IBAzAuOJgBAKABAaoBB2d3cy13aXo&sclient=gws-wiz'
          'Opening Youtube :' , 'https://www.youtube.com/'}
    
    if 'time' in command :
        engine.say(zx[0])
        engine.runAndWait()
        engine.say(now.strftime(zx[1]))
        engine.runAndWait()
    
    
    if 'unwell' in command :
         engine.runAndWait()
         engine.say(zx[2])
         engine.runAndWait()
         webbrowser.open(zx[3])


    if 'alarm' in command :
        os. system('clear')
        alarmH = int(input("What hour do you want the alarm to ring? "))
        alarmM = int(input("What minute do you want the alarm to ring? "))
        amPm = str(input("am or pm? "))
        os. system('clear')
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
        engine.say(zx[4])
        engine.runAndWait()
        webbrowser.open(zx[5])
        
    
     


  


                        
    