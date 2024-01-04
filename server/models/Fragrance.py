from app import db

from sqlalchemy.exc import IntegrityError

class Fragrance(db.Model):
  __tablename__ = "fragrance"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(255), nullable=False)
  brand = db.Column(db.String(255), nullable=False)
  duration = db.Column(db.Integer, nullable=False)
  notes = db.relationship("note", backref="fragrance")

  def __init__(self, name, brand, duration):
    self.name = name
    self.brand = brand
    self.duration = duration


  @staticmethod
  def create_fragrance(payload):
    fragrance = Fragrance(
      name=payload["name"],
      brand=payload["brand"],
      duration=payload["duration"],
    )
    try:
        db.session.add(fragrance)
        db.session.commit()
        return True
    except IntegrityError:
        return False
