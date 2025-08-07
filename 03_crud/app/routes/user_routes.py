from flask import Flask, jsonify, request, Blueprint
from app.models.user_model import get_all_users, get_user_by_id, create_user


# Create a Blueprint here
user_bp = Blueprint('user_bp',__name__,url_prefix='/users')

# Get all users
@user_bp.route('/', methods=['GET'])
def fetch_all_users():
    users = get_all_users()
    return jsonify(users), 200

# Get a specific user by ID
@user_bp.route('/<int:user_id>', methods=['GET'])
def fetch_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

# Create a new user
@user_bp.route('/', methods=['POST'])
def create_new_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'error': 'Name, Email, and Password are required'}), 400

    try:
        user_id = create_user(name, email, password)
        return jsonify({'message': 'User created successfully', 'user_id': user_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

