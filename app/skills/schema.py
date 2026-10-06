from db.db import Base
from sqlalchemy import Column, Integer, String, Boolean

class Skill(Base):
    __tablename__ = "skill"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    experience = Column(Integer,nullable=True)
    description = Column(String, nullable=True)


