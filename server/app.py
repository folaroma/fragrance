import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'postgresql://' + os.getenv("DB_PATH")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)