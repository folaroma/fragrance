from app import db
from datetime import datetime
from models.FragranceNote import fragrance_note

class Note(db.Model):
  __tablename__ = "note"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  note = db.Column(db.String(255), nullable=False, unique=True)
  category = db.Column(db.String(255), nullable=False)
  percentage = db.Column(db.Numeric(5, 2), nullable=False)
  fragrances = db.relationship("Fragrance", secondary=fragrance_note, back_populates="notes")
  created = db.Column(db.DateTime, default=datetime.utcnow)

  __table_args__ = (
      db.CheckConstraint("category IN ('0', '1', '2')"),
  )

  def __init__(self, note, category, percentage):
    self.note = note
    self.category = category
    self.percentage = percentage

