# app.py

from flask import Flask
from app.routes.auth import auth_bp

def create_app():
    app = Flask(__name__)

    # Register blueprint with `/api` prefix
    app.register_blueprint(auth_bp, url_prefix='/api')

    return app
