from fastapi import FastAPI

from routes.user_auth import router as auth_router
from routes.resume_routes import router as resume_router

app = FastAPI()

# Auth APIs
app.include_router(auth_router)

# Resume APIs
app.include_router(resume_router)

@app.get("/")
def home():
    return {
        "message": "Backend running"
    }