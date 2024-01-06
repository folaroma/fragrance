from server.app import db
from models import Fragrance, Note
from sqlalchemy.exc import IntegrityError

class FragranceService():
  @staticmethod
  def create_fragrance(payload):
    fragrance = Fragrance(
      name=payload["name"],
      duration=payload["duration"],
      brand_id=payload["brand_id"]
    )
    try:
        db.session.add(fragrance)
        db.session.commit()
        return True
    except IntegrityError:
        return False 

  @staticmethod
  def get_fragrance_by_id(fragrance_id):
     fragrance = Fragrance.query.filter_by(id=fragrance_id).first()
     return fragrance
  
  @staticmethod
  def get_fragrance_notes(fragrance_id):
     return Note.query.filter_by(fragrance_id).all()
  