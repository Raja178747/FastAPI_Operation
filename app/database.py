from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")
print(MONGO_DETAILS,"-==========MONGO_DETAILS==========")
client = MongoClient(MONGO_DETAILS)

try:
    client.admin.command('ping')
    print("Connected to MongoDB Atlas!")
    database = client["fastapi_db"]
    item_collection = database["items"]
    clock_in_collection = database["clock_in_records"]
except Exception as e:
    print("Could not connect to MongoDB Atlas:", e)
