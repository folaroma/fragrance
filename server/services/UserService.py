from models import User
from app import db, bcrypt
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
        return bcrypt.generate_password_hash(password).decode("utf-8")

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)
        return user
    
    @staticmethod
    def delete_user_by_id(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def update_user_by_id(user_id, payload):
        user = User.query.get(user_id)
        if user:
            try:
                for key, value in payload.items():
                    if hasattr(user, key):
                        setattr(user, key, value)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                return False, str(e)
        else:
            return False
    
    @staticmethod
    def get_all_users():
        users_query = User.query.all()
        users_list = []
        for user in users_query:
            users_list.append({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "created": user.created
            })
        return users_list