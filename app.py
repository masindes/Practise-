from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_serializer import serializer

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class product (db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30),nullable = False)
    price = db.Column(db.Integer,nullalble = False)
    category = db.Colunm(db.String(40),nullable = False)

def __repr__(self):
    return f"<product name:{self.name} price:{self.price} category:{self.category}>"

if __name__ == "__main__":
    app.run(debug=True)

