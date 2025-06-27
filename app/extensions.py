from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS  # ✅ NEW

db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()  # ✅ NEW
