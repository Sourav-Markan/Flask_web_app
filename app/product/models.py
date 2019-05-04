from flask_sqlalchemy import SQLAlchemy
from app import db

class Product(db.Model):
	__tablename__ = 'Product'
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	Brand_id = db.Column(db.String(20), nullable=False)
	Product_name = db.Column(db.String(20), nullable=False)
	Product_description = db.Column(db.String(250), nullable=False)

	def __init__(self, Product_name, Product_description, Brand_id):
		self.Product_name = Product_name
		self.Product_description = Product_description
		self.Brand_id = Brand_id

	def __repr__(self):
		return "Product { Brand_id: %r, Product_name: %r, Product_description: %r}" % (self.Brand_id, self.Product_name, self.Product_description)
