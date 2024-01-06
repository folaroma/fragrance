from server.app import db
from services import UserService

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    
    def __init__(self, email, password, username):
        self.username = username
        self.email = email
        self.password = UserService.hashed_password(password)