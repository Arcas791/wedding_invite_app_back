from pydantic import BaseModel

class GuestCreate(BaseModel):
    name: str
    isAttending: bool
    bus: str
    companionName: str
    allergies: str
    songRequests: str
    children: str
    childrenNames: list
    childrenAges: list
    tomorrowland: bool

class GuestOut(GuestCreate):
    id: int

    class Config:
         from_attributes = True