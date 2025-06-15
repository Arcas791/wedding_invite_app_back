from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Guest(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    isAttending = Column(Boolean, nullable=False, default=False)
    allergies = Column(String, nullable=True)
    songRequests = Column(String, nullable=True)
    children = Column(String, nullable=True)
    tomorrowland = Column(Boolean, nullable=False, default=False)