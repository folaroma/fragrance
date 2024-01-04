import os
from dotenv import load_dotenv

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
DB_PATH = os.getenv("DB_PATH")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'postgresql://' + DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)