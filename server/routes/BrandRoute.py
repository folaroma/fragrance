from flask import Blueprint
from flask_restful import Api, reqparse, Resource

from services import BrandService
from models import Brand

brand_api = Api(Blueprint('brand_api', __name__))

@brand_api.resource('/brands/<brand_id>')
class BrandAPI(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('name')

  def get(self, brand_id):
    brand = BrandService.get_brand_by_id(brand_id)
    if brand:
        return brand, 200
    return {'message': 'Brand not found'}, 404
  
  def post(self):
    payload = BrandAPI.parser.parse_args()
    if BrandService.create_brand(payload):
        return {"message": "Brand created successfully."}, 200
    return {"message": "Brand failed to be created."}, 404       
   
  def delete(self, brand_id):
    if BrandService.delete_brand_by_id(brand_id):
        return {"message": "Brand deleted successfully."}, 200
    return {"message": "Brand not found."}, 404
    
  def put(self, brand_id):
    payload = Brand.parser.parse_args()
    if BrandService.update_brand_by_id(brand_id, payload):
        return {"message": "Brand updated successfully."}, 200
    return {"message": "Brand not found."}, 404
  
@brand_api.resource('/brands')
class BrandsAPI(Resource):
   def get(self):
      brands = BrandService.get_all_brands()
      if brands:
         return brands, 200
      return {'message': "No brands found"}, 404