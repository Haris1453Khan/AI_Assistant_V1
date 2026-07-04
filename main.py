from src import API_client
from src import get_complition
import asyncio


async def main():

    client_instance = API_client()
    
    await get_complition(client_instance)


if __name__ == "__main__":
    asyncio.run(main())