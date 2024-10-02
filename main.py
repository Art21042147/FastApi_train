from fastapi import FastAPI

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

@app.get("/user/{first_name}/{last_name}")
async def news(first_name: str, last_name: str) -> dict:
    return {"message": f"Hello, {first_name} {last_name}"}
