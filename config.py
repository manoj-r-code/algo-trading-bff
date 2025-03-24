from pymongo import MongoClient
import os

from dotenv import load_dotenv

load_dotenv()

# Load MongoDB URL from environment variables
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

# Connect to MongoDB
client = MongoClient(MONGO_URL)
db = client["algo-trading"] 
orders_collection = db["orders"]  
positions_collection = db["positions"] 

