from fastapi import FastAPI, Path, Request, HTTPException
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/", response_class=HTMLResponse)
async def get_main_page(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/users/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: Annotated[int, Path(description="ID of the user")]):
    user = next((user for user in users if user.id == user_id), None)
    if user:
        return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(description="ID of the user to delete")]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}")
async def post_user(
        username: Annotated[str, Path(min_length=1, description="Enter Name", example="John")],
        age: Annotated[int, Path(ge=18, description="Enter Age", example=18)]):
    user_id = users[-1].id + 1 if users else 1

    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(description="ID of the user to update")],
        username: Annotated[str, Path(min_length=1, description="Updated username")],
        age: Annotated[int, Path(ge=18, description="Updated age")]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")
