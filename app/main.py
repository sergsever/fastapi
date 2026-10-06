from fastapi import FastAPI
from skills.router import router as skills_router

app = FastAPI()

@app.get("/")
def root():
    return {"app": "homeAPI"}
app.include_router(skills_router)