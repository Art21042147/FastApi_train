from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def post_user(
    username: Annotated[str, Path(min_length=1, description="Enter Name", example="John")],
    age: Annotated[int, Path(ge=18, description="Enter Age", example=18)]):
    user_id = str(max(map(int, users.keys())) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[str, Path(description="ID of the user to update")],
    username: Annotated[str, Path(min_length=1, description="Updated username")],
    age: Annotated[int, Path(ge=18, description="Updated age")]):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} has been updated"

@app.delete("/user/{user_id}")
async def delete_user(
    user_id: Annotated[str, Path(description="ID of the user to delete")]):
    del users[user_id]
    return f"User {user_id} has been deleted"
