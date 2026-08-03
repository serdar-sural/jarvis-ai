from openai import OpenAI
from openai import (
    APIConnectionError,
    AuthenticationError,
    RateLimitError
)
from core.prompt_loader import get_system_prompt
from core.logger import logger
from dotenv import load_dotenv
from config import settings
import os

client = None
messages = []

def initialize_ai():
    global client
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.error("OPENAI_API_KEY was not found in the environment variables.")
        return
    client = OpenAI(api_key=api_key)
    logger.info("OpenAI client successfully initialized.")
    system_prompt = get_system_prompt()
    add_message("system", system_prompt)
    

def generate_response(chat_message):
    add_message("user", chat_message)
    try:
        response = client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=messages
        )
        assistant_message = response.choices[0].message.content
        add_message("assistant", assistant_message)
        return assistant_message
    except APIConnectionError as e:
        logger.error(f"Connection error: {e}")
        return "Entschuldigung, ich kann derzeit keine Verbindung zum Server herstellen."
    except AuthenticationError as e:
        logger.error(f"Authentication error: {e}")
        return "Entschuldigung, es gibt ein Problem mit der Authentifizierung."
    except RateLimitError as e:
        logger.error(f"Rate limit exceeded: {e}")
        return "Entschuldigung, ich erhalte zu viele Anfragen. Bitte versuchen Sie es später erneut."
    except Exception as e:
        logger.error(f"Failed to generate response: {e}")
        return "Entschuldigung, ich habe Schwierigkeiten, eine Antwort zu generieren."

def add_message(role, content):
    messages.append({
        "role": role, 
        "content": content
        })
