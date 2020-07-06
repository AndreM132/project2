from application import db
  
class Outfit(db.Model):
    outfit_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String(40), nullable=False)
    clothes = db.Column(db.String(40), nullable=False)
	
