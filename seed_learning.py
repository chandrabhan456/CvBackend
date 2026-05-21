from database import db
learning_resources = [

    {
        "title": "React Frontend Development",

        "category": "Frontend",

        "description":
            "Learn React, components, hooks and routing.",

        "skills": [
            "react",
            "javascript",
            "html",
            "css"
        ],

        "link":
            "https://www.youtube.com/watch?v=bMknfKXIFA8"
    },

    {
        "title": "FastAPI Backend Mastery",

        "category": "Backend",

        "description":
            "Build APIs using Python FastAPI framework.",

        "skills": [
            "python",
            "fastapi",
            "api"
        ],

        "link":
            "https://www.youtube.com/watch?v=0sOvCWFmrtA"
    },

    {
        "title": "MongoDB Database Course",

        "category": "Database",

        "description":
            "Understand MongoDB collections and queries.",

        "skills": [
            "mongodb",
            "database"
        ],

        "link":
            "https://www.youtube.com/watch?v=ExcRbA7fy_A"
    },

    {
        "title": "AWS Cloud Fundamentals",

        "category": "Cloud",

        "description":
            "Learn AWS basics and deployment concepts.",

        "skills": [
            "aws",
            "cloud"
        ],

        "link":
            "https://www.youtube.com/watch?v=ulprqHHWlng"
    },

    {
        "title": "Docker for Beginners",

        "category": "DevOps",

        "description":
            "Containerization using Docker step by step.",

        "skills": [
            "docker",
            "devops"
        ],

        "link":
            "https://www.youtube.com/watch?v=3c-iBn73dDE"
    },

    {
        "title": "Kubernetes Crash Course",

        "category": "DevOps",

        "description":
            "Understand pods, services and deployments.",

        "skills": [
            "kubernetes",
            "devops"
        ],

        "link":
            "https://www.youtube.com/watch?v=X48VuDVv0do"
    },

    {
        "title": "Python Programming Bootcamp",

        "category": "Programming",

        "description":
            "Complete Python beginner to advanced course.",

        "skills": [
            "python"
        ],

        "link":
            "https://www.youtube.com/watch?v=_uQrJ0TkZlc"
    },

    {
        "title": "Selenium Automation Testing",

        "category": "Testing",

        "description":
            "QA automation using Selenium webdriver.",

        "skills": [
            "selenium",
            "testing"
        ],

        "link":
            "https://www.youtube.com/watch?v=j7VZsCCnptM"
    },

    {
        "title": "Tailwind CSS Full Course",

        "category": "Frontend",

        "description":
            "Modern UI design using Tailwind CSS.",

        "skills": [
            "tailwind",
            "css"
        ],

        "link":
            "https://www.youtube.com/watch?v=lCxcTsOHrjo"
    }
]

learning_collection = db["learning_resources"]

learning_collection.delete_many({})

learning_collection.insert_many(
    learning_resources
)

print("✅ Learning resources inserted")