from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__)
app.secret_key = 'your_secret_key' 

users = {
    "Katy Lio": {
        "days_kept_up": 1,
        "creature_name": "Fido",
        "creature_level": 1,
        "checked_in_days": ["November 17, 2024"],
        "current_goal": 30,
        "bad_habit_placeholder": "Smoking",
    },
    "Bili Bob": {
        "days_kept_up": 1,
        "creature_name": "Armageddon",
        "creature_level": 2,
        "checked_in_days": ["November 17, 2024"],
        "current_goal": 60,
        "bad_habit_placeholder": "drinking",
    }
}

@app.route('/')
def index():
    return render_template('index.html', user_logged_in=True)

@app.route("/profile")
def profile():
    username = "Bili Bob"
    user_data = users[username] 

    today = "November 17, 2024"
    checked_in_today = today in user_data['checked_in_days']

    return render_template(
        "profile.html",
        user_logged_in=True,
        username_placeholder=username,
        days_kept_up_placeholder=user_data['days_kept_up'],
        pet_name_placeholder=user_data['creature_name'],
        current_goal_placeholder=user_data['current_goal'],
        pet_level_placeholder=user_data['creature_level'],
        checked_in_days=user_data['checked_in_days'],
        checked_in_today=checked_in_today,
        bad_habit_placeholder=user_data['bad_habit_placeholder'],
    )

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route('/sign_in', methods=['POST'])
def sign_in():
    username = request.form['username']
    password = request.form['password']
    #return something

@app.route('/checkin')
def checkin():
    return render_template('checkin.html',  user_logged_in=True)

if __name__ == '__main__':
    app.run(debug=True)


