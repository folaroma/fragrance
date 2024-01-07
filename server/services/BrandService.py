from server.app import db
from models import Fragrance, Note, Brand
from services import NoteService
from sqlalchemy.exc import IntegrityError

class BrandService():
  @staticmethod
  def create_fragrance(payload):
    brand = Brand(
      name=payload["name"],
    )
    try:
        db.session.add(brand)
        db.session.commit()
        return True
    except IntegrityError:
        return False 

  @staticmethod
  def get_brand_by_id(brand_id):
     brand = Brand.query.filter_by(id=brand_id).first()
     return brand
  
  @staticmethod
  def get_brand_by_name(name):
     return Brand.query.filter_by(name=name).first()