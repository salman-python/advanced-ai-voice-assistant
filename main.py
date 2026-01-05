import speech_recognition as sr
import pyttsx3
import time
from tasks import command1, voice
from greetme import greet

def speak(text):
    print("Speaking:", text)
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen_command(timeout=5, phrase_time_limit=5):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            print("Listening...")
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            text = r.recognize_google(audio, language='en-US')
            print(f"You said: {text}")
            return text.lower()
        except Exception:
            return ""

if __name__ == "__main__":
    greet()
    speak("System initialized. Say wake up to start.")
    active = False
    last_active_time = 0
    idle_limit = 30  

    while True:
        if not active:
            command = listen_command(timeout=5, phrase_time_limit=4)
            if "wake up" in command:
                active = True
                speak("I am online. How can I help you?")
                last_active_time = time.time()
        else:
            command = listen_command(timeout=8, phrase_time_limit=6)

            if not command:
                now = time.monotonic()
                if now - last_active_time >= idle_limit:
                    speak("Going to sleep now.")
                    active = False
                continue

            last_active_time = time.monotonic()

            if "sleep" in command:
                speak("Going to sleep now.")
                active = False
                continue
            elif "stop" in command:
                speak("Stopping the assistant.")
                break

            if any(x in command for x in ["shutdown", "sleep"]):
                voice(command)
            else:
                command1(command)
