from pydantic import BaseModel

class GuestCreate(BaseModel):
    name: str
    email: str

class GuestOut(GuestCreate):
    id: int

    class Config:
         from_attributes = True
