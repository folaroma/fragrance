from server.app import db
from models import Fragrance, Note, Brand
from services import FragranceService
from sqlalchemy.exc import IntegrityError

class NoteService():
  @staticmethod
  def create_note(payload):
    note = Note(
      note=payload["note"],
      category=payload["duration"],
      percentage=payload["percentage"],
    )
    if payload["fragrance_ids"]:
       for fragrance_id in payload["fragrance_ids"]:
          fragrance = FragranceService.get_fragrance_by_id(fragrance_id)
          if fragrance:
             note.fragrances.append(fragrance)
    try:
        db.session.add(note)
        db.session.commit()
        return True
    except IntegrityError:
        return False 

  @staticmethod
  def get_note_by_id(note_id):
     note = Note.query.filter_by(id=note_id).first()
     return note
  
  @staticmethod
  def get_note_fragrances(note_id):
     return Fragrance.query.filter_by(note_id).all()
  
  @staticmethod
  def get_note_percentage(fragrance_id):
     fragrance = FragranceService.get_fragrance_by_id(fragrance_id)
     return fragrance.percentage
  