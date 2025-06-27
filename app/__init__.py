from flask import Flask
from app.extensions import db, jwt, cors  # ✅ import cors
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)  # ✅ enable CORS

    register_routes(app)

    return app
