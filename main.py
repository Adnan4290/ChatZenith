from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
import json
import os
from werkzeug.utils import secure_filename


db_url = "mysql://root:@127.0.0.1/ChatZenith"


app = Flask(__name__)


app.secret_key = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)


class Accounts(db.Model):
    index = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(26), nullable=False)







@app.route("/", methods=['GET', 'POST'])
def home():
    if session.get('logged_in')== True:
        return redirect("/default")
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        query = Accounts.query.filter(Accounts.email== email, Accounts.password== password).first()
        if query:
            session['logged_in'] = True
            return redirect("/default")
    return render_template("/login.html")

@app.route("/logout")
def logout():
    session.pop('logged_in')
    return redirect("/")



@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmpass = request.form.get("confirmpass")
        query = Accounts.query.filter(Accounts.email == email).first()
        if password == confirmpass and not query:
            newacc = Accounts(email = email, first_name = firstname, last_name = lastname, password = password)
            db.session.add(newacc)
            db.session.commit()
            newquery = Accounts.query.filter(Accounts.email== email, Accounts.password== password).first()
            if newquery:
                session['logged_in'] = True
                return redirect("/default")
    return render_template("/register.html")

@app.route("/otp")
def otp():
    return render_template("otp_verfy.html")
@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/default")
def default():
    if session.get('logged_in'):
        return render_template("default_Screen.html")
    else:
        return redirect("/")

app.run(debug= True, host="0.0.0.0")