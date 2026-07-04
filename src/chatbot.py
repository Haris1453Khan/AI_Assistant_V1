import asyncio
from openai import APIError


async def get_api_response(client, messages):
    
    try:
        response = await client.chat.completions.create(
            messages = messages,
            model = "deepseek-v4-flash",
            temperature = 0,
            stream = False
        )
        return response.choices[0].message.content
    
    except APIError as error:
        print("System Error: Unable to connect with AI server\n")
        return  f"Error from the server: {error}"

async def get_complition(client):

    state_management = [{"role" : "system" , "content" : "Act like a friendly human, Don't use any slang language. If user gives you complex task(i.e. to write code or research) than give response: 'Sorry, but I have no permission to complete this task'"}]

    print("Welcome to new the chat...\n")

    while True:
        loop = asyncio.get_event_loop()
        user_input = await loop.run_in_executor(None , input , "You: ")
        if user_input.lower()  == "exit":
            break

        state_management.append({"role" : "user" , "content" : user_input})

        response = await get_api_response(client , state_management)
        
        state_management.append({"role" : "assistant" , "content" : response})

        print(response)


