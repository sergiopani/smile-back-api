from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

users = [
    {
        "id": 1,
        "name": "smile",
        "pass": "1234",
        "email": "Info.smile.publicidad@gmail.com"
    }
]


users_from_web = [
    {
        "id": 1,
        "name": "Sergio",
        "pass": "1234"
    },
    {
        "id": 1,
        "name": "Jordi",
        "pass": "1234"
    },
    {
        "id": 1,
        "name": "Anonimo",
        "pass": "1234"
    },
    {
        "id": 1,
        "name": "Anonimo",
        "pass": "1234"
    }
]


class LoginRequest(BaseModel):
    email: str
    password: str


app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost:5173",
    "http://localhost:8000",
    "https://smile-admin-front-react.vercel.app"
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
        #lowe case
        email = user["email"].lower()
        login_request_email = login_request.email.lower()
        if email == login_request_email and user["pass"] == login_request.password:
            return JSONResponse(content={"message": "Login successful", "user_id": user["id"]})
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/get_users_from_web")
async def get_users_from_web():
    return JSONResponse(content={"users": users_from_web})