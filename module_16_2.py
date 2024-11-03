from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def news():
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def u_id(user_id: int = Path(ge = 1, le = 100, description = 'Enter User ID', examples = ['1', '33'])):
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user/{username}/{age}')
async def id_pager(username: Annotated[
    str, Path(min_length=5, max_length=20, description='Enter Username', examples=['UrbanUser', 'DonaldTrump'])],
                   age: int = Path(ge = 18, le = 120, description='Enter age', examples = [24])):
    return {'message': f'Информация о пользователе. Имя: {username}, возраст: {age}'}