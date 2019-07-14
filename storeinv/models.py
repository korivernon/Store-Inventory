from app import db
from datetime import datetime
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

    # How the information will be displayed
    def __repr__(self):
        return f"Product('{self.name}','{self.image_file}','{self.description}','{self.price}','{self.instock}')"

'''
    def __init__(self, name, image_file, description, price, instock, date_posted):
        self.name = name
        self.description = description
        self.price = price
        if instock == True:
            self.instock == "In Stock"
        else:
            self.instock == "Out of Stock"
        self.image_file = image_file
        self.date_posted = date_posted
'''
