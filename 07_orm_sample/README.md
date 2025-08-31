# Flask Backend Basics - 07 | ORM Sample

This example shows how to use **SQLAlchemy ORM** with Flask.  
We define `User` and `Post` models, establish relationships, and expose simple REST APIs.  


## 📂 Project Structure
07_orm_sample/
│── app.py # Flask app with API routes
│── models.py # SQLAlchemy ORM models
│── config.py # App configuration (SQLite DB)
│── seed.py # Script to reset + insert test data
│── requirements.txt
└── README.md


🚀 Setup & Run

1. Create Virtual Environment
```bash
git clone <git_url>

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

2. Install Dependencies
pip install -r requirements.txt

3. Seed the Database (optional but recommended)
python seed.py

This will:
•	Drop all tables
•	Recreate them
•	Insert 3 users and 4 posts

You’ll see:
    ✅ Database seeded successfully!

4. Run the App
python app.py

Server runs at → http://127.0.0.1:5000/
📌 API Endpoints
➤ Add a new user

POST /users
{ "name": "Alice", "email": "alice@example.com" }

➤ Get all users

GET /users
Example response (after seeding):

[
  {"id": 1, "name": "Alice", "email": "alice@example.com"},
  {"id": 2, "name": "Bob", "email": "bob@example.com"},
  {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

➤ Add a post

POST /posts

{ "title": "My First Post", "content": "Hello ORM!", "user_id": 1 }

➤ Get all posts with author info

GET /posts
Example response (after seeding):

[
  {"id": 1, "title": "Alice's First Post", "author": "Alice"},
  {"id": 2, "title": "Bob's Thoughts", "author": "Bob"},
  {"id": 3, "title": "Charlie's Diary", "author": "Charlie"},
  {"id": 4, "title": "Alice Again", "author": "Alice"}
]


✅ What You Learned
•	Setting up Flask + SQLAlchemy ORM
•	Defining Models & Relationships
•	Using db.session.add() and db.session.commit()
•	Seeding database with a reset script
•	Querying related data using relationship and foreign key

Happy Learning 🎉
License
MIT License

🙌🧑💻 Author
V Muralidharan
GitHub: https://github.com/MuraliV1983
LinkedIn: https://www.linkedin.com/in/dharanv/