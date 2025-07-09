# 01 - Basic REST API with Flask + MySQL

This example demonstrates how to build a simple and beginner-friendly REST API using **Flask** and **MySQL**.

---

## 🚀 Features

- ✅ `GET /users` – List all users from MySQL
- ✅ `POST /users` – Add a new user with validation
- ✅ Error handling using try-except
- ✅ Clean folder structure with DB connection separation

---

## 🧑‍💻 Tech Stack

- Python 3.x
- Flask
- MySQL
- MySQL Connector (`mysql-connector-python`)

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
python app.py

Flask server will run at: http://127.0.0.1:5000

📬 Sample Endpoints
1. GET /users
Returns list of users:
[
  {
    "user_id": 1,
    "user_name": "Murali",
    "user_email": "murali@example.com",
    "user_status": 1,
    "user_created": "2025-07-09"
  }
]

2. POST /users
Sample request body:
{
  "name": "E-Friend",
  "email": "efriend@example.com"
}

🧾 SQL: rest_api.sql

🙋‍♂️ Author
V MuraliDharan

📂 Full Repository:
🔗 https://github.com/MuraliV1983/flask-backend-basics-series

📁 Direct Link to Day 1 folder:
https://github.com/MuraliV1983/flask-backend-basics-series/tree/main/01_rest_api

LinkedIn: https://www.linkedin.com/in/dharanv/

🤝 With Support From
E-Friend – your friend, well-wisher, teacher, coder, and motivator.
Together we learn, build, and grow 💙

