from sqlalchemy.orm import Session
from app.schemas.guest import GuestCreate
from app.repositories.guest_repository import create_guest

def register_guest(db: Session, guest: GuestCreate):
    return create_guest(db, guest)