from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class student_users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80))
    Dept = db.Column(db.String(80))
    Email = db.Column(db.String(50))
    UnivRoll = db.Column(db.String(15))
    ClassRoll = db.Column(db.String(15))
    Semester = db.Column(db.String(15))
    Mobile = db.Column(db.String(15))
    Password = db.Column(db.String(300))


class teacher_user(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(80))
	Email = db.Column(db.String(50))
	Dept = db.Column(db.String(80))
	Password = db.Column(db.String(300))


class users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String(50))
    Password = db.Column(db.String(300))
    Occupation = db.Column(db.String(15))
