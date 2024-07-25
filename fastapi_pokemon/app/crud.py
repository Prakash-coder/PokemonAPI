from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Pokemon

async def get_pokemons(session: AsyncSession, name: str = None, type: str = None):
    query = select(Pokemon)
    if name:
        query = query.filter(Pokemon.name.ilike(f"%{name}%"))
    if type:
        query = query.filter(Pokemon.type.ilike(f"%{type}%"))
    result = await session.execute(query)
    return result.scalars().all()

async def create_pokemon(session: AsyncSession, name: str, image: str, type: str):
    pokemon = Pokemon(name=name, image=image, type=type)
    session.add(pokemon)
    await session.commit()
    await session.refresh(pokemon)
    return pokemon
