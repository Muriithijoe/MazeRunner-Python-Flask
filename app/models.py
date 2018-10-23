from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ ='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index=True)
    password_hash = db.Column(db.String())
    points = db.Column(db.Integer)
    badge = db.Column(db.String())
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User{self.username}'

class Question(db.Model):
    __tablename__ = 'questions'

    id=db.Column(db.Integer,primary_key=True)
    question =db.Column(db.String(255),unique=True,index=True)
    choice1 = db.Column(db.String)
    choice2 = db.Column(db.String)
    answer = db.Column(db.String)
    button1 = db.Column(db.String)
    button2 = db.Column(db.String)
    div= db.Column(db.String)


    def save_question(self):
        db.session.add(self)
        db.session.commit()


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    users= db.relationship('User',backref='role',lazy="dynamic")

    def __repr__(self):
        return f'User{self.name}'
