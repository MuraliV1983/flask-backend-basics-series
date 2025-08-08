# Flask Backend Basics Series - MVC Example

A simple Flask web application demonstrating the MVC pattern with:

- Flask Blueprints for modular routing
- SQLAlchemy ORM for database operations
- Jinja2 templates for rendering HTML views
- Automatic database creation if it doesn't exist

_____________________________________________________________________________________________________________________________

## Project Structure

05_mvc/
├── app/
│ ├── init.py # Flask app factory & setup
│ ├── controllers/
│ │ └── user_controller.py # Blueprint for user routes
│ ├── services/
│ │ └── user_service.py # Business logic and DB queries
│ ├── models.py # SQLAlchemy models
│ ├── views/
│ │ └── templates/
│ │ └── users.html # Jinja2 template
│ ├── extensions.py # db init
│ └── config.py # app config (DB URI, etc)
├── app.py # Entry point (runs app)
├── requirements.txt # Python dependencies
└── README.md # This file
_____________________________________________________________________________________________________________________________

## Setup & Run

### 1. Clone the repo or copy project files

### 2. Create and activate a Python virtual environment (optional but recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

Make sure requirements.txt includes:
Flask
SQLAlchemy
Flask-SQLAlchemy
sqlalchemy-utils
PyMySQL (or your DB driver)

4. Configure database connection
Update app/config.py with your MySQL connection string, for example:
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:yourpassword@localhost/yourdatabase"
  Note: Your MySQL user must have permissions to create databases if the app will create DB automatically.

5. Run the app
From the project root folder (05_mvc/), run:
python app.py

You should see:
 * Running on http://127.0.0.1:5000

Open your browser and navigate to:
http://127.0.0.1:5000/users

You should see the users list rendered from users.html
_____________________________________________________________________________________________________________________________
Troubleshooting
  TemplateNotFound:
    Make sure the template_folder path in app/__init__.py matches your actual templates directory location, or use an absolute path.
  Database Access Denied:
    Check your MySQL username, password, and host in the connection string.
  Virtual environment issues:
    Make sure your environment is activated before installing dependencies and running the app.
_____________________________________________________________________________________________________________________________

License
This project is open source and free to use under the MIT License.
_____________________________________________________________________________________________________________________________

🙌🧑‍💻 Author
V Muralidharan
GitHub: https://github.com/MuraliV1983
LinkedIn: https://www.linkedin.com/in/dharanv/
