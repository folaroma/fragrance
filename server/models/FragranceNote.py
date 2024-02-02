from app import db

class FragranceNote(db.model):
  fragrance_note = db.Table('fragrance_note',
      db.Column('fragrance_id', db.Integer, db.ForeignKey('fragrance.fragrance_id')),
      db.Column('note_id', db.Integer, db.ForeignKey('note.note_id'))
  )