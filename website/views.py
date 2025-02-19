from flask import Blueprint , render_template , request, Flask, redirect, url_for, flash
from datetime import datetime
from . import db
from .models import User 
from .models import Journal
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

@views.route('/questionaire',  methods = ['GET','POST'])
def questionaire():
    if request.method == 'POST':
        current_user.bad_habit = request.form.get('bad_habit')
        current_user.goal_duration = request.form.get('goal_duration')
        current_user.companion_name = request.form.get('companion_name')
        current_user.companion = request.form.get('companion')
        db.session.commit()
        print(current_user.bad_habit, current_user.goal_duration, current_user.companion_name, current_user.companion)
        
        return render_template('index.html')

             

@views.route('/about-us')
def about_us():
    return render_template('about-us.html')
    
@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/attributions')
def attributions():
    return render_template('attributions.html')

@views.route('/checkin', methods = ['GET', 'POST'])#working i think can use more testing
@login_required
def checkin():
    check_in_data = {
    "01/20/2025": {"mood": 3, "habit": False, "journal": "Felt a bit off today. Couldn't focus much, but at least I got some reading done. Hoping tomorrow will be more productive."},
    "01/21/2025": {"mood": 4, "habit": True, "journal": "Had a good day! Got through my coding assignment and even went for a walk in the evening. Feeling accomplished."},
    "01/22/2025": {"mood": 2, "habit": False, "journal": "Struggled with motivation. Kept procrastinating, and now I feel guilty. Need to get back on track tomorrow."},
    "01/23/2025": {"mood": 5, "habit": True, "journal": "Amazing day! Finished all my tasks early, watched a great movie (*Interstellar*, of course), and had a nice dinner with family."},
    "01/26/2025": {"mood": 2, "habit": False, "journal": "Mixed feelings today. Got some work done but didn't feel very engaged. Might just need more sleep."},
    "01/27/2025": {"mood": 4, "habit": True, "journal": "Really tough day. Nothing seemed to go right, and I felt overwhelmed. Hoping for a fresh start tomorrow."},
    "01/28/2025": {"mood": 5, "habit": True, "journal": "Felt productive and energized! Finished my CS assignment early and treated myself to some reading time."}
    }
    if request.method == 'POST':
       #date = datetime.now() dont think its needed
        mood = request.form.get('mood')
        habit_status = request.form.get('habit_status')
        data = request.form.get('journal')
        user_username = current_user.username

        new_journal = Journal(mood=mood, habit_status=habit_status,data=data,user_username=current_user.username)
        print(data, user_username)
        db.session.add(new_journal)
        db.session.commit

        return render_template('companion-hub.html',
                            user_logged_in=True,
                            username=current_user.username,
                            companion=current_user.companion,
                            goal_duration=current_user.goal,
                            check_in_data=check_in_data)

@views.route('/settings', methods = ['GET', 'POST'])
@login_required
def settings():
    print(current_user.companion_name)
    # Manage form submission
    return render_template('settings.html',
                           user_logged_in=True,
                           username=current_user.username,
                           email=current_user.email,
                           habit=current_user.bad_habit,
                           goal_duration=current_user.goal,
                           companion_name=current_user.companion_name,
                           companion=current_user.companion)
    
@views.route('/companion-hub', methods = ['GET', 'POST'])
@login_required
def companion_hub():
    if request.method == 'POST':
        date = request.form.get('date')
        mood = request.form.get('mood')
        habit_status = request.form.get('habit_status')
        data = request.form.get('journal')
        user_username = current_user.username

        new_journal = Journal(date=date, mood=mood, habit_status=habit_status,data=data,user_username=current_user.username)
        print(data, user_username)
        db.session.add(new_journal)
        db.session.commit

        return render_template('companion-hub.html',
                            user_logged_in=True,
                            username=current_user.username,
                            companion=current_user.companion,
                            goal_duration=current_user.goal,
                            check_in_data=check_in_data)

    # sample of check-in data, in a form that will be easy for me to analyse, process in js.
    check_in_data = {
    "01/20/2025": {"mood": 3, "habit": False, "journal": "Felt a bit off today. Couldn't focus much, but at least I got some reading done. Hoping tomorrow will be more productive."},
    "01/21/2025": {"mood": 4, "habit": True, "journal": "Had a good day! Got through my coding assignment and even went for a walk in the evening. Feeling accomplished."},
    "01/22/2025": {"mood": 2, "habit": False, "journal": "Struggled with motivation. Kept procrastinating, and now I feel guilty. Need to get back on track tomorrow."},
    "01/23/2025": {"mood": 5, "habit": True, "journal": "Amazing day! Finished all my tasks early, watched a great movie (*Interstellar*, of course), and had a nice dinner with family."},
    "01/26/2025": {"mood": 2, "habit": False, "journal": "Mixed feelings today. Got some work done but didn't feel very engaged. Might just need more sleep."},
    "02/13/2025": {"mood": 4, "habit": True, "journal": "Really tough day. Nothing seemed to go right, and I felt overwhelmed. Hoping for a fresh start tomorrow."},
    "02/14/2025": {"mood": 5, "habit": True, "journal": "Felt productive and energized! Finished my CS assignment early and treated myself to some reading time."}
    }
    return render_template('companion-hub.html',
                            user_logged_in=True,
                            username=current_user.username,
                            companion=current_user.companion,
                            goal_duration=current_user.goal,
                            check_in_data=check_in_data)
