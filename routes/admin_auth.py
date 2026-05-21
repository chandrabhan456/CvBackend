from fastapi import APIRouter
from database import admins_collection
from pydantic import BaseModel
import bcrypt

router = APIRouter()

class AdminLogin(BaseModel):
    email: str
    password: str


@router.post("/admin/login")
async def admin_login(admin: AdminLogin):

    db_admin = admins_collection.find_one({
        "email": admin.email
    })

    if not db_admin:
        return {
            "success": False,
            "message": "Admin not found"
        }

    valid_password = bcrypt.checkpw(
        admin.password.encode("utf-8"),
        db_admin["password"]
    )

    if not valid_password:
        return {
            "success": False,
            "message": "Invalid password"
        }

    return {
        "success": True,
        "message": "Admin login successful",
        "admin": {
            "email": db_admin.get("email")
        }
    }