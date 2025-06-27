from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
from flask_jwt_extended import JWTManager
from flask_cors import CORS  # ✅ NEW
=======
from flask_migrate import Migrate
>>>>>>> 27185fe8d7113dce8ab0a87497fb0e49a3313165

# Create shared instances

# NOTE: these will be initialized in create_app()
db = SQLAlchemy()
<<<<<<< HEAD
jwt = JWTManager()
cors = CORS()  # ✅ NEW
=======
migrate = Migrate()
>>>>>>> 27185fe8d7113dce8ab0a87497fb0e49a3313165
