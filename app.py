from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_migrate import Migrate
from models import *
login_manager = LoginManager()


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)
login_manager.init_app(app)
app.secret_key = "secret_key"


@app.route('/')
def index():
    return render_template('pages/index.html')


# load user function
users = [
    User(id=1, firstname="user1", password="password1"),
    User(id=2, firstname="user2", password="password2"),
]


@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if str(user.id) == str(user_id):
            return user
    return None


# login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        firstname = request.form["firstname"]
        password = request.form["password"]
        user = None
        for u in users:
            if u.firstname == firstname and u.password == password:
                user = u
                break
        if user:
            login_user(user)
            return redirect(url_for("protected"))
        else:
            return "Wrong credentials"
    return render_template("forms/login.html")


# logout page
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@login_required
def protected():
    return f"Welcome {current_user.firstname}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
