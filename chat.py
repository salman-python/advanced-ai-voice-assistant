import pyttsx3
import google.generativeai as genai
import os
from dotenv import load_dotenv


# ---- pyttsx3 setup ----
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def api(c):
    load_dotenv()

    api_key = os.getenv("GENAI_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please check your '.env' file.")

    # Suppress gRPC warnings
    os.environ["GRPC_VERBOSITY"] = "ERROR"
    os.environ["GRPC_CPP_MIN_LOG_LEVEL"] = "2"

    genai.configure(api_key=api_key)

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(f"{c} Answer me in short, not more than 3–4 lines.")
    return response.text
