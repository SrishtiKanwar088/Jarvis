import pyttsx3
import speech_recognition
from GreetMe import greetMe
import requests
from bs4 import BeautifulSoup 
import datetime

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r= speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        r.energy_threshold =300
        audio = r.listen(source,0,4)

    try:
        print("Understanding....")
        query= r.recognize_google(audio,language='en-in')
        print(f"You asked: {query}\n")
    except Exception as e:
        print("Can you repeat please")
        return ""
    return query.lower()

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok Boss , You can me call anytime")
                    break          

                elif "hello" in query:
                    speak("Hello Boss, How are you?")
                elif "i am fine" in query:
                    speak("that's great boss")
                elif "how are you?" in query:
                    speak("I am good, boss")
                elif "thank you " in query:
                    speak("My Pleasure, Boss")  

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb()

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)                      

                elif "temprature" in query:
                    search = "temprature in jaipur"  
                    url= f"https://www.google.com/search?q={search}" 
                    r = requests.get(url)
                    data=BeautifulSoup(r.text,"html.parser") 
                    temp=data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "weather" in query:
                    search = "weather in jaipur"  
                    url= f"https://www.google.com/search?q={search}" 
                    r = requests.get(url)
                    data=BeautifulSoup(r.text,"html.parser") 
                    wea=data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {wea}")    
                
                elif "the time" in query:
                    strTime= datetime.datetime.now().strftime("%H:%M")
                    speak(f"Boss, the time is {strTime}")

                elif "finally sleep" in query:
                    speak("Going to sleep")
                    exit()    