from app import db
from models.Brand import Brand
from sqlalchemy.exc import IntegrityError

class BrandService():
  @staticmethod
  def create_brand(payload):
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
  
  @staticmethod
  def delete_brand_by_id(brand_id):
      brand = Brand.query.get(brand_id)
      if brand:
          db.session.delete(brand)
          db.session.commit()
          return True
      return False
  
  @staticmethod
  def update_brand_by_id(brand_id, payload):
      brand = Brand.query.get(brand_id)
      if brand:
          try:
              for key, value in payload.items():
                  if hasattr(brand, key):
                      setattr(brand, key, value)
              db.session.commit()
              return True
          except Exception as e:
              db.session.rollback()
              return False, str(e)
      else:
          return False
      
  @staticmethod
  def get_all_brands():
      brands_query = Brand.query.all()
      brands_list = []
      for brand in brands_query:
          brands_list.append({
              "id": brand.id,
              "name": brand.name,
              "created": brand.created
          })
      return brands_list