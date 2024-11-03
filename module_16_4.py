from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: str
    username: str
    age: str

@app.get('/users')
async def get_all_users():
    return users

@app.get('/user/{user_id}')
async def get_user(user_id: str):
    for i in users:
        if i.id == user_id:
            return i
    raise HTTPException(status_code=404, detail='User not found')

@app.post('/user/{username}/{age}')
async def create_user(user: User, username: str, age:str):
    user.id = str(len(users) + 1)
    user.username = username
    user.age = age
    users.append(user)
    return user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username:str, age: str):
    for i in users:
        if i.id == user_id:
            i.username = username
            i.age = age
            return i
    raise HTTPException(status_code=404, detail='User not found')

@app.delete('/users/{user_id}')
async def delete_user(user_id: str):
    for i in users:
        if i.id == user_id:
            users.remove(i)
            return i
    raise HTTPException(status_code=404, detail='User not found')

@app.delete('/')
async def delete_all_users():
    users.clear()
    return 'All gone.'