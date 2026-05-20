from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URL"))

db = client["cvbuddy"]

users_collection = db["users"]
admins_collection = db["admins"]