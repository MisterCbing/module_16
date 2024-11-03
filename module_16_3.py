from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_all_users():
    return users

@app.get('/message/{user_id}')
async def get_user(user_id: str):
    return users[user_id]

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[
    str, Path(min_length=5, max_length=20, description='Enter Username', examples=['UrbanUser', 'DonaldTrump'])],
                   age: int = Path(ge = 18, le = 120, description='Enter age', examples = [24])):
    user_id = str(len(users) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered!'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge = 1, le = 100)], username: Annotated[
    str, Path(min_length=5, max_length=20, description='Enter Username', examples=['UrbanUser', 'DonaldTrump'])],
                   age: int = Path(ge = 18, le = 120, description='Enter age', examples = [24])):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is updated!'

@app.delete('/users/{user_id}')
async def delete_user(user_id: str):
    users.pop(user_id)
    return f'User {user_id} has been deleted!'

@app.delete('/')
async def delete_all_users():
    users.clear()
    return 'All gone.'