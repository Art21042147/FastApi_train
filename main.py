from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Hello World"}

@app.get("/main")
async def welcome() -> dict:
    return {"message": "Main Page"}

@app.get("/user/Jonathan/Livingston")
async def news() -> dict:
    return {"message": "Hello, QA!"}

@app.get("/id")
async def id_login(username: str = "Art", age: int = 24) -> dict:
    return {"User": username, "Age": age}

@app.get("/user/{username}/{id}")
async def news(username: Annotated[str, Path(
    min_length=3, max_length=15, description="Enter your username", example="Jonathan")],
        id: int = Path(ge=0, le=100, description="Enter your id", example=13)) -> dict:
    return {"message": f"Hello, {username} {id}"}
