from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from app import db
from app.brand.models import Brand
from app.product.models import Product

import os
APP_ROOT = os.path.abspath(os.path.dirname(__file__))

mod_brands = Blueprint('brands', __name__, url_prefix='/brands')


@mod_brands.route('/addBrand', methods=['POST'])
def new_ent():
    try:
        Brand_type = request.form['Brand_type']
        Brand_name = request.form['Brand_name']
        Year_start = request.form['Year_start']
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400


    brands = Brand.query.all()
    length = 1
    for brand in brands:
        length = length+1

    new_brand = Brand(Brand_name, Brand_type, Year_start)
    db.session.add(new_brand)
    db.session.commit()
    return redirect(url_for('user.check_login'))


@mod_brands.route('/', methods=['GET'])
def getAllBrand():
    products = Product.query.all()
    brands = Brand.query.all()
    Brand_array=[]
    for brand in brands:
        products = Product.query.filter(Product.Brand_id == brand.id)
        products_length = products.count()
        Brand_info = {"Brand_id" :brand.id ,"Brand_name": brand.Brand_name, "Brand_type": brand.Brand_type, "Year_start": brand.Year_start, "no_of_product": products_length}
        Brand_array.append(Brand_info)
    RBrand_array = sorted(Brand_array,key=lambda x:x['Brand_id'],reverse =True)
    return jsonify(brands = Brand_array, RBrands = RBrand_array)

@mod_brands.route('/topbrands', methods=['GET'])
def gettopBrand():
    products = Product.query.all()
    brands = Brand.query.all()
    Brand_array=[]
    for brand in brands:
        products = Product.query.filter(Product.Brand_id == brand.id)
        products_length = products.count()
        Brand_info = {"Brand_id" :brand.id ,"Brand_name": brand.Brand_name, "Brand_type": brand.Brand_type, "Year_start": brand.Year_start, "no_of_product": products_length}
        Brand_array.append(Brand_info)
    sorted_Brand_array = sorted(Brand_array, key=lambda x:x['no_of_product'], reverse = True )
    return jsonify(brands = sorted_Brand_array)
