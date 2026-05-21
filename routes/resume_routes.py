from fastapi import APIRouter, UploadFile, File, Form
import shutil
import os

from database import users_collection

from services.resume_parser import (
    extract_text,
    extract_resume_data
)

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/analyze-resume")
async def analyze_resume(

    email: str = Form(...),

    file: UploadFile = File(...)
):

    # =========================
    # SAVE FILE
    # =========================

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # =========================
    # EXTRACT TEXT
    # =========================

    text = extract_text(file_path)

    # =========================
    # PARSE RESUME
    # =========================

    result = extract_resume_data(text)

    # =========================
    # FIND USER
    # =========================

    user = users_collection.find_one({
        "email": email
    })

    if not user:

        return {
            "success": False,
            "message": "User not found"
        }

    # =========================
    # UPDATE USER
    # =========================

    users_collection.update_one(

        {
            "email": email
        },

        {
            "$set": {

                "name": result["name"],

                "role": result["role"],

                "experience": result["experience"],

                "skills": result["skills"],

                "resumeUploaded": True
            }
        }
    )

    return {

        "success": True,

        "message": "Resume analyzed successfully",

        "data": result
    }