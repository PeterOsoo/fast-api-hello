from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"greeting": f"Hello {name}"}

@app.get("/user")
def get_user(name: str, age: int):
    return {
        "name": name,
        "age": age
    }


class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created",
        "user": user
    }
