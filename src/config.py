from dotenv import load_dotenv
import os
load_dotenv()

from openai import AsyncOpenAI

def API_client():
    client = AsyncOpenAI(
        api_key = os.environ.get("DEEP_SEEK_API_KEY"),
        base_url = "https://api.deepseek.com"
    )

    return client