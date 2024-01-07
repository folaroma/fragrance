from server.app import db
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
  