from flask import Flask
from app.routes.user_routes import user_bp

app = Flask(__name__)

# Register your Blueprint here
app.register_blueprint(user_bp)

# Optional: root route for health check
@app.route('/')
def home():
    return 'Flask User API is running!'

if __name__ == '__main__':
    app.run(debug=True)