def validate_register_data(data):
    if not data.get("username") or not data.get("email") or not data.get("password"):
        return "All fields are required."
    if "@" not in data["email"]:
        return "Invalid email."
    return None

def validate_login_data(data):
    if not data.get("email") or not data.get("password"):
        return "Email and password required."
    return None
