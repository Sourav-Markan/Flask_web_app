from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for,jsonify
from app import db
from app.product.models import Product
from app.brand.models import Brand
from app.user.models import User
from flask import Flask
from flask_mail import Mail
mail = Mail()

mod_products = Blueprint('products', __name__, url_prefix='/products')

import os
APP_ROOT = os.path.abspath(os.path.dirname(__file__))


@mod_products.route('/addProduct', methods=['POST'])
def new_ent():
    try:
        Brand_id = request.form['Brand_id']
        Product_name = request.form['Product_name']
        Product_description = request.form['Product_description']
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400

    products = Product.query.all()
    length = 1
    for product in products:
        length=length+1
    name_image= str(length) + ".jpg"
    APP_ROOT = os.path.abspath(os.path.dirname(__file__))
    os.chdir(os.path.join(APP_ROOT, "../"))
    APP_ROOT = os.getcwd()
    os.chdir(os.path.join(APP_ROOT, "static/images"))
    APP_ROOT = os.getcwd()

    target = os.path.join(APP_ROOT, "ProductImages")

    
    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("Product_Pic"):
        destination = "/".join([target, name_image])
        file.save(destination)
      

    new_product = Product(Product_name,Product_description, Brand_id)
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('user.check_login'))

@mod_products.route('/', methods=['GET'])
def allproducts():
    products = Product.query.all()
    array = []
    for product in products:
        brand = Brand.query.filter(product.Brand_id==Brand.id).first()
        ##Image Link
        Product_link = "/static/images/ProductImages/" + str(product.id) +".jpg"
        Product_info = {"Product_id" :product.id ,"Product_name": product.Product_name,"Product_description": product.Product_description, "Product_Brand": brand.Brand_name, "Product_link" : Product_link}
        array.append(Product_info)
    arr = sorted(array,key=lambda x:x['Product_id'],reverse =True)
    return jsonify(Product = arr)

@mod_products.route('/searchProduct', methods=['POST'])
def searchproducts():
    try:
        Search_Product_name = request.form['Search_Product_name']
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400
    products = Product.query.all()
    array = []
    for product in products:
        brand = Brand.query.filter(product.Brand_id==Brand.id).first()
        ##Image Link
        Product_link = "/static/images/ProductImages/" + str(product.id) +".jpg"
        Product_info = {"Product_id" :product.id ,"Product_name": product.Product_name,"Product_description": product.Product_description, "Product_Brand": brand.Brand_name, "Product_link" : Product_link}
        Pname = product.Product_name.lower()
        Key_words = Pname.split(' ')
        Sname = Search_Product_name.lower()
        Skey_words = Sname.split(' ')
        for word in Skey_words:
            if word in Key_words:
                array.append(Product_info)
    arr = sorted(array,key=lambda x:x['Product_id'],reverse =True)
    render_template('index.html')
    return jsonify(Product = arr)

@mod_products.route('/sendmail', methods=['POST'])
def send_mail():
    try:
        Pro_id = request.form['Product_id']
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400
    Pro_id = 1    
    product = Product.query.filter(Product.id == Pro_id).first()
    Product_info = {"Product_name": product.Product_name,"Product_description": product.Product_description}
    # user_id = session['user_id']
    # user = User.query.filter(User.user_id == user_id)
    # user_email = user.email
    # msg = Message(Product_info,
    #               sender="sourav.markan97@gmail.com",
    #               recipients=[user_email])
    return jsonify(success=True, message="Configure the sender Email for this App for sending email to user"), 200