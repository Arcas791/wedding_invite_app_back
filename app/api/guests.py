from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.guest import GuestCreate, GuestOut
from app.services.guest_service import register_guest
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=GuestOut)
def create_guest_endpoint(guest: GuestCreate, db: Session = Depends(get_db)):
    return register_guest(db, guest)