from fastapi import APIRouter
from database import users_collection
from models.user_model import UserSignup, UserLogin
import bcrypt

router = APIRouter()


# USER SIGNUP
@router.post("/user/signup")
async def signup(user: UserSignup):

    existing = users_collection.find_one({
        "email": user.email
    })

    if existing:
        return {
            "success": False,
            "message": "Email already exists"
        }

    hashed = bcrypt.hashpw(
        user.password.encode(),
        bcrypt.gensalt()
    )

    users_collection.insert_one({
        "name": user.name,
        "email": user.email,
        "password": hashed
    })

    return {
        "success": True,
        "message": "User created successfully"
    }


# USER LOGIN
@router.post("/user/login")
async def login(user: UserLogin):

    db_user = users_collection.find_one({
        "email": user.email
    })

    if not db_user:
        return {
            "success": False,
            "message": "User not found"
        }

    valid = bcrypt.checkpw(
        user.password.encode(),
        db_user["password"]
    )

    if not valid:
        return {
            "success": False,
            "message": "Wrong password"
        }

    return {
        "success": True,
        "message": "User login success",
        "user": {
            "name": db_user["name"],
            "email": db_user["email"]
        }
    }