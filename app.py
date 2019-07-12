from flask import Flask, flash, redirect, jsonify, render_template, request, session, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from app import db
import os

# Initializing Application
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

#items = ['T-Shirt','Pants','Ice Cream']

# Product Class/Model
# Model gives predefined methods
class Product(db.Model):
    # var_name = db.Column((database).TYPE)
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    inStock = db.Column(db.Boolean)

    def __init__(self, name, description, price, inStock):
        self.name = name
        self.description = description
        self.price = price
        if inStock == True:
            self.inStock == "In Stock"
        else:
            self.inStock == "Out of Stock"

# Product Schema
# The output to the front end - this is what we want to show.
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description','price', 'inStock')

# Init Schema
product_schema = ProductSchema(strict = True)
products_schema = ProductSchema( many = True , string=True)

# Create a Product
@app.route('/product',methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    inStock = request.json['inStock']

    new_product = Product(name,description,price,inStock)

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
@app.route('/product/<id>',method=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    inStock = request.json['inStock']


    product.name = name
    product.description = description
    product.price = price
    product.inStock = inStock

    db.session.commit()
    return product_schema.jsonify(product

@app.route('/product.<id>',method=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)

    db.session.commit()
    return product_schema.jsonify(product)

'''
@app.route("/catalog/")
def catalog():
    # This displays the items by setting the items equal to their respective parts.
    # We want to get the price of the items.
    # We want to get the status of the items.
    # We want to display these items in conjunction with one another.
    return render_template(
    'catalog.html',
    items=items)

@app.route("/item/<user>/")
def item(user):
    return render_template(
    'output.html',item_num=user, clothing_article = items[int(user)-1])
'''
# Run Server
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
