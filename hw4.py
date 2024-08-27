from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int


# get запрос по маршруту '/users' теперь возвращает список users.
@app.get("/users")
async def get_user()-> List[User]:
    return users

# post запрос по маршруту '/user/{username}/{age}', Добавляет в список users объект User.
# В конце возвращает созданного пользователя.
@app.post("/user/{username}/{age}")
async def post_user(username: str, age: int, user: User):
    user.id = (len(users) + 1)
    user.username = username
    user.age = age
    users.append(user)
    return user


# put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
# Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение HTTPException
@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: int, username: str, age: int) -> str:
    try:
        edit_user = users[user_id - 1]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


# delete запрос по маршруту '/user/{user_id}',
# Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение HTTPException
@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    try:
        for user in users:
            if user_id == user.id:
                users.pop(user_id-1)
                return user, f"User {user_id} has been deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
