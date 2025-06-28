from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import TypeDecorator
import json

class StringList(TypeDecorator):
    impl = Text

    def process_bind_param(self, value, dialect):
        return json.dumps(value) if value is not None else None

    def process_result_value(self, value, dialect):
        return json.loads(value) if value is not None else None

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
    childrenNames = Column(StringList, nullable=True)
    childrenAges = Column(StringList, nullable=True)
    tomorrowland = Column(Boolean, nullable=False, default=False)
