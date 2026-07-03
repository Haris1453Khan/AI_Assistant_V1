from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

def get_compilation(prompt , model="deepseek-v4-flash") :
    client = OpenAI(
        api_key = os.environ.get("DEEP_SEEK_API_KEY"),
        base_url = "https://api.deepseek.com"
    )

    messages = [{"role" : "user" , "content" : prompt}]

    response = client.chat.completions.create(
        messages= messages,
        model = model,
        temperature = 0,
        stream = False,
    )

    print(response.choices[0].message.content)

text = "My name is Muhammad Haris Khan. I am 21 years old, currently I am doing bachelors in computer science from FAST NUCES Karachi. In my summer break I follow the AI Engineer road map to prepare for this role."

prompt = f"""Make a short summary for the text present in the triple backtiks. Make sure the response length is at most 50 characters.```{text}```
"""

get_compilation(prompt);