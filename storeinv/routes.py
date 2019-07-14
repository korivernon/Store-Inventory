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
