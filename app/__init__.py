# Import flask and template operators
from flask import *
from flask_sqlalchemy import *
from flask import Flask, render_template
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import *
from functools import wraps

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify(message="Unauthorized", success=False), 401
        return f(*args, **kwargs)
    return decorated

# Import a module / component using its blueprint handler variable (mod_auth)
from app.user.controllers import mod_user
from app.brand.controllers import mod_brands
from app.product.controllers import mod_products

# Register blueprint(s)
app.register_blueprint(mod_user)
app.register_blueprint(mod_brands)
app.register_blueprint(mod_products)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

@app.route('/')
def index():
    return render_template('index.html')
