from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Ensure MongoDB URL is loaded correctly
MONGO_URL = os.getenv("MONGO_URL")
if not MONGO_URL:
    raise ValueError("MONGO_URL is not set in environment variables!")

# Connect to MongoDB and explicitly select a database
client = MongoClient(MONGO_URL)
db = client["algo-trading"]  # Explicitly specify database name here

# Define collections
orders_collection = db["orders"]
positions_collection = db["positions"]
