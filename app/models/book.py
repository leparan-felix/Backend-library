from app.extensions import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    read = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, nullable=False)  # 🧑 Link to user
