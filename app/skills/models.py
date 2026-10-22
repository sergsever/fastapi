from pydantic import BaseModel

class SkillDTO(BaseModel):
    title: str
    experience: int
    description: str