from app import db

class Note(db.Model):
  __tablename__ = "note"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  note = db.Column(db.String(255), nullable=False)
  category = db.Column(db.String(255), nullable=False)
  percentage = db.Column(db.Numeric(5, 2), nullable=False)
  fragrance_id = db.Column(db.Integer, db.ForeignKey('fragrance.id'))

  def __init__(self, note, category, percentage):
    self.name = note
    self.brand = category
    self.duration = percentage
