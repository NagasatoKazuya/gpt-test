from sqlalchemy import Column, Integer, String
from database import Base

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    votes = Column(Integer, default=0)
