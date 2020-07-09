from application import db
from application.models import Outfit

db.drop_all()
db.create_all()
