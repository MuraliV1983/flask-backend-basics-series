from flask import Blueprint, request, jsonify
from db.mongo_connector import mongo_users

nosql_bp = Blueprint('nosql_bp', __name__)

@nosql_bp.route('/users', methods=['GET', 'POST'])
def nosql_users():
    if request.method == 'POST':
        data = request.json
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({'error': 'Missing "name" or "email"'}), 400
        mongo_users.insert_one(data)
        return jsonify({'message': 'User added to MongoDB'}), 201

    users = list(mongo_users.find({}, {'_id': 0}))  # hide _id for simplicity
    return jsonify(users)

