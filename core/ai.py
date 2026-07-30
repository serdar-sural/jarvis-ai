from openai import OpenAI
from openai import (
    APIConnectionError,
    AuthenticationError,
    RateLimitError
)
from prompt_loader import get_system_prompt
from dotenv import load_dotenv
import os

client = None
MODEL_NAME = "gpt-5.6-terra"
messages = []

def initialize_ai():
    global client
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Fehler: OPENAI_API_KEY nicht in Umgebungsvariablen gefunden.")
        return
    client = OpenAI(api_key=api_key)
    print("OpenAI client erfolgreich initialisiert.")
    system_prompt = get_system_prompt()
    add_message("system", system_prompt)
    

def generate_response(chat_message):
    add_message("user", chat_message)
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages
        )
        assistant_message = response.choices[0].message.content
        add_message("assistant", assistant_message)
        return assistant_message
    except APIConnectionError as e:
        print(f"Verbindungsfehler: {e}")
        return "Entschuldigung, ich kann derzeit keine Verbindung zum Server herstellen."
    except AuthenticationError as e:
        print(f"Authentifizierungsfehler: {e}")
        return "Entschuldigung, es gibt ein Problem mit der Authentifizierung."
    except RateLimitError as e:
        print(f"Rate Limit Fehler: {e}")
        return "Entschuldigung, ich erhalte zu viele Anfragen. Bitte versuchen Sie es später erneut."
    except Exception as e:
        print(f"Fehler beim Generieren der Antwort: {e}")
        return "Entschuldigung, ich habe Schwierigkeiten, eine Antwort zu generieren."

def add_message(role, content):
    messages.append({
        "role": role, 
        "content": content
        })
