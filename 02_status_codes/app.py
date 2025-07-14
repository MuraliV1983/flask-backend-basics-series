from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in memory data 
users = [
            {"id":1,"name":"Murali"},
            {"id":2,"name":"Dharan"},
            {"id":3,"name":"E-Friend"}
        ]

@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == (user_id)),None)
    if user:
        return jsonify(user),200 # 200 for OK
    else:
        return jsonify({"erro" : "User Not Found"}),404     # 404 , user not found error
    
@app.route('/users',methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error" : "Name is required"}),400  #400, name is required error
    
    new_user = {
        "id": len(users)+1,
        "name": name
    }
    users.append(new_user)
    return jsonify(new_user),201    #201, new user created successfully

if __name__ == '__main__':
    app.run(debug=True)