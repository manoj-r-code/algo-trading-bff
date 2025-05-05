from flask import Blueprint
from services.basic import delete_order, get_all_orders, get_all_positions, insert_order, save_position, store_user

kite_routes = Blueprint('kite_routes', __name__)

@kite_routes.route('/') 
def home():
    return "Hello, Flask with Routes!"

@kite_routes.route('/ping') 
def ping():
    return "pong!"

@kite_routes.route('/about')
def about():
    return "This is the About Page for Kite."

from flask import Blueprint, request, jsonify



@kite_routes.route('/store-user', methods=['POST'])
def store_user_route():
    data = request.json
    if not data or "name" not in data or "age" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400

    result = store_user(data["name"], data["age"], data["email"])
    return jsonify(result), 201



# Route to add a new order
@kite_routes.route('/add-orders', methods=['POST'])
def add_order():
    order_data = request.get_json()  # Get JSON data from request
    insert_order(order_data)  # Store in DB
    return jsonify({"status": "success", "message": "Order added successfully!"}), 201

# Route to fetch all orders from MongoDB
@kite_routes.route('/get-orders', methods=['GET'])
def fetch_orders():
    orders = get_all_orders()  # Get data from DB
    return jsonify({"status": "success", "data": orders})


@kite_routes.route('/delete-order/<order_id>', methods=['DELETE'])
def delete_order_route(order_id):
    """API endpoint to delete an order by order_id."""
    response = delete_order(order_id)
    return jsonify(response)



@kite_routes.route('/add-positions', methods=['POST'])
def add_position():
    position_data = request.get_json()  # Get JSON data from request
    save_position(position_data)  # Store in DB
    return jsonify({"status": "success", "message": "Order added successfully!"}), 201

@kite_routes.route('/get-positions', methods=['GET'])
def fetch_positions():
    positions = get_all_positions()  # Get data from DB
    
    response = {
        "status": "success",
        "data": {
            "net": positions 
        }
    }
    
    return jsonify(response)



