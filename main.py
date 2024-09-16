from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str

users = [
    {
        "id": 1,
        "email": "anonimo@example.com",
        "pass": "1234"
    },
    {
        "id": 2,
        "email": "usuario2@example.com",
        "pass": "abcd"
    }
]

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://yourdomain.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/login")
async def login(login_request: LoginRequest):
    for user in users:
        if user["email"] == login_request.email and user["pass"] == login_request.password:
            return JSONResponse(content={"message": "Login successful", "user_id": user["id"]})
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/get_users_from_web")
async def get_users_from_web():
    return JSONResponse(content={"users": users_from_web})