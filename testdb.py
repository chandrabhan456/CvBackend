# test_db.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("MONGO_URL")
print("Your URL is:", url)

try:
    client = MongoClient(url, serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    print("✅ MongoDB Connected Successfully!")
except Exception as e:
    print(f"❌ Connection Failed: {e}")