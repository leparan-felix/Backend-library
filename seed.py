from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.book import Book

app = create_app()

with app.app_context():
    print("📦 Dropping all tables...")
    db.drop_all()

    print("🛠️ Creating tables...")
    db.create_all()

    print("👤 Seeding test user...")
    user = User(username="testuser")
    user.set_password("testpass")
    db.session.add(user)
    db.session.commit()  # Commit first to get user.id

    print("📚 Seeding test book...")
    book = Book(
        title="Rich Dad Poor Dad",
        author="Robert Kiyosaki",
        description="A personal finance classic.",
        read=True,
        user_id=user.id
    )

    db.session.add(book)
    db.session.commit()

    print("✅ Done seeding!")
