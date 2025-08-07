from flask import Flask, request, jsonify
from db_connection import init_mysql
import bcrypt
import jwt
from datetime import datetime, timezone, timedelta
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My_Secret_Key'

mysql = init_mysql(app)
# Helper: JWT Token required decorator
def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None

        # check for token in header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # "Bearer <token>"

        if not token:
            return jsonify({'message': "Token is Missing!"}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = data['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({"message":"Token Expired!"}), 401
        except Exception:
            return jsonify({"message":"Token is Invalid"}), 401
        return func(current_user,*args,**kwargs)
    return decorated

# Route Register
@app.route('/register',methods=['POST'])
def register():

    try:
        data = request.json
        username = data['username']
        password = data['password']

        hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username,password) VALUES (%s,%s)",(username,hashed_password))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message":"User Registered Successfully!"}), 201
    except Exception as error:
        return jsonify({"Error":str(error)}), 500

# Route Login
@app.route('/login',methods=['POST'])
def login():

    try:
        data = request.json
        username = data['username']
        password = data['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT id,username,password FROM users WHERE username=%s",(username,))
        user = cur.fetchone()
        cur.close()

        if not user or not bcrypt.checkpw(password.encode('utf-8'),user['password'].encode('utf-8')):
            return jsonify({"message":"Username or Password is not valid"}), 401
        
        token = jwt.encode({
            'user_id':user['id'],
            'exp':datetime.now(timezone.utc) + timedelta(hours=1)

        },app.config['SECRET_KEY'],algorithm='HS256'
        )
        return jsonify({"token": token}), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500
    
# Protected Route
@app.route('/protected', methods=['GET'])
@token_required
def protected_route(current_user):
    try:
        return jsonify({"message":f"Access Granted!. Hello user{current_user}"}), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500


if __name__ == '__main__':
    app.run(debug=True)