from app import db
from models.Note import Note
from services import FragranceService
from sqlalchemy.exc import IntegrityError

class NoteService():
  @staticmethod
  def create_note(payload):
    note = Note(
      note=payload["note"],
      category=payload["category"],
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
  def delete_note_by_id(note_id):
      note = Note.query.get(note_id)
      if note:
          db.session.delete(note)
          db.session.commit()
          return True
      return False
  
  @staticmethod
  def update_note_by_id(note_id, payload):
      note = Note.query.get(note_id)
      if note:
          try:
              for key, value in payload.items():
                  if hasattr(note, key):
                      setattr(note, key, value)
              db.session.commit()
              return True
          except Exception as e:
              db.session.rollback()
              return False, str(e)
      else:
          return False
      
  @staticmethod
  def get_all_notes():
      notes_query = Note.query.all()
      notes_list = []
      for note in notes_query:
          notes_list.append({
              "id": note.id,
              "name": note.name,
              "created": note.created
          })
      return notes_list
  