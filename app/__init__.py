from flask import Flask
from app.extensions import db, migrate
from app.models import user, book
from app.routes.books import books_bp
from app.routes.auth import auth_bp
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "super-secret"  # Change in production

    db.init_app(app)
    migrate.init_app(app, db)
    JWTManager(app)

    app.register_blueprint(books_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/api')

    return app
