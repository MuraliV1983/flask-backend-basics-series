from app import create_app
from app.services.user_service import add_user

app = create_app()

# Seed sample data (only if DB is empty)
with app.app_context():
    from app.models.user_model import User
    if not User.query.first():
        add_user("Murali")
        add_user("John Doe")

if __name__ == '__main__':
    app.run(debug=True)
