from fastapi import FastAPI
from fastapi.responses import JSONResponse
users = [
    {
        "id": 1,
        "name": "smile",
        "pass": "1234"
    }
]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users")
async def get_users():
    return JSONResponse(content=users)


