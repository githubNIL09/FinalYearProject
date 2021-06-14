from flask import Blueprint, render_template, request, session, logging, url_for, redirect, flash
from MODELS import student_users, teacher_user, users,  db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
#import __UserIntegration

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route("/register_student", methods=["POST"])
def register_post_student():
    if request.method == "POST":
        name = request.form.get("form_name")
        dept = request.form.get("form_department")
        email = request.form.get("form_email")
        univroll = request.form.get("form_univ_roll")
        classroll = request.form.get("form_class_roll")
        sem = request.form.get("form_sem")
        mobno = request.form.get("form_mob_no")
        password1 = request.form.get("form_passw")
        password2 = request.form.get("form_conf_passw")

        user = student_users.query.filter_by(Email=email).first()

        if user:
            flash('Email id already exists! Try a new email id','danger')
            return render_template("loginregistrationproject.html")
        if not password1 == password2:
            flash("Password does not match","danger")
            return render_template("loginregistrationproject.html")
        entry = student_users(Name = name, Dept = dept, Email = email, UnivRoll = univroll, ClassRoll = classroll, Semester = sem, Mobile = mobno, Password = generate_password_hash(password1))
        entry1 = users(Email = email, Password = generate_password_hash(password1), Occupation = "STUDENT")
        db.session.add(entry)
        db.session.add(entry1)
        db.session.commit()
        return render_template("registrationsuccess.html")


@auth.route("/register_teacher", methods=["POST"])
def register_post_teacher():
    if request.method == "POST":
        name = request.form.get("teacher_name")
        email = request.form.get("teacher_email")
        dept = request.form.get("teacher_dept")
        passw1 = request.form.get("teacher_passw")
        passw2 = request.form.get("teacher_passw_conf")

        user = teacher_user.query.filter_by(Email=email).first()

        if user:
            flash('Email id already exists! Try a new email id','danger')
            return render_template("loginregistrationproject.html")
        if not passw1 == passw2:
            flash("Password does not match","danger")
            return render_template("loginregistrationproject.html")
        entry = teacher_user(Name = name, Email = email, Dept = dept, Password = generate_password_hash(passw1))
        entry1 = users(Email = email, Password = generate_password_hash(passw1), Occupation = "TEACHER")
        db.session.add(entry)
        db.session.add(entry1)
        db.session.commit()
        return render_template("registrationsuccess.html")

@auth.route("/login", methods=["POST"])
def loginuser():
    if request.method == "POST":
        occupation = request.form.get("form-occupation")
        email = request.form.get("form-username")
        passw = request.form.get("form-password")
        user = users.query.filter_by(Email=email).first()
        if not user:
            flash('Email id does not exist!! Please check your login details and try again.','danger')
            return render_template("loginregistrationproject.html")
        if not check_password_hash(user.Password, passw):
            flash('Incorrect password!! Please check your login details and try again.','danger')
            return render_template("loginregistrationproject.html")
        login_user(user)
        if occupation == "TEACHER":
            return render_template("teacher_dashboard.html")
        elif occupation == "STUDENT":
            return render_template("applicationform(1).html")
        