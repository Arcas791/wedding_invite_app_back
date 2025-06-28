from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Guest(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    companionName = Column(String, nullable=True)
    isAttending = Column(Boolean, nullable=False, default=False)
    bus = Column(String, nullable=True, default=False)
    allergies = Column(String, nullable=True)
    songRequests = Column(String, nullable=True)
    children = Column(String, nullable=True)
    childrenNames = Column(list, nullable=True)
    childrenAges = Column(list, nullable=True)
    tomorrowland = Column(Boolean, nullable=False, default=False)
