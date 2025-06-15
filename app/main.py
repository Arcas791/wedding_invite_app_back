from fastapi import FastAPI
from app.api import guests
from app.models.guest import Base
from app.db.session import engine

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Wedding Invitation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes reemplazar "*" por ["http://localhost:5000"] si quieres limitarlo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(guests.router, prefix="/guests", tags=["Guests"])