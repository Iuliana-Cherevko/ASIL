from flask import Blueprint , request , render_template, redirect, url_for, flash 
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db
from .views import users
auth = Blueprint("auth", __name__)

# Authentication file contains login and registration

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
                return render_template('index.html')
            else:
                flash('Incorrect password.', category='error')
                return render_template('index.html')

        else:
            flash('Username not found.', category='error')
            return render_template('index.html')


# Endpoint:
@auth.route("logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return render_template('index.html') 

@auth.route('registration', methods = ['GET', 'POST'])
def registration():
    #data = request.form
    if request.method == 'POST':
        #habit = request.form.get("question1")
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        #character = request.form.get('character')
        #goal = request.form.get("goal-days")

        ### Checks if username already exists

        user = User.query.filter_by(username=username).first()
        email_check = User.query.filter_by(email=email).first()

        if user and password:
            username_taken, email_taken = True, True
            print("username and email taken")
            return render_template('index.html')

        elif user:
            username_taken = True
            flash('Username already exists', category='error')
            print('username taken')
            return render_template('index.html')
        
        elif email_check:
            email_taken = True
            print("email taken") # for debugging
            flash('Email already exists', category='error')
            return render_template('index.html')

        #hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=generate_password_hash(password,method='pbkdf2:sha256')
                            , email=email,bad_habit=0,companion=0,experience=0,goal=0)
        db.session.add(new_user)
        db.session.commit()
        print(username,password,email) 
        login_user(new_user, remember=True) #will remember user logged in 

        flash('Account successful!', category='success')

        print(username,password,email) 
        return render_template ('index.html')
    return render_template("index.html")