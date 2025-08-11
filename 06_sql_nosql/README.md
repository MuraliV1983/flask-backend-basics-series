# Flask MySQL + MongoDB Example API

A minimal Flask backend demonstrating how to use both MySQL (SQL) and MongoDB (NoSQL) databases in the same app.  
Includes simple REST API endpoints for managing users in both databases.

---
## Folder Structure
my_flask_app/
│
├── app.py                  # Main Flask app (routes + logic)
├── requirements.txt        # Python dependencies list
├── config.py               # Configuration variables (DB credentials, etc.)
│
├── db/                     # Database related scripts or helpers
│   ├── __init__.py        <-- create this file (empty)
│   ├── mysql_connector.py  # MySQL connection helper
│   └── mongo_connector.py  # MongoDB connection helper
│
├── models/                 # (Optional) Data models or ORM files
│   └── user_model.py       # User model if needed
│
├── routes/                 # (Optional) Separate route files for modularity
│   ├── __init__.py        <-- create this file (empty)
│   ├── mysql_routes.py
│   └── nosql_routes.py
│
├── tests/                  # Tests for API endpoints or DB operations
│   └── test_app.py
│
└── README.md               # Project description and instructions


## Features

- Flask API with Blueprints for modular routing
- MySQL integration using `mysql-connector-python`
- MongoDB integration using `pymongo`
- Basic CRUD for user data (GET all users, POST new user)
- Input validation and error handling

---

## Prerequisites

- Python 3.7+
- MySQL server running and accessible
- MongoDB server running and accessible
- `pip` for Python package management

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/flask-mysql-mongo.git
cd flask-mysql-mongo

2. Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
pip install -r requirements.txt

4. Configure database connection in config.py:
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'flaskuser',
    'password': 'server',
    'database': 'flask_auth_db',
    'auth_plugin': 'mysql_native_password'
}

MONGO_URI = 'mongodb://localhost:27017/'

5. Ensure MySQL database and users table exist:
CREATE DATABASE IF NOT EXISTS flask_auth_db;

USE flask_auth_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

6. Run the Flask app:
python app.py

API Endpoints
MySQL Users
GET /mysql/users - Get all users from MySQL

POST /mysql/users - Add a new user to MySQL
Request body JSON:

{
  "name": "Murali",
  "email": "murali@example.com"
}

MongoDB Users
GET /nosql/users - Get all users from MongoDB

POST /nosql/users - Add a new user to MongoDB
Request body JSON:

{
  "name": "MongoUser",
  "email": "mongo@example.com"
}

Testing
Use Postman or curl to test API endpoints. Make sure your Flask app is running.

Example curl to add a MySQL user:
curl -X POST -H "Content-Type: application/json" -d '{"name":"Murali","email":"murali@example.com"}' http://127.0.0.1:5000/mysql/users

License
MIT License

🙌🧑‍💻 Author
V Muralidharan
GitHub: https://github.com/MuraliV1983
LinkedIn: https://www.linkedin.com/in/dharanv/