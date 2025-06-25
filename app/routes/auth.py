from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json(force=True)
        print("DEBUG: Received data:", data)

        if not data:
            return jsonify({"error": "Missing JSON body"}), 400

        email = data.get("email") or data.get("username")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password required"}), 400

        # For testing purposes only — hardcoded admin
        if email != "admin@example.com" or password != "admin123":
            return jsonify({"error": "Invalid credentials"}), 401

        return jsonify({
            "username": "admin",
            "submitted_email": email,
            "submitted_password": password
        }), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500
