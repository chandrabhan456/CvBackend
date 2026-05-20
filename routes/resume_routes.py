from fastapi import APIRouter, UploadFile, File
import shutil
import os

from services.resume_parser import (
    extract_text,
    extract_resume_data
)

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)

    result = extract_resume_data(text)

    return result