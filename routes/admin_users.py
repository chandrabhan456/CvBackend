from fastapi import APIRouter
from database import users_collection

router = APIRouter()


# =========================
# GET ALL USERS
# =========================

@router.get("/admin/users")
async def get_users():

    users = list(

        users_collection.find(
            {},
            {
                "_id": 0,
                "password": 0
            }
        )
    )

    return {
        "users": users
    }


# =========================
# GET SINGLE USER
# =========================

@router.get("/admin/user/{email}")
async def get_single_user(email: str):

    user = users_collection.find_one(
        {"email": email},
        {
            "_id": 0,
            "password": 0
        }
    )

    if not user:

        return {
            "success": False,
            "message": "User not found"
        }

    return {
        "success": True,
        "user": user
    }