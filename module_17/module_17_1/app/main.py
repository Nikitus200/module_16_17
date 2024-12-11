from fastapi import FastAPI
from typing import Dict
from routers import user, task



app = FastAPI()

app.include_router(user.router)
app.include_router(task.router)

@app.get("/", response_model=Dict)
async def welcome():
    return {"message": "Welcome to Taskmanager"}
