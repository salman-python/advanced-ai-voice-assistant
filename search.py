import speech_recognition as sr
import pyttsx3
import webbrowser



engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    print("Speaking:", audio)
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(audio)
    engine.runAndWait()
    engine.stop()


def search_task(c):
    if "search" in c.lower() and "on google" in c.lower():
        query = c.replace("search","").replace("on google","").strip()
        if query:
            speak(f"Searching for {query} on goole")
            webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
            return
        
    elif "search" in c.lower() and "on youtube" in c.lower():
        query = c.replace("search","").replace("on youtube","").strip()
        if query:
            speak("Searching for {query} on youtube")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}")
            return
       