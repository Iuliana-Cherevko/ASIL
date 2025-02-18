from flask import Blueprint , render_template , request, Flask, redirect, url_for, flash
from datetime import datetime
from . import db
from .models import User 
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

# File contains index and profile

app = Flask(__name__)
views = Blueprint("views", __name__)

users = {
    "Katy Lio": {
        "days_kept_up": 1,
        "creature_name": "Fido",
        "creature_level": 1,
        "checked_in_days": ["November 17, 2024"],
        "current_goal": 30,
        "Fid": "Smoking",
    },
    "Bili Bob": {
        "days_kept_up": 1,
        "creature_name": "Armageddon",
        "creature_level": 2,
        "checked_in_days": ["November 17, 2024"],
        "current_goal": 60,
        "bad_habit_placeholder": "Smoking",
    }
}
@views.route('/index')
def index():
    if request.method == "PUT":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                render_template('profile.html', user = current_user)
                #return redirect(url_for('profile.html', user = current_user))
            
    return render_template("index.html", user = current_user)


#@views.route('/profile', methods = ['GET','POST'])
#@login_required
#def profile():
    # username = "Katy Lio"
    # user_data = users[username] 

    # today = "November 17, 2024"
    # checked_in_today = today in user_data['checked_in_days']

    # return render_template(
    #     "profile.html",
    #     user_logged_in=True,
    #     username_placeholder=username,
    #     days_kept_up_placeholder=user_data['days_kept_up'],
    #     pet_name_placeholder=user_data['creature_name'],
    #     current_goal_placeholder=user_data['current_goal'],
    #     pet_level_placeholder=user_data['creature_level'],
    #     checked_in_days=user_data['checked_in_days'],
    #     checked_in_today=checked_in_today,
    #     bad_habit_placeholder=user_data['bad_habit_placeholder']
    # )
    #return render_template("profile.html")

@views.route('/check-in', methods= ['GET', 'POST'])
def check_in():
    if request.method == 'POST':
        name = current_user
        return render_template('index.html', user_logged_in = True)
        #journal = request.form.get('journal')
        #users[name]['journal'] = journal
        #return render_template("checkin.html")
    return render_template('checkin.html')

@views.route('/about-us')
def about_us():
    return render_template('about-us.html')
    
@views.route('/contact')
def contact():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        job_role = request.form.get('job_role')
        habit = request.form.get('habit')
        goals = request.form.get('goals')

        # Simple validation (ensure fields are not empty)
        if not first_name or not last_name or not email or not habit or not goals:
            flash("All fields are required!", category='error')
        else:
            # Save to database
            new_story = ContactStory(
                first_name=first_name,
                last_name=last_name,
                email=email,
                job_role=job_role,
                habit=habit,
                goals=goals
            )
            db.session.add(new_story)
            db.session.commit()

            flash("Your story has been submitted successfully!", category='success')

    return render_template('contact.html')
@views.route('/concern', methods=['GET', 'POST'])
def concern():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        concern = request.form.get('concern')

        # Simple validation
        if not name or not email or not concern:
            flash("All fields are required!", category='error')
        else:
            new_concern = Concern(name=name, email=email, concern=concern)
            db.session.add(new_concern)
            db.session.commit()
            flash("Your concern has been submitted successfully!", category='success')

    return redirect(url_for('views.contact'))  # Redirect back to contact page after submission

@views.route('/attributions')
def attributions():
    return render_template('attributions.html')

@views.route('/checkin')
def checkin():
    return render_template('checkin.html')# doesnt work rn 

@views.route('/settings', methods = ['GET', 'POST'])
@login_required
def settings():
    # Manage form submission
    return render_template('settings.html',
                           user_logged_in=True,
                           username=current_user.username,
                           email=current_user.email,
                           habit=current_user.habit,
                           goal_duration=current_user.goal,
                           companion_name=current_user.character,
                           companion=current_user.character)
 
@views.route('/companion-hub', methods = ['GET', 'POST'])
@login_required
def companion_hub():
    return render_template('companion-hub.html',
                           user_logged_in=True,
                           username=current_user.username,
                           companion=current_user.character)
