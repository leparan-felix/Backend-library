from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create shared instances

# NOTE: these will be initialized in create_app()
db = SQLAlchemy()
migrate = Migrate()
