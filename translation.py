import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_to_swedish(text):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Translate the English text to Swedish."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content