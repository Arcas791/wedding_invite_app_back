from pydantic import BaseModel

class GuestCreate(BaseModel):
    name: str
    isAttending: bool
    email: str
    allergies: str
    songRequests: str
    children: str
    tomorrowland: bool

class GuestOut(GuestCreate):
    id: int

    class Config:
         from_attributes = True