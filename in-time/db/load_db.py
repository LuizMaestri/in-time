from flask_mongoalchemy import MongoAlchemy
from application.flask_config import app

db = MongoAlchemy(app)
Document = db.Document
DocumentField = db.DocumentField
