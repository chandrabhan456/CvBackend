from fastapi import APIRouter
from database import users_collection

router = APIRouter()


@router.get("/admin/dashboard-stats")
async def dashboard_stats():

    users = list(users_collection.find())

    # =========================
    # TOTAL USERS
    # =========================

    total_users = len(users)

    # =========================
    # RESUME UPLOADED
    # =========================

    uploaded_resume = 0

    # =========================
    # ROLE COUNTS
    # =========================

    role_counts = {
        "Frontend": 0,
        "Backend": 0,
        "Full Stack": 0,
        "DevOps": 0,
        "QA": 0,
        "Unknown": 0
    }

    # =========================
    # EXPERIENCE COUNTS
    # =========================

    experience_counts = {
        "Fresher": 0,
        "1 Year": 0,
        "2 Years": 0,
        "3+ Years": 0
    }

    # =========================
    # SKILL COUNTS
    # =========================

    skill_counts = {}

    # =========================
    # LOOP USERS
    # =========================

    for user in users:

        # Resume uploaded
        if user.get("resumeUploaded"):
            uploaded_resume += 1

        # ---------------------
        # ROLE
        # ---------------------

        role = user.get("role", "Unknown")

        if "frontend" in role.lower():
            role_counts["Frontend"] += 1

        elif "backend" in role.lower():
            role_counts["Backend"] += 1

        elif "full stack" in role.lower():
            role_counts["Full Stack"] += 1

        elif "devops" in role.lower():
            role_counts["DevOps"] += 1

        elif "qa" in role.lower():
            role_counts["QA"] += 1

        else:
            role_counts["Unknown"] += 1

        # ---------------------
        # EXPERIENCE
        # ---------------------

        exp = user.get("experience", "").lower()

        if "1" in exp:
            experience_counts["1 Year"] += 1

        elif "2" in exp:
            experience_counts["2 Years"] += 1

        elif "3" in exp:
            experience_counts["3+ Years"] += 1

        else:
            experience_counts["Fresher"] += 1

        # ---------------------
        # SKILLS
        # ---------------------

        skills = user.get("skills", {})

        for category in skills.values():

            for skill in category:

                if skill not in skill_counts:
                    skill_counts[skill] = 0

                skill_counts[skill] += 1

    # =========================
    # RESPONSE
    # =========================

    return {

        "success": True,

        "cards": {

            "totalUsers": total_users,

            "resumeUploaded": uploaded_resume,

            "resumePending":
                total_users - uploaded_resume
        },

        "rolesChart": role_counts,

        "experienceChart": experience_counts,

        "skillsChart": skill_counts
    }