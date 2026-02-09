from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse


app = FastAPI(
    title="Hello FastAPI",
    description="My first FastAPI project for learning",
    version="1.0.0"
)



@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Hello FastAPI</title>
      </head>
      <body>
        <h1>Hello FastAPI 🚀</h1>
        <p>Welcome to my first FastAPI app</p>
      </body>
    </html>
    """



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
