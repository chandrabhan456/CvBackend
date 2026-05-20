import fitz
from docx import Document
import re

TECH_SKILLS = {
    "frontend": ["react", "html", "css", "javascript", "typescript", "next.js"],
    "backend": ["node.js", "express", "fastapi", "django", "flask"],
    "database": ["mongodb", "mysql", "postgresql"],
    "cloud": ["aws", "azure", "gcp"],
    "devops": ["docker", "kubernetes", "jenkins"],
    "testing": ["selenium", "jest", "pytest"],
    "languages": ["python", "java", "c++", "javascript"]
}

def extract_text(file_path):

    if file_path.endswith(".pdf"):
        doc = fitz.open(file_path)

        text = ""

        for page in doc:
            text += page.get_text()

        return text

    elif file_path.endswith(".docx"):
        doc = Document(file_path)

        text = "\n".join([p.text for p in doc.paragraphs])

        return text

    return ""


def extract_resume_data(text):

    lower_text = text.lower()

    # NAME (simple first line approach)
    lines = text.split("\n")
    name = lines[0].strip() if lines else "Unknown"

    # EXPERIENCE
    exp_match = re.search(r'(\d+)\+?\s+years?', lower_text)

    experience = exp_match.group(0) if exp_match else "Not Found"

    # SKILLS
    categorized_skills = {}

    for category, skills in TECH_SKILLS.items():

        found = []

        for skill in skills:
            if skill in lower_text:
                found.append(skill)

        categorized_skills[category] = found

    # ROLE DETECTION
    role = "Unknown"

    if categorized_skills["frontend"] and categorized_skills["backend"]:
        role = "Full Stack Developer"

    elif categorized_skills["frontend"]:
        role = "Frontend Developer"

    elif categorized_skills["backend"]:
        role = "Backend Developer"

    elif categorized_skills["devops"]:
        role = "DevOps Engineer"

    return {
        "name": name,
        "role": role,
        "experience": experience,
        "skills": categorized_skills
    }