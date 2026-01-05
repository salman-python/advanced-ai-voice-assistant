# 🤖 AI Voice Assistant (Mega Project)

A **Python-based AI Voice Assistant** inspired by **Jarvis**, built with speech recognition, text-to-speech, automation, and AI-powered responses.  
The assistant listens for a **wake word**, processes voice commands, performs tasks, and intelligently goes idle when not in use.

This project demonstrates **real-time voice interaction**, **modular design**, and **advanced assistant behavior**.

---

## ✨ Key Highlights

- 🎙 **Wake Word Detection** (`"wake up"`)
- 🗣 **Speech-to-Text** using Google Speech Recognition
- 🔊 **Text-to-Speech** with Pyttsx3 (SAPI5)
- 🧠 **Command Processing System**
- ⏳ **Idle Detection & Auto Sleep Mode**
- 🔁 **Continuous Listening Loop**
- 🧩 **Modular & Scalable Architecture**
- 🤖 **AI-powered responses (Google Generative AI)**
- 🖱 **Automation & System Control**
- 🌦 **Weather Information**
- 🔍 **Search Capabilities**
- 📝 **Task Handling System**

---

## 🧠 How the Assistant Works

1. The system **starts in sleep mode**
2. It continuously listens for the **wake word**
3.  wake up

- Once activated:
- The assistant listens for user commands
- Executes tasks via different modules
4. If the assistant is **idle for 30 seconds**, it automatically goes back to sleep
5. Commands like:
- `sleep` → puts assistant to sleep
- `stop` → completely shuts down the assistant

---

## 📁 Project Structure

├── main.py # Core logic, wake word, idle handling

├── tasks.py # Command execution & automation logic

├── greetme.py # Startup greetings

├── chat.py # AI chat responses

├── api.py # API-based features

├── search.py # Web/search operations

├── weather.py # Weather information

├── test.py # Testing & experiments

├── requirements.txt # Dependencies

├── .env # API keys (ignored)

├── example.env # Sample environment variables

├── .venv/ # Virtual environment (ignored)

└── pycache/ # Cache files (ignored)

---

## ⚙️ Requirements

All dependencies are listed in `requirements.txt`:

pyttsx3
pyautogui
requests
SpeechRecognition
google-generativeai
python-dotenv


---
``` 2️⃣ Create Virtual Environment (Recommended)

python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```
3️⃣ Install Dependencies
bash
pip install -r requirements.txt
🔑 Environment Variables
Create a .env file using example.env:

env
GOOGLE_API_KEY=your_api_key_here
⚠️ Never upload .env to GitHub

▶️ Running the Assistant
Start the assistant using:

bash
python main.py
Example Flow
vbnet

Assistant: System initialized. Say wake up to start.
User: wake up
Assistant: I am online. How can I help you?
User: what's the weather today?
Assistant: (Responds with weather info)
🛑 Voice Commands
Command	Action
wake up	---> Activate assistant
sleep ---->	Put assistant to sleep
stop---->	Stop program completely
Other commands	Handled by task system


📜 License

This project is intended for learning, experimentation, and personal use.


## 👤 Author

**Muhammad Salman Kazam**  
Python Developer | AI & Automation Enthusiast  

- GitHub: https://github.com/salman-python
- Email: smpmine159@gmail.com

