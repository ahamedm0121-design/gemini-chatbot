from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL = "gemini-3.5-flash"

print(f"Chatbot ready with {MODEL}! Type 'exit' to quit.\n")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    response = client.models.generate_content(model=MODEL, contents=user)
    print(f"Bot: {response.text}\n")