from flask import Blueprint , request , render_template, redirect, url_for, flash 
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db
from .views import users

auth = Blueprint("auth", __name__)

# Sign In Popup
@auth.route("sign-in", methods=['GET', 'POST'])#is a popup
def sign_in():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        # Look up the user in the dictionary
        # Validate credentials

        if username in users.keys():
            if users[username]['password'] == password:
             # Validate the password
                flash("Logged in successfully!", category="success")

                return render_template(
                    "profile.html",
                    user_logged_in=True,
                    username_placeholder=username,
                    days_kept_up_placeholder=users[username]['days_kept_up'],
                    pet_name_placeholder=users[username]['creature_name'],
                    current_goal_placeholder=users[username]['current_goal'],
                    pet_level_placeholder=users[username]['creature_level'],
                    checked_in_days=users[username]['checked_in_days'],
                    checked_in_today = users[username]['checked_in_today'],
                )
            else:
                flash('Incorrect password.', category='danger')
        else:
            flash('Username not found.', category='danger')

    return render_template('index.html')


# Registration Popup
@auth.route('Registration', methods = ['GET', 'POST'])
def registration():
    #data = request.form
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")
        character = request.form.get('character')
        habit = request.form.get('habit')
        goal = request.form.get("goal-days")

        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match.', category='danger')
            return redirect(url_for('auth.registration'))

        # Check if username already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', category='danger')
            return redirect(url_for('auth.registration'))

        
        # Hash password and create and save new user
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password, email=email,
                       habit=habit,character=character,experience=0,goal=goal)
            
        # Add user to database
        db.session.add(new_user)
        db.session.commit()

        # Log user in
        flash('Account created successfully!', category='success')
        return redirect(url_for('auth.sign_in'))

    return render_template("registration.html")


# Brief Questionaire Popup
@auth.route('questionaire', methods = ['GET', 'POST'])
def questionaire():

    if request.method == 'POST':
       waiver = request.form.get(questionaire='waiver')
       bad_habit = request.form.get(questionaire='bad-habit')
       goal_duration = request.form.get(questionaire='goal-duration')
       companion = request.form.get(questionaire='companion')
       companion_name = request.form.get(questionaire='companion-name')

       # Save the data to the database
       flash('Questionaire submitted successfully!', category='success')
       return redirect(url_for('views.index'))

    return render_template("questionaire.html")

# Logout Popup
@auth.route('logout')
@login_required # Checks if the user is logged in
def logout():
    logout_user()
    flash('Logged out successfully!', category='success')
    return render_template("index.html")


# Contact Popup
@auth.route('contact-us')
def contact_us():
    return render_template("contact.html")

# About Us Popup
@auth.route('about-us')
def about_us():
    return render_template("about.html")