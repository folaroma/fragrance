from models import User
from server.app import Bcrypt
from server.app import db
from sqlalchemy.exc import IntegrityError

class UserService():
    @staticmethod
    def create_user(payload):
        user = User(
            email=payload["email"],
            password=payload["password"],
            username=payload["username"],
        )
        try:
            db.session.add(user)
            db.session.commit()
            return True
        except IntegrityError:
            return False

    @staticmethod
    def hashed_password(password):
        return Bcrypt.generate_password_hash(password).decode("utf-8")

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.filter_by(id=user_id).first()
        return user

    @staticmethod
    def get_user_with_email_and_password(email, password):
        user = User.query.filter_by(email=email).first()
        if user and Bcrypt.check_password_hash(user.password, password): 
            return user
        else: 
            return None
        
    @staticmethod
    def get_user_with_username_and_password(username, password):
        user = User.query.filter_by(username=username).first()
        if user and Bcrypt.check_password_hash(user.password, password): 
            return user
        else: 
            return None