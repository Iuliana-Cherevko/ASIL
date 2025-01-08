from flask import Blueprint , request , render_template, redirect, url_for, flash 
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .views import users
auth = Blueprint("auth", __name__)

@auth.route("sign-in", methods=['GET', 'POST'])
def sign_in():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        key = username
        # Look up the user in the dictionary
        if key in users.keys():
            if users[key]['password'] == password:
             # Validate the password
                #check_password_hash(user["password"], password):
                flash("Logged in successfully!", category="success")
                #login_user(username) 
                return render_template(
        "profile.html",
        user_logged_in=True,
        username_placeholder=username,
        days_kept_up_placeholder=users[username]['days_kept_up'],
        pet_name_placeholder=users[username]['creature_name'],
        current_goal_placeholder=users[username]['current_goal'],
        pet_level_placeholder=users[username]['creature_level'],
        checked_in_days=users[username]['checked_in_days'],
        #checked_in_today=checked_in_today,
    )
                #return redirect(url_for("views.profile"))
            else:
                flash('Incorrect password.', category='danger')
        else:
            flash('Username not found.', category='danger')

    return render_template('index.html')

@auth.route("logout")
def logout():
    return "<h1>logout</h1>"

@auth.route('Registration', methods = ['GET', 'POST'])
def registration():
    #data = request.form
    if request.method == 'POST':
        habit = request.form.get("question1")
        name = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        character = request.form.get('character')
        goals = request.form.get("goal-days")

        users[name] = {}
        users[name]['days_kept_up'] = 0
        users[name]['creature_name'] = character
        users[name]['creature_level'] = 0
        users[name]['checked_in_days'] = 0
        users[name]['current_goal'] = goals
        users[name]['email'] = email
        users[name]['password'] = password
        users[name]['habit'] = habit

        print(habit,name,password,email,character) 
        return redirect(url_for('views.index'))
    return render_template("registration.html")