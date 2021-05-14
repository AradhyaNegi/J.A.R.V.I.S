# -*- coding: utf-8 -*-
"""
J.A.R.V.I.S
"""
import speech_recognition as speech
import pyttsx3
import datetime
now = datetime.datetime.now()
import pyjokes
import time
import pywhatkit
import wikipedia

engine=pyttsx3.init()

engine.setProperty("RATE",125)

engine.say("Hello!")
time.sleep(2)
engine.say("I am JARVIS !! Just A Rather Very Intelligent System")
time.sleep(1)
engine.say("I can do a lot of things such as tell you the time, play songs, crack jokes and even tell you information of anything or anyone!")
engine.say("You can say, JARVIS wake up to activate me, If I am inactive, which I rather won't be!")


engine.runAndWait()


while True:
    try:
        #Take the user input to activate reception of Voice Commands
        engine.say("Press v to start voice commands and q to quit: ")
        engine.runAndWait()
        
        userInput=input("Here press 'v' :")
        
        if userInput=='v':
            
            #Take Voice commands from mic
            r=speech.Recognizer()
            with speech.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Speak:")
                audio=r.listen(source)
            #Convert Voice Commands to Text
            command=r.recognize_google(audio)
            
            if "wake" in command :
                    engine.say("Up and ready for you sir!")
                    engine.runAndWait()
                    
            
            if "time" in command:
                    engine.say("The time is:")
                    engine.runAndWait()
                    engine.say(now.strftime("%H:%M:%S"))
                    engine.runAndWait()
                    
            if "joke" in command :
                    engine.say("Here it is!")
                    engine.runAndWait()
                    engine.say(pyjokes.get_joke())
                    engine.runAndWait()
                    engine.say("ha ha ha")
                    engine.runAndWait()

            if 'play' in command:
                    song = command.replace('play', '')
                    engine.say('playing ' + song)
                    engine.runAndWait()
                    pywhatkit.playonyt(song)
                
            if 'who is' in command :
                    person = command.replace('who is', '')
                    info = wikipedia.summary(person, 1)
                    print(info)
                    engine.say(info)
                    engine.runAndWait()
                
            if 'what is' in command :
                    person = command.replace('what is', '')
                    info = wikipedia.summary(person, 1)
                    print(info)
                    engine.say(info)
                    engine.runAndWait()
            
            if 'fact' in command :
                    engine.say("A very astute observation sir. We should improve the space travel from our planet.")
                    engine.runAndWait()
                    
            if 'ready' in command :
                    engine.say("For you sir? Always!")
                    engine.runAndWait()
        else:
            break
   
    #Statements to Handle errors while receiving voice commands
    except speech.UnknownValueError:
        engine.say("Could not understand audio")
        engine.runAndWait()
    except speech.RequestError as e:
        engine.say("Could not request results; {0}".format(e))
        engine.runAndWait()
    except KeyboardInterrupt:
        break
engine.say("Nice interacting with you sir.")
engine.runAndWait()
print("Nice interacting with you!!")
