from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome():
    return {"Главная страница"}

@app.get("/user/admin")
async def hi_admin():
    return {"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def hi_user(user_id: str):
    return {f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def inf_user(username:str, age: str):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
