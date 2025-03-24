from pymongo import MongoClient
from config import MONGO_URL
from models.user import User

# Connect to MongoDB
client = MongoClient(MONGO_URL)
db = client.get_database()  # Select the database
users_collection = db.users  # Select the collection

def store_user(name, age, email):
    user = User(name, age, email)
    users_collection.insert_one(user.to_dict())
    return {"message": "User stored successfully"}


from config import orders_collection, positions_collection

# Function to insert a new order into the database
def insert_order(order_data):
    orders_collection.insert_one(order_data)

def save_position(position_data):
    positions_collection.insert_one(position_data)

def get_all_positions():
    return list(positions_collection.find({}, {"_id": 0}))  # Exclude MongoDB _id



    

# Function to fetch all orders from the database
def get_all_orders():
    return list(orders_collection.find({}, {"_id": 0}))  # Exclude MongoDB's _id field
 

 
def delete_order(order_id):
    """Delete an order by order_id."""
    result = orders_collection.delete_one({"order_id": str(order_id).strip()})  # Strip any whitespace
    if result.deleted_count > 0:
        return {"status": "success", "message": f"Order {order_id} deleted successfully".strip()}
    return {"status": "error", "message": f"Order {order_id} not found".strip()}


def insert_position(position_data):
    positions_collection.insert_one(position_data)


def get_all_positions():
    return list(orders_collection.find({}, {"_id": 0}))  # Exclude MongoDB's _id field