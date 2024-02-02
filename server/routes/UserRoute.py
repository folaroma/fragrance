from flask import Blueprint
from flask_restful import Api, abort, reqparse, Resource

from app import db
from services import UserService
from models import User

user_api = Api(Blueprint('user_api', __name__))

@user_api.resource('/users/<user_id>')
class User(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('email')
  parser.add_argument('password')
  parser.add_argument('username')

  def get(self, user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return user, 200
    return {'message': 'User not found'}, 404
  
  def post(self):
    payload = User.parser.parse_args()
    if UserService.create_user(payload):
        return {"message": "User created successfully."}, 200
    return {"message": "User failed to be created."}, 404       
  
  def delete(self, user_id):
    if UserService.delete_user_by_id(user_id):
        return {"message": "User deleted successfully."}, 200
    return {"message": "User not found."}, 404
    
  def put(self, user_id):
    payload = User.parser.parse_args()
    if UserService.update_user_by_id(user_id, payload):
        return {"message": "User updated successfully."}, 200
    return {"message": "User not found."}, 404
  
@user_api.resource('/users')
class Users(Resource):
   def get(self):
      users = UserService.get_all_users()
      if users:
         return users, 200
      return {'message': "No users found"}, 404