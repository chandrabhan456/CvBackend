from fastapi import APIRouter
from database import db, users_collection

router = APIRouter()

learning_collection = db["learning_resources"]


# =====================================
# ADMIN - GET ALL LEARNING RESOURCES
# =====================================

@router.get("/admin/learning")
async def get_all_learning():

    resources = list(

        learning_collection.find(
            {},
            {
                "_id": 0
            }
        )
    )

    return {

        "success": True,

        "resources": resources
    }


# =====================================
# USER - MATCHED LEARNING
# =====================================

@router.get("/user/learning/{email}")
async def matched_learning(email: str):

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
    # LEARNING RESOURCES
    # =========================

    resources = list(

        learning_collection.find(
            {},
            {
                "_id": 0
            }
        )
    )

    matched_resources = []

    # =========================
    # MATCHING
    # =========================

    for resource in resources:

        resource_skills = [

            skill.lower()
            for skill in resource["skills"]
        ]

        matched = list(

            set(user_skills)
            &
            set(resource_skills)
        )

        if len(matched) > 0:

            match_percent = int(

                (len(matched) /
                len(resource_skills)) * 100
            )

            matched_resources.append({

                "title":
                    resource["title"],

                "category":
                    resource["category"],

                "description":
                    resource["description"],

                "skills":
                    resource["skills"],

                "link":
                    resource["link"],

                "matchedSkills":
                    matched,

                "matchPercentage":
                    match_percent
            })

    # =========================
    # SORT
    # =========================

    matched_resources.sort(
        key=lambda x: x["matchPercentage"],
        reverse=True
    )

    return {

        "success": True,

        "resources":
            matched_resources[:6]
    }