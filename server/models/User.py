from server.app import db
from services import UserService
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False) 
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, email, password, username):
        self.username = username
        self.email = email
        self.password = UserService.hashed_password(password)
        self.created = datetime.utcnow