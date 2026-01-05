import pyttsx3
import datetime
engine = pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def speak(audio):
    print("Speaking:", audio)
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

def greet():
    time = int(datetime.datetime.now().hour)
    if time>=0 and time<=12:
        speak("Good Morning, Sir!")
    elif time>12 and time <=18:
        speak("Good Afternoon, Sir!")
    else:
        speak("Good Evening,Sir!")
