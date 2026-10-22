from fastapi import FastAPI
from skills.router import router as skills_router
import uvicorn
from db.db import create_all

app = FastAPI()

@app.get("/")
def root():
    return {"app": "homeAPI"}
app.include_router(skills_router)

if (__name__ == "__main__"):
    create_all()
    uvicorn.run(app, host="0.0.0.0", port=8000)