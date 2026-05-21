from pymongo import MongoClient
from dotenv import load_dotenv
import os
import bcrypt

load_dotenv()

client = MongoClient(os.getenv("MONGO_URL"))

db = client["cvbuddy"]

admins_collection = db["admins"]

email = "admin@gmail.com"
password = "admin123"

hashed_password = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)

existing_admin = admins_collection.find_one({
    "email": email
})

if existing_admin:
    print("❌ Admin already exists")

else:
    admins_collection.insert_one({
        "email": email,
        "password": hashed_password
    })

    print("✅ Admin created successfully")