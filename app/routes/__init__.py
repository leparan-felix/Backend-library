from .auth import auth_bp
from .profile import profile_bp
from .books import books_bp
from .errors import errors_bp

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(profile_bp, url_prefix="/api")
    app.register_blueprint(books_bp, url_prefix="/api")
    app.register_blueprint(errors_bp)
