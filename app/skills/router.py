from fastapi import APIRouter
from db.db import async_session_maker
from .schema import Skill
from sqlalchemy import select 

router = APIRouter(
    prefix="/skills",
    tags=["skills"]
)

@router.get("/")
async def get_skills():
    async with async_session_maker() as session: 
        query = select(Skill)
        result = await session.execute(query)
        skills = result.scalars().all()
        print(f"skills: {len(skills)}")
        return skills

    


