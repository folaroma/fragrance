from app import db

fragrance_note = db.Table('fragrance_note',
    db.Column('fragrance_id', db.Integer, db.ForeignKey('fragrance.id'), primary_key=True),
    db.Column('note_id', db.Integer, db.ForeignKey('note.id'), primary_key=True)
)