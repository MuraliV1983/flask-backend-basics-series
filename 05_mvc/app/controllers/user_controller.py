from flask import Blueprint, render_template
from ..services.user_service import get_all_users

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users')
def list_users():
    users = get_all_users()
    return render_template('users.html', users=users)
