from ..models.user_model import User
from ..extensions import db

def get_all_users():
    return User.query.all()

def add_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
