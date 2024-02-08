from app import db
from models import Fragrance, Note, Brand
from services import NoteService
from sqlalchemy.exc import IntegrityError

class FragranceService():
   @staticmethod
   def create_fragrance(payload):
      fragrance = Fragrance(
         name=payload["name"],
         duration=payload["duration"],
         brand_id=payload["brand_id"]
      )
      if payload["note_ids"]:
         for note_id in payload["note_ids"]:
            note = NoteService.get_note_by_id(note_id)
            if note:
               fragrance.notes.append(note)
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

   @staticmethod
   def get_fragrance_brand(fragrance_id):
      fragrance = FragranceService.get_fragrance_by_id(fragrance_id)
      return Brand.query.filter_by(fragrance.brand_id).first()

   @staticmethod
   def delete_fragrance_by_id(fragrance_id):
         fragrance = Fragrance.query.get(fragrance_id)
         if fragrance:
            db.session.delete(fragrance)
            db.session.commit()
            return True
         return False

   @staticmethod
   def update_fragrance_by_id(fragrance_id, payload):
         fragrance = Fragrance.query.get(fragrance_id)
         if fragrance:
            try:
               for key, value in payload.items():
                     if hasattr(fragrance, key):
                        setattr(fragrance, key, value)
               db.session.commit()
               return True
            except Exception as e:
               db.session.rollback()
               return False, str(e)
         else:
            return False
         
   @staticmethod
   def get_all_fragrances():
         fragrance_query = Fragrance.query.all()
         fragrances_list = []
         for fragrance in fragrance_query:
            fragrances_list.append({
               "id": fragrance.id,
               "name": fragrance.name,
               "duration": fragrance.duration,
               "brand": fragrance.brand_id,
               "created": fragrance.created
            })
         return fragrances_list
