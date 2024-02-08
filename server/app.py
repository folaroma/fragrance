import os
from os.path import join, dirname
from dotenv import load_dotenv
from logging import StreamHandler
from sys import stdout

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

dotenv_path = join(dirname(__file__), './.env')
load_dotenv()

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
  from routes import brand_api, fragrance_api, note_api, user_api
  from views.index import index_view

  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] =\
            'postgresql+psycopg2://' + os.getenv("DB_PATH")
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  app.register_blueprint(brand_api.blueprint, url_prefix='/api')
  app.register_blueprint(fragrance_api.blueprint, url_prefix='/api')
  app.register_blueprint(note_api.blueprint, url_prefix='/api')
  app.register_blueprint(user_api.blueprint, url_prefix='/api')
  app.register_blueprint(index_view)

  db.init_app(app)
  bcrypt.init_app(app)

  handler = StreamHandler(stdout)
  app.logger.addHandler(handler)
  return app