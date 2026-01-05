import pyttsx3
import os
import webbrowser
import pyautogui
import requests
import speech_recognition as sr
import time
import datetime
from chat import api
from search import search_task
API_KEY = os.getenv("NEWS_API_KEY")
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


def voice(d):
    r = sr.Recognizer()

    # Check for shutdown
    if "shutdown" in d.lower() and ("computer" in d.lower() or "laptop" in d.lower()):
        speak("Are you sure you want to shut down your laptop?")
        with sr.Microphone() as source:
            print("Listening for confirmation...")
            r.pause_threshold = 1
            r.energy_threshold = 350
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=4)
                confirm = r.recognize_google(audio).lower()
                print(f"You said: {confirm}")
            except Exception:
                confirm = ""

        if "yes" in confirm:
            speak("Shutting down the laptop.")
            time.sleep(2)
            os.system("shutdown /s /f /t 0")
        else:
            speak("Okay, cancelling shutdown.")

    # Check for sleep
    elif "sleep" in d.lower() and ("computer" in d.lower() or "laptop" in d.lower()):
        speak("Are you sure you want to put your laptop to sleep?")
        with sr.Microphone() as source:
            print("Listening for confirmation...")
            r.pause_threshold = 1
            r.energy_threshold = 300
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=4)
                confirm = r.recognize_google(audio).lower()
                print(f"You said: {confirm}")
            except Exception:
                confirm = ""

        if "yes" in confirm:
            speak("Putting the laptop to sleep.")
            time.sleep(2)
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        else:
            speak("Okay, cancelling sleep.")




def command1(c):
    TASKS = {
        "google": ["open google", "launch google", "go to google"],
        "youtube": ["open youtube", "launch youtube", "go to youtube"],
        "facebook": ["open facebook", "launch facebook", "go to facebook"],
        "chatgpt": ["open chat", "open chatgpt", "launch chatgpt"]
    }
    for j, k in TASKS.items():
        if any(l in c.lower() for l in k):
            urls = {
                "google": "https://google.com",
                "youtube": "https://youtube.com",
                "facebook": "https://facebook.com",
                "chatgpt": "https://chatgpt.com"
            }
            webbrowser.open(urls[j])
            speak(f"Opening {j}")
            return

    if c.lower().startswith("play"):
        o = c.lower().split(" ")[1]
        l = dir.d[o]
        webbrowser.open(l)


    elif "search" in c.lower() and "on google" in c.lower():
        t = c.lower()
        query = t.replace("search","").replace("on google","").strip()
        if query:
            speak(f"Searching for {query} on google")
            webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
            return True
        

    elif "search" in c.lower() and "on youtube" in c.lower():
        t = c.lower()
        query = t.replace("search","").replace("on youtube","").strip()
        if query:
            speak(f"Searching for {query} on youtube")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}")
            return True

    elif "tell me news" in c.lower():
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for article in data.get("articles", []):
                speak(article["title"])


    elif "close google" in c.lower():
        os.system("taskkill /im chrome.exe /f")
    elif "close tab" in c.lower():
        time.sleep(1)
        pyautogui.hotkey('ctrl','w')


    elif "close the program" in c.lower():
        time.sleep(0.8)
        pyautogui.click(1033,450)
        time.sleep(1)
        pyautogui.hotkey('alt','f4')
    elif "close the tab" in c.lower():
        time.sleep(0.8)
        pyautogui.click(1033,450)
        time.sleep(1)
        pyautogui.hotkey('ctrl','w')
    elif "minimize" in c.lower() or "minimise" in c.lower():
        time.sleep(0.8)
        pyautogui.click(1033,450)
        time.sleep(1)
        pyautogui.hotkey('winleft','d')
    elif "time batana" in c.lower() or "time kia hua" in c.lower():
        strf= datetime.datetime.now().strftime("%H:%M%S")
        speak(f"Sir, The Time is {strf}")
    
    elif "ai" in c.lower():
        output = api(c)
        h = output
        print(h)
        speak(output)
