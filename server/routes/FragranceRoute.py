from flask import Blueprint
from flask_restful import Api, reqparse, Resource

from services import FragranceService
from models import Fragrance

fragrance_api = Api(Blueprint('fragrance_api', __name__))

@fragrance_api.resource('/fragrances/<fragrance_id>')
class FragranceAPI(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('name')
  parser.add_argument('duration')
  parser.add_argument('brand_id')

  def get(self, fragrance_id):
    fragrance = FragranceService.get_fragrance_by_id(fragrance_id)
    if fragrance:
        return fragrance, 200
    return {'message': 'Fragrance not found'}, 404
  
  def post(self):
    payload = Fragrance.parser.parse_args()
    if FragranceService.create_fragrance(payload):
        return {"message": "Fragrance created successfully."}, 200
    return {"message": "Fragrance failed to be created."}, 404       
  
  def delete(self, fragrance_id):
    if FragranceService.delete_fragrance_by_id(fragrance_id):
        return {"message": "Fragrance deleted successfully."}, 200
    return {"message": "Fragrance not found."}, 404
    
  def put(self, fragrance_id):
    payload = Fragrance.parser.parse_args()
    if FragranceService.update_fragrance_by_id(fragrance_id, payload):
        return {"message": "Fragrance updated successfully."}, 200
    return {"message": "Fragrance not found."}, 404
  
@fragrance_api.resource('/fragrances')
class FragrancesAPI(Resource):
   def get(self):
      fragrances = FragranceService.get_all_fragrances()
      if fragrances:
         return fragrances, 200
      return {'message': "No fragrances found"}, 404