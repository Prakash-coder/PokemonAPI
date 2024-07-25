import asyncio
import httpx
from app.database import async_session
from app.crud import create_pokemon
from contextlib import asynccontextmanager

@asynccontextmanager
async def get_session():
    async with async_session() as session:
        yield session

async def fetch_and_store_pokemons():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://pokeapi.co/api/v2/pokemon?limit=100")
        pokemons = response.json()["results"]

        async with get_session() as session:
            for poke in pokemons:
                details = await client.get(poke["url"])
                details_json = details.json()
                name = details_json["name"]
                image = details_json["sprites"]["front_default"]
                types = ", ".join(t["type"]["name"] for t in details_json["types"])
                await create_pokemon(session, name, image, types)

if __name__ == "__main__":
    asyncio.run(fetch_and_store_pokemons())
