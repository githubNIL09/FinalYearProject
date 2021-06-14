from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from MODELS import db
from MODELS import student_users, teacher_user, users
from auth import auth
from teacher import teacher
from student import student
#from main import main
from flask_login import LoginManager

app = Flask(__name__, static_url_path='/static')
app.register_blueprint(auth)
app.register_blueprint(teacher)
app.register_blueprint(student)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:''@localhost/final year project'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db.init_app(app)

@app.route("/")
def home():
	return render_template("loginregistrationproject.html")
#    return redirect('/ivorybox')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

#@app.errorhandler(404)
#def not_found(e):
#	return render_template('404.html')

@login_manager.user_loader
def load_user(user_id):
    return users.query.get(int(user_id))

if __name__=='__main__':
    app.secret_key="1234_Aditi"
    app.run(debug=True)