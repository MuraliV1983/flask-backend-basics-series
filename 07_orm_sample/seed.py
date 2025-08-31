from app import app, db, User, Post

def seed_data():
    with app.app_context():
        # Clear existing tables
        db.drop_all()
        db.create_all()

        # Create Users
        user1 = User(user_name="Murali", user_email="Murali@example.com")
        user2 = User(user_name="Bob", user_email="bob@example.com")
        user3 = User(user_name="Charlie", user_email="charlie@example.com")

        db.session.add_all([user1, user2, user3])
        db.session.commit()

        # Create Posts
        post1 = Post(post_title="Murali's Sample Post", post_content="Hello from Murali!", post_user_id=user1.user_id)
        post2 = Post(post_title="Bob's Thoughts", post_content="ORM is cool!", post_user_id=user2.user_id)
        post3 = Post(post_title="Charlie's Diary", post_content="Learning Flask + SQLAlchemy", post_user_id=user3.user_id)
        post4 = Post(post_title="Murali Again!!!!", post_content="Second post from Murali.", post_user_id=user1.user_id)

        db.session.add_all([post1, post2, post3, post4])
        db.session.commit()

        print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
