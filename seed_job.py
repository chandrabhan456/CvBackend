from database import db

jobs_collection = db["jobs"]
jobs = [

    {
        "company": "TechNova Solutions",
        "title": "Frontend Developer",
        "description": "React frontend developer required",
        "requiredSkills": [
            "react",
            "javascript",
            "html",
            "css"
        ]
    },

    {
        "company": "CloudMatrix",
        "title": "Backend Developer",
        "description": "FastAPI backend developer",
        "requiredSkills": [
            "python",
            "fastapi",
            "mongodb"
        ]
    },

    {
        "company": "ByteFusion Labs",
        "title": "Full Stack Developer",
        "description": "MERN stack developer",
        "requiredSkills": [
            "react",
            "node.js",
            "mongodb"
        ]
    },

    {
        "company": "DevSync Technologies",
        "title": "DevOps Engineer",
        "description": "Cloud deployment engineer",
        "requiredSkills": [
            "docker",
            "aws",
            "kubernetes"
        ]
    },

    {
        "company": "QualitySphere",
        "title": "QA Engineer",
        "description": "Software testing engineer",
        "requiredSkills": [
            "selenium",
            "pytest",
            "testing"
        ]
    },

    {
        "company": "CodeCraft Systems",
        "title": "Python Developer",
        "description": "Python API developer",
        "requiredSkills": [
            "python",
            "django",
            "mongodb"
        ]
    },

    {
        "company": "SkyNet Cloud",
        "title": "Cloud Engineer",
        "description": "AWS cloud infrastructure engineer",
        "requiredSkills": [
            "aws",
            "docker",
            "linux"
        ]
    },

    {
        "company": "PixelMind Studio",
        "title": "React Developer",
        "description": "Modern React UI developer",
        "requiredSkills": [
            "react",
            "tailwind",
            "typescript"
        ]
    },

    {
        "company": "DataNest Technologies",
        "title": "Database Engineer",
        "description": "Database management engineer",
        "requiredSkills": [
            "mongodb",
            "mysql",
            "postgresql"
        ]
    }
]

jobs_collection.insert_many(jobs)

print("✅ 9 Jobs Inserted")