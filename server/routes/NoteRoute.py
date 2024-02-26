from flask import Blueprint
from flask_restful import Api, reqparse, Resource

from services import NoteService
from models.Note import Note

note_api = Api(Blueprint('note_api', __name__))

@note_api.resource('/notes/<note_id>')
class NoteAPI(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('note')
  parser.add_argument('category')
  parser.add_argument('percentage')

  def get(self, note_id):
    note = NoteService.get_note_by_id(note_id)
    if note:
        return note, 200
    return {'message': 'Note not found'}, 404
  
  def post(self):
    payload = Note.parser.parse_args()
    if NoteService.create_note(payload):
        return {"message": "Note created successfully."}, 200
    return {"message": "Note failed to be created."}, 404       
  
  def delete(self, note_id):
    if NoteService.delete_note_by_id(note_id):
        return {"message": "Note deleted successfully."}, 200
    return {"message": "Note not found."}, 404
    
  def put(self, note_id):
    payload = NoteAPI.parser.parse_args()
    if NoteService.update_note_by_id(note_id, payload):
        return {"message": "Note updated successfully."}, 200
    return {"message": "Note not found."}, 404
  
@note_api.resource('/notes')
class NotesAPI(Resource):
   def get(self):
      notes = NoteService.get_all_notes()
      if notes:
         return notes, 200
      return {'message': "No notes found"}, 404