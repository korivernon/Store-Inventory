from flask import Flask, flash, redirect, jsonify, render_template, request, session, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models import Product
import mysql.connector

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

#first = Product(name = 'kori', image_file='aPicture', description = 'i am here' , price=100, instock=True)

# To prevent circular imports
from storeinv import routes

'''
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description','price', 'instock')

# Init Schema
product_schema = ProductSchema(strict = True)
products_schema = ProductSchema( many = True , strict=True)
'''
