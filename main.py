from fastapi import FastAPI
from routes.user_auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Backend running"}