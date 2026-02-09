from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/ping")
def ping():
    return {"status": "ok"}
