from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.database import get_session
from app.crud import get_pokemons
from app.schemas import Pokemon

router = APIRouter()

@router.get("/pokemons", response_model=List[Pokemon])
async def read_pokemons(
    name: Optional[str] = None,
    type: Optional[str] = None,
    session: AsyncSession = Depends(get_session)
):
    return await get_pokemons(session, name, type)
