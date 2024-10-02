from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Hello World"}

@app.get("/main")
async def welcome() -> dict:
    return {"message": "Main Page"}

@app.get("/user/{first_name}/{last_name}")
async def news(first_name: str, last_name: str) -> dict:
    return {"message": f"Hello, {first_name} {last_name}"}
