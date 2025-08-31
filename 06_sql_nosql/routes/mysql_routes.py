from flask import Blueprint, request, jsonify
from db.mysql_connector import get_mysql_connection

mysql_bp = Blueprint('mysql_bp', __name__)

@mysql_bp.route('/users', methods=['GET', 'POST'])
def mysql_users():
    conn = get_mysql_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        data = request.json
        print("Received data:", data)
        # Check if data is valid and has required keys
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        if 'name' not in data or 'email' not in data:
            return jsonify({'error': 'Missing "name" or "email" in request'}), 400
        try:
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s)",
                (data['name'], data['email'])
            )
            conn.commit()
            return jsonify({'message': 'User added to MySQL'}), 201
        except Exception as err:
            print("Error:", err)
            return jsonify({'error': str(err)}), 400

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

