from flask_sqlalchemy import SQLAlchemy
from app import db


class Brand(db.Model):
    __tablename__ = 'Brand'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Brand_name = db.Column(db.String(20), nullable=False)
    Year_start = db.Column(db.String(20), nullable=False)
    Brand_type = db.Column(db.String(20), nullable=False) 

    def __init__(self, Brand_name, Brand_type, Year_start):
        self.Brand_name = Brand_name
        self.Brand_type = Brand_type
        self.Year_start = Year_start

    def __repr__(self):
        return "Brand { type: %r, name: %r, year: %r}" % (self.Brand_type, self.Brand_name, self.Year_start)


