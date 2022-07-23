from importlib.resources import path
from matplotlib.pyplot import quiverkey
from pip import main
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

#creating list
l=["it was good, what about you","it was such a hectic day","it wasn't that good","its better to not to talk about it","it was such a cheerful day"]

#write function to wish 
def wish():
    hr=int(datetime.datetime.now().hour)
    if hr>0 and hr<12:
        speak("good morning.....")
    elif hr>=12 and hr<16:
        speak("good afternoon....")
    else:
        speak("good evening.....")
    speak("hello...... i am your personal assistant..... how may i help you?")

    
#function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#take microphone inputs from the user
def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening....")
        #r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f'you said:{query}\n')
    except Exception as e:
        print("please say that again")
        return "None"
    return query
    



if __name__=="__main__":
   wish()
   while True:
       query=command().lower()
       #logic for executing task based on query
       if 'wikipedia'in query:
           speak('searching wikipedia....')
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=2)
           speak("according wikipedia")
           print(results)
           speak(results)
       elif 'what is your name' in query:
           name="alexa"
           speak(f'my name is {name}')
       elif 'how are you' in query:
           speak("i am fine, thank you, what about you")
       
       elif 'fine' in query or "i am good" in query:
           speak("It's good to know that your fine")
       
       elif 'how you doing' in query:
           speak("i am doing good..")
       
       elif 'good morning' in query:
            speak("good morning to you too")

       elif 'good afetrnoon' in query:
            speak("good afternoon to you too")
      
       elif 'good evening' in query:
            speak("good evening, how was your day")
      
       elif 'good night' in query:
            speak("good night,sweet dreams, take care, sleep well")
      
       elif 'how was your day' in query:
           d=random.choice(l)
           speak(d)
        

       elif 'open youtube' in query:
            speak("opening youtube for you")
            webbrowser.open("youtube.com")

       elif 'open google' in query:
           speak("yes sure, opening google for you")
           webbrowser.open("google.com")
      
       elif 'play a music' in query:
           path="D:\\music"
           files=os.listdir(path)
           print(files)
           d=random.choice(files)
           os.startfile(os.path.join(path,d))
       elif 'date' in query:
            today=datetime.datetime.today().strftime("%B %d %Y")
            print(today)
            speak(today)
       
       elif 'time' in  query:
           t=datetime.datetime.now().strftime("%H :%M")
           print(t)
           speak(f'the time is {t}')
       
       elif 'open microsoft wordpad' in query:
           path="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
           os.startfile(path)
       
       elif  'open chrome' in query:
           os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
           speak("opening chrome for you")


       elif 'open web WhatsApp' in query:
           webbrowser.open("https://web.whatsapp.com")
           speak("opening web whats app for you")
      
       elif 'VLC' in query:
           path="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
           os.startfile(path)

       elif 'exit' or 'quit' in query:
            speak("Thanks for giving me your time")
            exit()
       

