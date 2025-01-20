from flask import Flask,jsonify
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
    price = db.Column(db.Integer,nullable = False)
    category = db.Column(db.String(40),nullable = False)

def __repr__(self):
    return f"<product name:{self.name} price:{self.price} category:{self.category}>"

@app.route("/")
def get_products():
    products = product.query.all()
    return jsonify([
        {
            "id" : product.id,
            "name" : product.name,
            "price" : product.price,
            "category" : product.category
        }for product in products
    ])

@app.route("/Home")
def home ():
    return "<h1>Welcome to our page.Stay tuned, sharon will keep you updated</h1>"



if __name__ == "__main__":
    app.run(debug=True)

