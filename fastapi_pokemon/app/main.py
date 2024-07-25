from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from .database import get_session
from .crud import get_pokemons
from .schemas import Pokemon

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.get("/api/v1/pokemons", response_model=List[Pokemon])
async def read_pokemons(
    name: Optional[str] = None,
    type: Optional[str] = None,
    session: AsyncSession = Depends(get_session)
):
    return await get_pokemons(session, name, type)
