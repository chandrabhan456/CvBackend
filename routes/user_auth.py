from fastapi import APIRouter
from database import users_collection
from models.user_model import User
import bcrypt

router = APIRouter()

@router.post("/user/signup")
async def signup(user: User):

    existing = users_collection.find_one({
        "email": user.email
    })

    if existing:
        return {"message": "Email already exists"}

    hashed = bcrypt.hashpw(
        user.password.encode(),
        bcrypt.gensalt()
    )

    users_collection.insert_one({
        "name": user.name,
        "email": user.email,
        "password": hashed
    })

    return {"message": "User created"}

@router.post("/user/login")
async def login(user: User):

    db_user = users_collection.find_one({
        "email": user.email
    })

    if not db_user:
        return {"message": "User not found"}

    valid = bcrypt.checkpw(
        user.password.encode(),
        db_user["password"]
    )

    if not valid:
        return {"message": "Wrong password"}

    return {"message": "User login success"}