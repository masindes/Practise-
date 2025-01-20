from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_serializer import serializer

app = Flask (__name__)
app.config['SQLALCHEMY_DATABESE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICAFTIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class products =