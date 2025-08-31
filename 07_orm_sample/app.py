import re
from flask import Flask, jsonify, request
from models import db, User, Post
from config import Config
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Create tables if not exists
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {"message": "Welcome to Flask ORM Sample!"}

# Add a new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    # Extract fields
    user_name = data.get("user_name")
    user_email = data.get("user_email")

    # Check if required fields are provided
    if not user_name or not user_email:
        return jsonify({"error": "user_name and user_email are required"}), 400

    # Validate email format
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", user_email):
        return jsonify({"error": "Invalid email format"}), 400

    # Check duplicate email
    if User.query.filter_by(user_email=user_email).first():
        return jsonify({"error": "Email already exists"}), 400

    # Create new user
    user = User(user_name=user_name, user_email=user_email)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully", "user_id": user.user_id}), 201

# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([
        {"id": u.user_id, "name": u.user_name, "email": u.user_email}
        for u in users
    ])

# Add a post
@app.route("/posts", methods=["POST"])
def add_post():
    data = request.get_json()
    try:
        post = Post(
            post_title=data["post_title"],
            post_content=data["post_content"],
            post_user_id=data["post_user_id"]
        )
        db.session.add(post)
        db.session.commit()
        return {"message": f"Post '{post.post_title}' added successfully!"}, 201
    except IntegrityError:
        db.session.rollback()
        return {"error": "Invalid user_id or duplicate entry"}, 400

# Get posts with user info
@app.route("/posts", methods=["GET"])
def get_posts():
    posts = Post.query.all()
    return jsonify([
        {
            "id": p.post_id,
            "title": p.post_title,
            "content": p.post_content,
            "author": p.user.user_name
        }
        for p in posts
    ])

if __name__ == "__main__":
    app.run(debug=True)
