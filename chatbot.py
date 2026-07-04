from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

def get_api_response(client, messages):
    
    response = client.chat.completions.create(
            messages = messages,
            model = "deepseek-v4-flash",
            temperature = 0,
            stream = False
        )
    return response.choices[0].message.content

def get_complition(client):

    state_management = [{"role" : "system" , "content" : "Act like a friendly human, Don't use any slang language. If user gives you complex task(i.e. to write code or research) than give response: 'Sorry, but I have no permission to complete this task'"}]

    print("Welcome to new the chat...\n")

    while True:
        user_input = input("You: ")
        if user_input.lower()  == "exit":
            break

        state_management.append({"role" : "user" , "content" : user_input})

        response = get_api_response(client , state_management)
        
        state_management.append({"role" : "assistant" , "content" : response})

        print(response)

def main():
    client = OpenAI(
        api_key = os.environ.get("DEEP_SEEK_API_KEY"),
        base_url = "https://api.deepseek.com"
    )
    get_complition(client)

if __name__ == "__main__":
    main()
