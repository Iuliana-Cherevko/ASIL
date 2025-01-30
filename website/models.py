from . import db
from flask_login import UserMixin
from sqlalchemy import func

# File contains database models
#experience doesnt reset just progresses
#add
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    email = db.Column(db.String(150),unique = True)
    goal_duration = db.Column(db.String(150))
    bad_habit = db.Column(db.String(150))
    companion = db.Column(db.String(150))#change to companion
    companion_name = db.Column(db.String(150))
    experience = db.Column(db.String(150))#out of 100 increase experience per level , expeience gain is constant 
    companion_level = db.Column(db.String(150))#companion_level
    goal = db.Column(db.String(150))
    journal = db.relationship('Journal')


class Journal(db.Model):
    id = db.Column(db.String(150),primary_key=True)
    data = db.Column(db.String(300))
    mood = db.Column(db.Integer)
    habit_status = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now)
    user_username = db.Column(db.String(150), db.ForeignKey('user.username'))
