"""
API module for the app
"""
from typing import List
from movie import Movie
import aiohttp
import asyncio

async def fetch_data(media_type: str, time_period: str) -> List[Movie]:
    token_file = open("token.txt", "r") 
    token = token_file.read()
    token_file.close()

    url = f"https://api.themoviedb.org/3/trending/{media_type}/{time_period}"
    headers = {"Authorization" : "Bearer " + token}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            data = data['results']
            if media_type == 'movie':
                data = [Movie(item['title'], item['vote_average']) for item in data]
            elif media_type == 'tv':
                data = [Movie(item['name'], item['vote_average']) for item in data]

    return data
