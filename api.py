import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please check your '.env' file.")



genai.configure(api_key=api_key)

# Define generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(history=[])

# Send a message and get a response
response = chat_session.send_message()

# Print the response text
print(response.text)