from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import glob
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#secret key
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3' #user. is the table
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))

    def __init__(self, name, email):
        self.name=name
        self.email=email

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        #the session last as long as defined in timedelta parameter
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"]= found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash(f"Succesfully Logged In {user}")
        return redirect(url_for("user", usr=user))
    else:  
        if "user" in session:
            flash("Already Logged In")
            return redirect(url_for("user")) 

        return render_template("login.html")

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"{user} sei un coglione sloggato", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None

    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by().first()
            found_user.email = email
            db.session.commit()
            flash("Email Saved")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)
    else:
        flash("Non sei loggato brutto coglione")
        return redirect(url_for("login.html"))

if __name__ == "__main__":
    db.create_all() #create database if doesnt exist
    app.run(host='127.0.0.1', port=8080, debug=True)