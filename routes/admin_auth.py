from fastapi import APIRouter
from database import admins_collection
from models.admin_model import Admin
import bcrypt

router = APIRouter()

@router.post("/admin/login")
async def admin_login(admin: Admin):

    db_admin = admins_collection.find_one({
        "email": admin.email
    })

    if not db_admin:
        return {"message": "Admin not found"}

    valid = bcrypt.checkpw(
        admin.password.encode(),
        db_admin["password"]
    )

    if not valid:
        return {"message": "Wrong password"}

    return {"message": "Admin login success"}