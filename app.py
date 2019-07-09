from flask import Flask, flash, redirect, jsonify, render_template, request, session, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmellow import Marshmellow
import os

# Initializing Application
app = Flask(__name__)
items = ['T-Shirt','Pants','Ice Cream']

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

if __name__ == "__main__":
    app.run()
# https://www.youtube.com/watch?v=PTZiDnuC86g
