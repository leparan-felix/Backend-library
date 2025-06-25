from flask import Flask
from .extensions import db, jwt, migrate
from .models import book, user  # 👈 Make sure all models are imported

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
    app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change in production

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)  # ✅ Migrate setup

    return app
