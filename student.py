from flask import Blueprint, render_template, request, session, logging, url_for, redirect, flash, abort
from MODELS import student_users, teacher_user, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user



student = Blueprint('student', __name__, template_folder='templates')

@student.route('/dashboard')
@login_required
def dashboard():
	__CONTEXT__ = {
					'name' : current_user.Name,
					'email' : current_user.Email,
					'dept' : current_user.Dept
				}
	return  render_template('student_dashboard.html', context = __CONTEXT__)