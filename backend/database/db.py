# database/db.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId

# Load environment variables
load_dotenv()

# MongoDB connection
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/legal_app")
client = MongoClient(mongo_uri)
db = client.get_database()

def get_db():
    return db

# Helper function to serialize MongoDB documents
def serialize_doc(doc):
    if doc.get("_id"):
        doc["_id"] = str(doc["_id"])
    return doc
