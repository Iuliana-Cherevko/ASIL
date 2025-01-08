
class User():
    def __init__(self, name, password, email, journal):
        self.name = name
        self.password = password
        self.email = email
        self.journal = journal





# from . import db
# from flask_login import UserMixin
# from sqlalchemy.sql import func


# class Journal(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150), unique=True)
#     password = db.Column(db.String(150))
#     username = db.Column(db.String(150))
#     habit_date = db.Column(db.DateTime(timezone=True), default=func.now())
#     notes = db.relationship('Note')
#     #character, habit
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from os import path
# from flask_login import LoginManager

# db = SQLAlchemy()
# DB_NAME = "database.db"


# def create_app():

#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
#     app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
#     db.init_app(app)

#     from .views import views
#     from .auth import auth



#     app.register_blueprint(views, url_prefix='/')
#     app.register_blueprint(auth, url_prefix='/')




#     from .models import User, Journal

#     with app.app_context():
#         db.create_all()

#     login_manager = LoginManager()
#     login_manager.login_view = 'auth.login'
#     login_manager.init_app(app)

#     @login_manager.user_loader
#     def load_user(id):
#         return User.query.get(int(id))

#     return app


# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')