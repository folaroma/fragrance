from app import db
from datetime import datetime

class Brand(db.Model):
  __tablename__ = "brand"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(255), nullable=False, unique=True)
  fragrance = db.relationship('fragrance', backref='brand')
  created = db.Column(db.DateTime, default=datetime.utcnow)

  def __init__(self, name):
    self.name = name