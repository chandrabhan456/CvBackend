import os
import fitz
import bcrypt

from docx import Document
from pymongo import MongoClient
from dotenv import load_dotenv

# =========================
# LOAD ENV
# =========================

load_dotenv()

client = MongoClient(os.getenv("MONGO_URL"))

db = client["cvbuddy"]

users_collection = db["users"]

# =========================
# RESUME FOLDER
# =========================

RESUME_FOLDER = "resume_samples"

# =========================
# SKILL CATEGORIES
# =========================

TECH_SKILLS = {
    "frontend": [
        "react",
        "html",
        "css",
        "javascript",
        "typescript",
        "tailwind"
    ],

    "backend": [
        "node.js",
        "express",
        "fastapi",
        "django",
        "flask"
    ],

    "database": [
        "mongodb",
        "mysql",
        "postgresql"
    ],

    "cloud": [
        "aws",
        "azure",
        "gcp"
    ],

    "devops": [
        "docker",
        "kubernetes",
        "jenkins"
    ],

    "testing": [
        "selenium",
        "pytest",
        "jest"
    ],

    "languages": [
        "python",
        "java",
        "c++",
        "javascript"
    ]
}

# =========================
# EXTRACT TEXT
# =========================

def extract_text(file_path):

    text = ""

    # PDF
    if file_path.endswith(".pdf"):

        doc = fitz.open(file_path)

        for page in doc:
            text += page.get_text()

    # DOCX
    elif file_path.endswith(".docx"):

        doc = Document(file_path)

        text = "\n".join([
            para.text for para in doc.paragraphs
        ])

    return text


# =========================
# PARSE RESUME
# =========================

def parse_resume(text):

    lines = text.split("\n")

    name = lines[0].strip()

    lower_text = text.lower()

    # ROLE
    role = "Unknown"

    if "full stack" in lower_text:
        role = "Full Stack Developer"

    elif "frontend" in lower_text:
        role = "Frontend Developer"

    elif "backend" in lower_text:
        role = "Backend Developer"

    elif "devops" in lower_text:
        role = "DevOps Engineer"

    elif "qa" in lower_text:
        role = "QA Engineer"

    # EXPERIENCE
    experience = "Not Found"

    if "2+ years" in lower_text:
        experience = "2 years"

    elif "3+ years" in lower_text:
        experience = "3 years"

    # SKILLS
    categorized_skills = {}

    for category, skills in TECH_SKILLS.items():

        found = []

        for skill in skills:

            if skill in lower_text:
                found.append(skill)

        categorized_skills[category] = found

    return {
        "name": name,
        "role": role,
        "experience": experience,
        "skills": categorized_skills
    }


# =========================
# HASH PASSWORD
# =========================

hashed_password = bcrypt.hashpw(
    "user123".encode(),
    bcrypt.gensalt()
)

# =========================
# PROCESS ALL RESUMES
# =========================

for file_name in os.listdir(RESUME_FOLDER):

    file_path = os.path.join(
        RESUME_FOLDER,
        file_name
    )

    print(f"\nProcessing: {file_name}")

    text = extract_text(file_path)

    data = parse_resume(text)

    email = (
        data["name"]
        .lower()
        .replace(" ", "")
        + "@gmail.com"
    )

    existing_user = users_collection.find_one({
        "email": email
    })

    if existing_user:
        print("User already exists")
        continue

    users_collection.insert_one({

        "name": data["name"],

        "email": email,

        "password": hashed_password,

        "role": data["role"],

        "experience": data["experience"],

        "skills": data["skills"]
    })

    print("✅ User inserted:", data["name"])

print("\n🎉 All resumes processed successfully")