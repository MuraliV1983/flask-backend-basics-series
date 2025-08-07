# 03_crud - Basic User CRUD with Flask + MySQL

This example demonstrates basic **CRUD operations** for a `users` table using **Flask**, **MySQL**, and **bcrypt** for password hashing.

### 🔧 Features

- Create a new user with name, email, and hashed password
- Retrieve all users
- Retrieve a single user by ID
- Update user details (name, email)
- Delete a user
- Passwords are stored securely using `bcrypt`

---

### 📁 Project Structure

03_crud/
│
├── app/
│ ├── init.py # Flask app + Blueprint registration
│ ├── db_connection.py # MySQL connection function
│ ├── routes/
│ │ └── user_routes.py # All user-related endpoints
│ └── models/
│ └── user_model.py # User CRUD logic
│
├── .env # Database credentials (not uploaded to GitHub)
├── app.py # Main entry point
└── requirements.txt # Required Python packages


---

### 🚀 API Endpoints

| Method | Endpoint        | Description            |
|--------|------------------|------------------------|
| GET    | `/users/`        | Get all users          |
| GET    | `/users/<id>`    | Get user by ID         |
| POST   | `/users/`        | Create new user        |
| PUT    | `/users/<id>`    | Update user            |
| DELETE | `/users/<id>`    | Delete user            |

---

### ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/MuraliV1983/flask-backend-basics-series
   cd flask-backend-basics-series/03_crud


2. Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure .env file
Create a .env file in 03_crud/ with your MySQL config:
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=flask_demo

5. Run the Flask app
python app.py

🔐 Password Handling
Passwords are hashed using bcrypt before being stored in the database. Plain-text passwords are never saved.

🧪 Sample cURL Test
curl -X POST http://127.0.0.1:5000/users/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "email": "john@example.com", "password": "secret"}'

📚 Related Topics
Flask Blueprints
MySQL connector for Python
Secure password hashing with bcrypt
RESTful API with Python

🧑‍💻 Author
V Muralidharan
GitHub: https://github.com/MuraliV1983
LinkedIn: https://www.linkedin.com/in/dharanv/