from app.extensions import db

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    read = db.Column(db.Boolean, default=False)

    # Foreign key to link book to a user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Book {self.title} by {self.author}>'

