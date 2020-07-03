from application import db
  
class Clothes(db.Model):
    clothes_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    clothes = db.Column(db.String(40), nullable=False)
    
    
    def __repr__(self):
        return str(self.clothes)
