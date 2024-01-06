from server.app import db

class Fragrance(db.Model):
  __tablename__ = "fragrance"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(255), nullable=False)
  duration = db.Column(db.Integer, nullable=False)
  notes = db.relationship("note", backref="fragrance")
  brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))

  def __init__(self, name, duration, brand_id):
    self.name = name
    self.duration = duration
    self.brand_id = brand_id