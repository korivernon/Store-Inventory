from flask import Flask, flash, redirect, jsonify, render_template, request, session, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import mysql.connector
from datetime import datetime
# from app import db
import os

# Initializing Application
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:R0bin54!@localhost/storeinv?auth_plugin=mysql_native_password'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize Database
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

# Product Class/Model
# Model gives predefined methods
class Product(db.Model):
    # var_name = db.Column((database).TYPE)
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),unique=True, nullable = False)
    image_file = db.Column(db.String(20),unique=True,nullable=False)
    description = db.Column(db.String(200), nullable = False)
    price = db.Column(db.Float, nullable = False )
    instock = db.Column(db.Boolean, nullable = False)
    date_posted = db.Column(db.DateTime,nullable=False, default=datetime.utcnow)

    def __init__(self, name, description, price, instock, image_file, date_posted):
        self.name = name
        self.description = description
        self.price = price
        if instock == True:
            self.instock == "In Stock"
        else:
            self.instock == "Out of Stock"
        self.image_file = image_file
        self.date_posted = date_posted

    # How the information will be displayed
    def __repr__(self):
        return f"Product('{self.name}','{self.image_file}','{self.description}','{self.price}','{self.instock}')"

# Product Schema
# The output to the front end - this is what we want to show.
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description','price', 'instock')

# Init Schema
product_schema = ProductSchema(strict = True)
products_schema = ProductSchema( many = True , strict=True)

# Create a Product
@app.route('/product',methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    instock = request.json['instock']

    new_product = Product(name,description,price,instock)

    # Add to the Databse
    db.session.add(new_product)
    # Commit to the database
    db.session.commit()
    # Return to client
    return product_schema.jsonify(new_product)

@app.route('/product',methods=['GET'])
def get_products():
    # Select all of the products.
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result.data)

@app.route('/product/<id>',methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    result = product_schema.dump(product)
    return jsonify(result.data)

# UPDATE THE PRODUCT
@app.route('/product/<id>',methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    instock = request.json['instock']


    product.name = name
    product.description = description
    product.price = price
    product.instock = instock

    db.session.commit()
    return product_schema.jsonify(product)

@app.route('/product.<id>',methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)

    db.session.commit()
    return product_schema.jsonify(product)

# Run Server
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
