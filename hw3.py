from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


# get запрос по маршруту '/users', который возвращает словарь users.
@app.get("/users")
async def get_user():
    return users

# post запрос по маршруту '/user/{username}/{age}',
# который добавляет в словарь по максимальному по значению ключом значение строки
@app.post("/user/{username}/{age}")
async def post_user(username: str, age: int):
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    # return users
    return {f"User {user_id} is registered"}

# put запрос по маршруту '/user/{user_id}/{username}/{age}',
# который обновляет значение из словаря users под ключом user_id на строку
@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: int, username: str, age: int):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {f"The user {user_id} has been updated"}

# delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    users.pop(user_id)
    return {f"User {user_id} has been deleted"}