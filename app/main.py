from fastapi import FastAPI
from app.api import guests
from app.models.guest import Base
from app.db.session import engine

app = FastAPI(title="Wedding Invitation API")

app.include_router(guests.router, prefix="/guests", tags=["Guests"])