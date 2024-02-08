from flask import Blueprint, jsonify
from flask_restful import Api, reqparse, Resource

from services import UserService

user_api = Api(Blueprint('user_api', __name__))

@user_api.resource('/users/<user_id>')
class UserAPI(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('email')
  parser.add_argument('password')
  parser.add_argument('username')

  def get(self, user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        user_data = {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "created": user.created
        }
        return jsonify(user_data), 200
    return {'message': 'User not found'}, 404
  
  def post(self):
    payload = UserAPI.parser.parse_args()
    if UserService.create_user(payload):
        return {"message": "User created successfully."}, 200
    return {"message": "User failed to be created."}, 404       
  
  def delete(self, user_id):
    if UserService.delete_user_by_id(user_id):
        return {"message": "User deleted successfully."}, 200
    return {"message": "User not found."}, 404
    
  def put(self, user_id):
    payload = UserAPI.parser.parse_args()
    success, message = UserService.update_user_by_id(user_id, payload)
    if success:
        return {"message": "User updated successfully."}, 200
    else:
        return {"message": message}, 404
  
@user_api.resource('/users/')
class UsersAPI(Resource):
   def get(self):
    users = UserService.get_all_users()
    return users, 200