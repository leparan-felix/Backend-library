from flask import Flask
<<<<<<< HEAD
from app.extensions import db, jwt, cors  # ✅ import cors
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)  # ✅ enable CORS

    register_routes(app)
=======
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
>>>>>>> 27185fe8d7113dce8ab0a87497fb0e49a3313165

    return app
