from server.app import db

class Brand(db.Model):
  __tablename__ = "brand"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(255), nullable=False, unique=True)
  fragrance = db.relationship('fragrance', backref='brand')

  def __init__(self, name):
    self.name = name