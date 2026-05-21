from fastapi import APIRouter
from database import db

router = APIRouter()

jobs_collection = db["jobs"]


# =========================
# GET ALL JOBS
# =========================

@router.get("/admin/jobs")
async def get_jobs():

    jobs = list(

        jobs_collection.find(
            {},
            {
                "_id": 0
            }
        )
    )

    return {

        "success": True,

        "jobs": jobs
    }