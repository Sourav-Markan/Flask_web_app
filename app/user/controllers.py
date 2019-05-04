from flask import Blueprint, request, session, jsonify,redirect,render_template,make_response,url_for
from sqlalchemy.exc import IntegrityError
from app import db ,requires_auth
from app.user.models import User
import os

APP_ROOT = os.path.abspath(os.path.dirname(__file__))
mod_user = Blueprint('user', __name__, url_prefix='/user')


############ LOGIN ########################
@mod_user.route('/login', methods=['GET'])
def check_login():
    if 'user_id' in session:
        user = User.query.filter(User.user_id == session['user_id']).first()
        user_Type = user.user_type
        if(user_Type=="admin"):
            return render_template('admin.html')
        return render_template('user.html')

    return redirect(url_for('index'))

@mod_user.route('/login', methods=['POST'])
def login():
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400

    user = User.query.filter(User.email == email).first()
    if user is None or not user.check_password(password):
        return render_template('index.html'), 400

    session['user_id'] = user.user_id
    userType = user.user_type

    if(userType == "admin"):
        return render_template('admin.html')
    return render_template('user.html')


###########USER DETAIL####################

### By this multiple user can access to an webapp at same time
@mod_user.route('/getUserDetail', methods=['GET'])
@requires_auth
def user_detail():
    if 'user_id' in session:
        user_id = session['user_id']
        user_array = []
        user = User.query.filter(User.user_id == user_id).first()
        userType = user.user_type
        if (userType == "admin"):
            render_template('admin.html')

        render_template('user.html')

        data = {"user_id": str(user.user_id), "username": str(user.username), "user_type": str(user.user_type)};
        user_array.append(data)
        return jsonify(success=True,user = user_array)
    return jsonify(success=False), 401




######################LOGOUT################
@mod_user.route('/logout', methods=['GET'])
@requires_auth
def logout():
    session.pop('user_id')
    return redirect(url_for('user.check_login'))


#################CREATE USER################
@mod_user.route('/register', methods=['POST'])
def create_user():
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        last_name = request.form['last_name']
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400

    user_type = "user"

    if '@' not in email:
        return jsonify(success=False, message="Please enter a valid email"), 400

    cast = User.query.all()
    length = 1
    for cas in cast:
        length = length + 1

    user = User(first_name, middle_name, last_name, email, username,user_type, password)
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError as e:
        return jsonify(success=False, message="This email already exists"), 400

    session['user_id'] = str(length)

    return redirect(url_for('user.check_login'))

