import re
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User table
class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), nullable=False)
    user_email = db.Column(db.String(120), unique=True, nullable=False)

    # This automatically creates `post.user`
    posts = db.relationship("Post", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.user_name}>"   # fixed attribute

    # Email validation at ORM level
    @validates("user_email")
    def validate_email(self, key, address):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, address):
            raise ValueError(f"Invalid email format: {address}")
        return address
    
# Post table
class Post(db.Model):
    __tablename__ = "posts"

    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(150), nullable=False)
    post_content = db.Column(db.Text, nullable=False)  # capital T for Text

    post_user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    
  
    def __repr__(self):
        return f"<Post {self.post_title}>"   # fixed attribute

