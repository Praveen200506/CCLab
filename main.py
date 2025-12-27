from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



@app.get("/")
def home():
    return {"message": "Welcome to the Home endpoint"}

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI!"}


class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(data: LoginRequest):
    return {
        "username": data.username,
        "message": "Login data received"
    }
