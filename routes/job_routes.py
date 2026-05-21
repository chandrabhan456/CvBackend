from fastapi import APIRouter
from database import users_collection, db

router = APIRouter()

jobs_collection = db["jobs"]


@router.get("/user/recommended-jobs/{email}")
async def recommended_jobs(email: str):

    user = users_collection.find_one({
        "email": email
    })

    if not user:

        return {
            "success": False,
            "message": "User not found"
        }

    # =========================
    # USER SKILLS
    # =========================

    user_skills = []

    skills = user.get("skills", {})

    for category in skills.values():

        user_skills.extend(category)

    user_skills = [
        skill.lower()
        for skill in user_skills
    ]

    # =========================
    # GET JOBS
    # =========================

    jobs = list(jobs_collection.find({}, {
        "_id": 0
    }))

    recommendations = []

    # =========================
    # MATCHING
    # =========================

    for job in jobs:

        required_skills = [
            skill.lower()
            for skill in job["requiredSkills"]
        ]

        matched = list(

            set(user_skills)
            &
            set(required_skills)
        )

        match_percent = int(

            (len(matched) /
            len(required_skills)) * 100
        )

        recommendations.append({

            "company": job["company"],

            "title": job["title"],

            "description": job["description"],

            "requiredSkills":
                job["requiredSkills"],

            "matchedSkills": matched,

            "matchPercentage":
                match_percent
        })

    # =========================
    # SORT TOP MATCH
    # =========================

    recommendations.sort(
        key=lambda x: x["matchPercentage"],
        reverse=True
    )

    return {

        "success": True,

        "recommendedJobs":
            recommendations[:3]
    }