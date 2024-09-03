import os
import aiohttp
import asyncio
from dotenv import load_dotenv

load_dotenv()

PINNACLE_API_KEY = os.getenv("PINNACLE_API_KEY")
LIVESCORE_API_KEY = os.getenv("LIVESCORE_API_KEY")
API_FOOTBALL_KEY = os.getenv("API_FOOTBALL_KEY")

async def fetch_data(url, headers, params=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            return await response.json()

async def fetch_all_data():
    tasks = []

    # Define URLs and headers for different APIs
    pinnacle_url = "<https://pinnacle-odds.p.rapidapi.com/kit/v1/special-markets>"
    livescore_url = "<https://livescore6.p.rapidapi.com/v2/search>"
    football_url = "<https://api-football-v1.p.rapidapi.com/v2/odds/league/865927/bookmaker/5>"

    headers_pinnacle = {"x-rapidapi-key": PINNACLE_API_KEY}
    headers_livescore = {"x-rapidapi-key": LIVESCORE_API_KEY}
    headers_football = {"x-rapidapi-key": API_FOOTBALL_KEY}

    # Multiple requests for different football teams/leagues
    tasks.append(fetch_data(pinnacle_url, headers_pinnacle, {"is_have_odds": "true", "sport_id": "1"}))
    tasks.append(fetch_data(livescore_url, headers_livescore, {"Category": "soccer", "Query": "chel"}))
    tasks.append(fetch_data(football_url, headers_football))

    responses = await asyncio.gather(*tasks)

    return responses
  
if __name__ == "__main__":
    data = asyncio.run(fetch_all_data())
    print(data)
