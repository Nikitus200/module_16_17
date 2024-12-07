from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel, Field

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int




@app.get("/users")
async def get_message() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
async def add_message(username: str, age: int) -> User:
    if len(users) > 0:
        user_id = len(users) + 1
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

