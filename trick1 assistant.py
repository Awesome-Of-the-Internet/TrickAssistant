# This is made and copyrighted by Tricky. Hahahahahaha !!!!!
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import wolframalpha
import sys
from selenium import webdriver

print("Initializing Trick...")
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('Your_App_ID')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
song_number = random.randint(0, 0)

# this function will pronounce the string in it.
def speak(text):
    engine.say(text)
    engine.runAndWait()


# this function will wish me as per the current time.
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Tricky')
        print('Good Morning Tricky')
    elif hour >= 12 and hour< 18:
        speak('Good Afternoon Tricky')
        print('Good Afternoon Tricky')
    else:
        speak('Good Evening Tricky')
        print('Good Evening Tricky')


# this function will take command from the microphone.
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry Tricky! I didn\'t get that! Try typing the query!')
        print('Sorry Tricky! I didn\'t get that! Try typing the query!')
        query = str(input('Query: '))

    return query


# main program
speak('initializing trick')
wish_me()
speak('I am Trick. How may I help you?')

# logic for executing basic tasks
name =  Tricky"
if name ==  Tricky':

    while True:

        query = myCommand()
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('www.google.com')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')


        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'play music' in query:
            songs_dir = "E:\\Tricky\ Tricky songs"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is{strTime}")

        elif 'open timer' in query or 'open cstimer' in query or 'open CS timer' in query.lower():
            speak('okay')
            brave_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(brave_path).open('www.cstimer.net')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak("Bye Tricky, have a good day!")
            sys.exit()

        elif 'hello' in query:
            speak('Hello Tricky')

        elif"thanks"in query or 'thank you'in query or 'thank'in query:
            speak("you're welcome Tricky!")

        elif 'bye' in query:
            speak('Bye Tricky, have a good day.')
            sys.exit()

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got..  it.')
                    print(results)
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    print(results)
                    speak(results)

            except:
                speak("sorry, I couldnt find that. Here are the results on google.")
                brave_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(brave_path).open(f'https://www.google.com/search?q={query}')

        speak('Next Query Tricky!')
