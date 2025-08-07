# Flask JWT Authentication API

This is a simple Flask-based backend project implementing **User Registration**, **Login**, and **JWT-based Secure Routes** using **MySQL** as the database.

## 🔧 Tech Stack

- **Backend**: Python (Flask)
- **Database**: MySQL
- **Authentication**: JWT (JSON Web Tokens)
- **Hashing**: bcrypt

---

## 📁 Project Structure

flask-backend-basics-series/04_jwd
│
├── app.py # Main application entry
├── requirements.txt # All required Python packages
├── db_config.py # MySQL DB connection logic
├── README.md # You're here!


---

## 🔐 API Features

- ✅ User Registration (`/register`)
- ✅ User Login (`/login`)
- ✅ JWT Token Generation
- ✅ Secure Route Example (`/protected`)

---

## 📦 Installation

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/flask-backend-basics-series.git
cd flask-backend-basics-series

2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # On Windows

3. Install Required Packages
pip install -r requirements.txt

4. Configure MySQL DB
Create a database named: flask_auth_db
Create a table:
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

5. Update app.py or db_config.py with your DB credentials
python app.py

6. Run the Application
App runs at: http://127.0.0.1:5000

🔄 API Usage (via Postman)
🔹 Register
POST /register
Body (JSON):
{
  "username": "murali",
  "password": "pass123"
}

🔹 Login
POST /login
Body (JSON):
{
  "username": "murali",
  "password": "pass123"
}

Returns:
{
  "token": "your-jwt-token-here"
}

🔹 Secure Route
GET /protected
Header:
Authorization: Bearer <your-jwt-token>

✅ Requirements
Flask
Flask-MySQLdb
PyJWT
bcrypt
(Already in requirements.txt)

📚 Next Steps
Add Role-based Access (Admin/User)
Add Logout & Token Blacklisting
Setup CORS for frontend access
Deploy on AWS EC2


🙌🧑‍💻 Author
V Muralidharan
Learning Flask, MySQL, JWT the right way 🧠💻
GitHub: https://github.com/MuraliV1983
LinkedIn: https://www.linkedin.com/in/dharanv/