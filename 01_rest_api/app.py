from db_connection import get_connection
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/users',methods=['GET'])
def get_users():
    try:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT user_id,user_name,user_email,user_created,user_status FROM users")
        users = cur.fetchall() 
        return jsonify(users)
    except Exception as error:
        return jsonify({"error":str(error)}),500

    finally:
        if cur: cur.close()
        if conn: conn.close()

@app.route('/users',methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")

        if not name or not name.strip():
            return jsonify({"error": "Name is empty or not valid"}),400
        if not email or not email.strip():
            return jsonify({"error": "Email is empty or not valid"}),400
        if "@" not in email or "." not in email:
            return jsonify({"error": "Invalid email format"}),400

        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("INSERT INTO users(user_name,user_email) VALUES (%s,%s)",(name,email,))
        return jsonify({"message":"User Created Successfully"}),201
    except Exception as error:
        return jsonify({"error": str(error)}),500

    finally:
        if conn: conn.close()
        if cur: cur.close()

if __name__ == '__main__':
    app.run(debug=True)