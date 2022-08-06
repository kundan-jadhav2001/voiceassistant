#System need internet connection to work
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 140)
engine.setProperty('volume', 300)

def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<16:
        speak('Good Afternoon')
    elif hour>=16 and hour<19:
        speak('Good Evening')
    else:
        speak('Good Night')
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('Listening...')
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query

if __name__=="__main__":
    #speak("hii there")
    print('Initializing system...')
    speak('Initializing system...')
    wishme()
    print('system is online...')
    speak('system is online...')
    
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences =2)
            print(results)
            speak(results)
        elif 'open youtube' in query:
            url = 'www.youtube.com'
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            speak('opening youtube')
            print('opening youtube')
            webbrowser.get(chrome_path).open(url)
        elif 'gaana' in query:
            url = 'gaana.com'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak('opening gaana')
            print('opening gaana')
            webbrowser.get(chrome_path).open(url)
            #webbrowser.open('www.gaana.com')
        elif 'open google' in query:
            url = 'www.google.com'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak('opening google')
            print('opening google')
            webbrowser.get(chrome_path).open(url)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'music' in query:
            x = random.randrange(0,45)
            #print(random.random())#To print random integers betn 0 to 1
            songs_dir = "D:\\Songs\\shortcuts"
            songs = os.listdir(songs_dir)
            speak('playing songs')
            print('playing songs')
            print(x)
            os.startfile(os.path.join(songs_dir, songs[0+x]))
            #print(songs)

        elif 'song' in query:
            x = random.randrange(0,45)
            #print(random.random())#To print random integers betn 0 to 1
            songs_dir = "D:\\Songs\\shortcuts"
            songs = os.listdir(songs_dir)
            speak('playing songs')
            print('playing songs')
            print(x)
            os.startfile(os.path.join(songs_dir, songs[0+x]))
            #print(songs)

        elif 'shutdown' in query:
            speak('shutting down system, have a good day...')
            print('shutting down system, have a good day...')
            sys.exit()
        elif 'hi there' in query:
            speak('hello there... how may i help?')
            print('hello there... how may i help?')
        else:
            speak('unable to help')
            print('unable to help')
