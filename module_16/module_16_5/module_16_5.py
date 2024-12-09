from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
from pydantic import BaseModel, Field

app = FastAPI()

template = Jinja2Templates(directory="templates")


users = []

class User(BaseModel):
    id: int
    username: str
    age: int



@app.get("/")
async def get_users(request: Request) -> HTMLResponse:
    return template.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
async def get_message(request: Request, user_id: int) -> HTMLResponse:
     if users:
        for i in users:
            if i.id == user_id:
                return template.TemplateResponse("users.html", {"request": request, "user": i})
        raise HTTPException(status_code=404, detail="User was not found")
     else:
         raise HTTPException(status_code=1000-7, detail="Create user, users is empty")

@app.post("/user/{username}/{age}")
async def add_message(username: str, age: int) -> User:
    if len(users) > 0:
        user_id = max(users, key=lambda x: x.id).id + 1
    else:
        user_id = 1
    users.append(User(id = user_id, username = username, age= age))
    return users[user_id - 1]

@app.put("/user/{user_id}/{username}/{age}")
async def update_message(user_id: int, username: str, age: int) -> User:
        for i in users:
            if user_id == i.id:
                users[users.index(i)].username, users[user_id - 1].age = username, age
                return users[users.index(i)]
        raise HTTPException(status_code=404, detail="User was not found")





@app.delete("/user/{user_id}")
async def delete_message(user_id: int) -> User:
    for i in users:
        if user_id == i.id:
            users.remove(i)
            return i
    raise HTTPException(status_code=404, detail="User was not found")

