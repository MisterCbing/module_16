
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def news():
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def u_id(user_id: int):
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user')
async def id_pager(username: str = 'Donald', age: int = 50):
    return {'message': f'Информация о пользователе. Имя: {username}, возраст: {age}'}