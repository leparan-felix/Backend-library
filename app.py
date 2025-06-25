from app import create_app
from routes.books import books_bp # type: ignore
from routes.auth import auth_bp  # type: ignore # if using auth

app = create_app()

# ✅ Register blueprints *after* creating app
app.register_blueprint(books_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api')  # if you have this

if __name__ == '__main__':
    app.run(debug=True)
