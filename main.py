from fastapi import FastAPI
from fastapi.responses import JSONResponse
users = [
    {
        "id": 1,
        "name": "smile",
        "pass": "1234"
        "email": "xpanisergio@gmail.com"
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