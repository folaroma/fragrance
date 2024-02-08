from app import db

class FragranceNote():
  fragrance_note = db.Table('fragrance_note',
      db.Column('fragrance_id', db.Integer, db.ForeignKey('fragrance.id')),
      db.Column('note_id', db.Integer, db.ForeignKey('note.id'))
  )