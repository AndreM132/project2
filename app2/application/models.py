from application import db
  
class Brands(db.Model):
    brands_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brands = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return str(self.brands)
