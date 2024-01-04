import os
from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

load_dotenv()
DB_PATH = os.getenv("DB_PATH")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'postgresql://' + DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)