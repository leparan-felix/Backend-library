# app.py

<<<<<<< HEAD
from flask import Flask
from app.routes.auth import auth_bp

def create_app():
    app = Flask(__name__)

    # Register blueprint with `/api` prefix
    app.register_blueprint(auth_bp, url_prefix='/api')

    return app
=======

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

>>>>>>> af767733514901972120d625d3d136c04e03d8a4
