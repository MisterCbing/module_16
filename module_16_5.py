
from fastapi import FastAPI, HTTPException, Body, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory= "templates")
app = FastAPI()

users = []

class User(BaseModel):
    id: str
    username: str
    age: str

for i in range(1,4):
    user = User(id = str(i), username = 'user' + str(i), age = str(30 + i))
    users.append(user)

@app.get('/')
async def get_all_users(request: Request):
    return templates.TemplateResponse("users.html", {"request":request, "users": users})

@app.get('/user/{user_id}')
async def get_user(request: Request, user_id: str):
    for i in users:
        if i.id == user_id:
            return templates.TemplateResponse("users.html", {"request":request, "user": i})
    raise HTTPException(status_code=404, detail='User not found')

@app.post(path='/')
async def create_user(request: Request, user: str = Form(), age: str = Form()):
    users.append(User(id=str(len(users) + 1), username=user, age=age))
    return templates.TemplateResponse("users.html", {"request":request, "users": users})

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