from fastapi import APIRouter, status, HTTPException
from db.db import engine, async_session_maker
from .schema import Skill, SkillDTO
from .models import SkillDTO
# from sqlalchemy.orm import Session
# from sqlalchemy import select
from sqlmodel import Session, select

router = APIRouter(
    prefix="/skills",
    tags=["skills"]
)

@router.get("/")
async def get_skills():
        async with async_session_maker() as session:
            statement = select(Skill)
            results = await session.execute(statement)
            skills = []
            for result in results:
                 print(f"result: {result[0]}")
                # skill = Skill(result.id, result.title, result.experience, result.description)
                #  skill = Skill(result)
                #  result[1] = int(result[1])
                 skills.append(result[0])
            # print(f"results: {skills}")
            return skills
            #skills = await results.all()
            
            #skills = session.execute(query).all()
            # print(f"skills: {skills}")
            

@router.post("/add/")
def create_skill(skill: SkillDTO):
    with Session(engine) as session:
        try:
          dbskill = Skill(id=0,title=skill.title, experience=skill.experience,description=skill.description)
          session.add(dbskill)
          session.commit()
          return {"skill": skill.title}
        except Exception as ex:
         print("exception: ", ex)
         raise HTTPException(status_code=501, detail=f"ex : {ex}")
        finally:
          session.close()
    

  


     



    


