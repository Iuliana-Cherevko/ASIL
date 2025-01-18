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
            if user.password == password:
                flash('Logged in', category='success')
                return render_template('profile.html')
    #             return redirect(url_for("views.profile"))
    #         else:
    #             flash('Incorrect password.', category='danger')
    #     else:
    #         flash('Username not found.', category='danger')

        return render_template('index.html')

@auth.route("logout")
def logout():
    return "<h1>logout</h1>"

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

        new_user = User(username=username, password=password, email=email,
                        habit=0,character=0,experience=0,goal=0)
        #db.session.commit(new_user)
        #db.session.commit()


        # users[name] = {}
        # users[name]['days_kept_up'] = 0
        # users[name]['creature_name'] = character
        # users[name]['creature_level'] = 0
        # users[name]['checked_in_days'] = 0
        # users[name]['current_goal'] = goals
        # users[name]['email'] = email
        # users[name]['password'] = password
        # users[name]['habit'] = habit

        print(username,password,email) 
        return redirect(url_for('views.index'))
    return render_template("registration.html")