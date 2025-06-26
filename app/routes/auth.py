from flask import Blueprint, request, jsonify
<<<<<<< HEAD

auth_bp = Blueprint('auth', __name__, url_prefix='/api')
=======
from app.models.user import User
from app.extensions import db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409

    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

>>>>>>> af767733514901972120d625d3d136c04e03d8a4

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
<<<<<<< HEAD
    username = data.get('username')
    password = data.get('password')

    print("DEBUG: Received data:", data)

    # TEMP: Skip real auth for now
    if username != 'trevour' or password != 'secret123':
        return jsonify({"error": "Invalid username or password"}), 401

    return jsonify({
        "message": "Login successful",
        "username": username
    }), 200
=======
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), 200
>>>>>>> af767733514901972120d625d3d136c04e03d8a4
