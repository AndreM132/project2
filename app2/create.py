from application import db
from application.models import Brands

db.drop_all()
db.create_all()
