# routes.py
from flask import Blueprint, jsonify, request

bp = Blueprint('main', __name__)

# Example 1: A simple GET route
@bp.route('/')
def home():
    return jsonify(message='Hello from Blueprint!')

# Example 2: A GET route to fetch all items
@bp.route('/items', methods=['GET'])
def get_items():
    items = ["item1", "item2", "item3"]
    return jsonify(items)

# Example 3: A POST route to add a new item
@bp.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    new_item = data.get('name')
    return jsonify({"message": f"Item {new_item} added!"}), 201

# Example 4: A PUT route to update an existing item
@bp.route('/items/<string:item_name>', methods=['PUT'])
def update_item(item_name):
    data = request.get_json()
    new_name = data.get('name')
    return jsonify({"message": f"Item {item_name} updated to {new_name}!"})

# Example 5: A DELETE route to delete an item
@bp.route('/items/<string:item_name>', methods=['DELETE'])
def delete_item(item_name):
    return jsonify({"message": f"Item {item_name} deleted!"})
