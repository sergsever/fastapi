from __future__ import annotations

from typing import Optional
from dataclasses import dataclass, field
from typing import List

# from sqlalchemy import Column, ForeignKey, Integer, String

# from sqlalchemy.orm import registry, relationship
from sqlmodel import Field, Session, SQLModel, create_engine, Column, BigInteger
from pydantic import BaseModel

# mapper_registry = registry()

# @mapper_registry.mapped
@dataclass
class Skill(SQLModel, table=True):
    __tablename__ = "skill"
    id: int = Field(default=None, sa_column=Column(BigInteger(), primary_key=True))
    title: str # = field(default=None, metadata={"": Column(String(256))})
    experience: int | None = None # = field(init=False, metadata={"": Column(Integer, primary_key=False)})
    description: str # = field(default=None, metadata={"": Column(String(256))})

class SkillDTO(BaseModel):
    title:str
    experience:int
    description:str  