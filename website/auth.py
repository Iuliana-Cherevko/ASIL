from flask import Blueprint , request , render_template, redirect, url_for, flash 
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db
from .views import users
auth = Blueprint("auth", __name__)

@auth.route("sign-in", methods=['GET', 'POST'])#is a popup
def sign_in():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in', category='success')
                login_user(user, remember=True) #will remember user logged in 
                return render_template('profile.html')
            else:
                flash('Incorrect password.', category='error')
                return render_template('index.html')

        else:
            flash('Username not found.', category='error')
            return render_template('index.html')


@auth.route("logout")
@login_required
def logout():
    logout_user()
    return render_template('index.html')

@auth.route('Registration', methods = ['GET', 'POST'])
def registration():
    #data = request.form
    if request.method == 'POST':
        #habit = request.form.get("question1")
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        #character = request.form.get('character')
        #goal = request.form.get("goal-days")
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists', category='error')

        #hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, password=generate_password_hash(password,method='pbkdf2:sha256')
                        , email=email,habit=0,character=0,experience=0,goal=0)
        db.session.add(new_user)
        db.session.commit()
        print(username,password,email) 
        login_user(new_user, remember=True) #will remember user logged in 

        flash('Account successful!', category='success')

        print(username,password,email) 
        return redirect(url_for('views.profile'))
    return render_template("registration.html")