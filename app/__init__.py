from flask import Flask
from app.config import Config
from app.extensions import db, jwt, migrate
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    register_routes(app)
    return app
