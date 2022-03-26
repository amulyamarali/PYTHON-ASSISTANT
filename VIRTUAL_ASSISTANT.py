# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 19:24:33 2022

@authors: Amulyam, Dhatri and Sharanya
"""

from tkinter import *
import webbrowser as wb
import speech_recognition as sr #speech to text
import pyttsx3 as pt #text to speech
import pyjokes # for jokes
import time # for time
import pywhatkit #for accessing applications
import datetime # to access date and time
import wikipedia #to access info from wiki

root=Tk() #object initialization where Tk is a claa and root is an object
root.title("PYTHON ASSISTANT") #to assign title to the application window 

def assist(): 
    text=pt.init() # initializing the engine
    r=sr.Recognizer() #initializing the recognizer
    text.say("hello. i am luca. i am your virtual assistant ")
    text.say("what can i do for you") # for audio output
    text.runAndWait() #its a loop for the engine to speak and wait
    
    
    with sr.Microphone() as source:#to use the microphone as the source
        audio=r.listen(source) #to listen to the user's input
        
        try:
            ans=r.recognize_google(audio) # using google to recognize audio
            if "name" in ans.lower():
                text.say("your name is dhamya")
                text.runAndWait()
            elif "search" in ans.lower():
                a=ans.split()
                a.remove('search')
                a.remove('for')
                if 'can' and 'you' in a:
                    a.remove('can')
                    a.remove('you')
                else:
                    pass
                n=''
                for i in range(len(a)):
                    n=n+str(a[i])+" "
                # for web search using google
                wb.open_new('https://www.google.com/search?q='+n+
                            '&ei=dozzYb2sGJ7H4-EP0uWeoA8&ved='+
                            '0ahUKEwi9v6aQ6NP1AhWe4zgGHdKyB_'+
                            'QQ4dUDCA4&uact=5&oq=flowers&gs_lcp='+
                            'Cgdnd3Mtd2l6EAMyCAgAELEDEJECMggIABCxAx'+
                            'CRAjIICAAQgAQQsQMyCAguELEDEJECMgUIABCABDIF'+
                            'CAAQgAQyBQgAEIAEMgUIABCABDIKCAAQgAQQsQMQCjI'+
                            'ICAAQgAQQsQM6BwgAELADEAo6CwgAELADEAcQChAeSg'+
                            'QIQRgBSgQIRhgAUNkDWNkDYL8JaAFwAHgAgAFqiAFq'+
                            'kgEDMC4xmAEAoAEByAEGwAEB&sclient=gws-wiz')
                text.say("searching"+n)
                text.runAndWait()
            # for telling jokes
            elif "joke" in ans.lower():
                My_joke = pyjokes.get_joke(language="en", category="neutral") 
                time.sleep(1)
                print("The joke is:")
                text.say(My_joke)
                text.runAndWait()
                print(My_joke)
            elif "song" in ans.lower():
                text.say("which song do you want to play")
                text.runAndWait()
                with sr.Microphone() as source:
                    audio=r.listen(source)
                    try:
                        song=r.recognize_google(audio)
                        pywhatkit.playonyt(song)
                        text.say("paying"+song+"on youtube")
                        text.runAndWait()
                    except():
                        text.say("could not recognise the song name")
                        text.runAndWait()
            elif "video" in ans.lower():
                text.say("which video do you want to play")
                text.runAndWait()
                with sr.Microphone() as source:
                    audio=r.listen(source)
                    try:
                        video=r.recognize_google(audio)
                        pywhatkit.playonyt(video)
                        text.say("paying"+video+"on youtube")
                        text.runAndWait()
                    except():
                        text.say("could not recognise the song name")
                        text.runAndWait()
             
            elif "time" in ans.lower():
                time=datetime.datetime.now().strftime('%H:%M')
                print("the current time is ",time)
                text.say("current time is "+time)
                text.runAndWait()
                
            elif ("who is " in ans.lower()) or ("what is " in ans.lower()):
                *a,b=ans.split()
                info=wikipedia.summary(b,)
                text.say(info)
                text.runAndWait()
            elif "bye" in ans.lower():
                text.say("bye")
                text.say("have a nice day")
                text.runAndWait()
            elif "project" in ans.lower():
                text.say("We have tried to implement all the topics our professor"+
                         " has taught us so far and it was quite insightful for us"+
                         " regarding the various applications of python, it was a"+
                         " process of learning and we had a great time throughout"+
                         " the course of this project. The fact that we could"+
                         " create our own virtual assistant was quite intriguing"+
                         " and we thank our professor for this wonderful opportunity.")
                text.runAndWait()
            else:
                text.say("this is out of my reach. sorry")
                text.runAndWait()
        except:
            text.say("sorry could not recognize your voice") 
            text.runAndWait()
    
#GUI
b1=Button(root,text="speak ",command=assist,fg="blue",bg="yellow")
b1.pack()

b2=Button(root,text="close",command=root.destroy,bg="red")
b2.pack()

root.mainloop()





