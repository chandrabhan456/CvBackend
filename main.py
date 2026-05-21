from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ROUTERS
from routes.user_auth import router as user_router
from routes.admin_auth import router as admin_router
from routes.resume_routes import router as resume_router
from routes.admin_dashboard import router as dashboard_router
from routes.admin_users import router as users_router
from routes.job_routes import router as job_router
from routes.admin_jobs import router as jobs_router
from routes.learning_routes import router as learning_router
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# USER AUTH APIs
app.include_router(user_router)

# ADMIN AUTH APIs
app.include_router(admin_router)

# RESUME ANALYZER APIs
app.include_router(resume_router)

app.include_router(dashboard_router)

app.include_router(users_router)
app.include_router(job_router)
app.include_router(jobs_router)
app.include_router(learning_router)

@app.get("/")
def home():
    return {
        "success": True,
        "message": "CV Buddy Backend Running 🚀"
    }