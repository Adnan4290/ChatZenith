from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
import json
import os
from werkzeug.utils import secure_filename
from random import randint

db_url = "mysql://root:@127.0.0.1/ChatZenith"


app = Flask(__name__)


app.secret_key = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)
app.config.update(
    MAIL_SERVER='smtp.office365.com',
    MAIL_PORT='587',
    MAIL_USE_SSL=False,
    MAIL_USE_TLS=True,
    MAIL_USERNAME="ChatZenith@outlook.com",
    MAIL_PASSWORD="Chat@Zenith"
)
mail = Mail(app)

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
        session['firstname'] = request.form.get("firstname")
        session['lastname'] = request.form.get("lastname")
        session['email'] = request.form.get("email")
        session['password'] = request.form.get("password")
        session['confirmpass'] = request.form.get("confirmpass")
        query = Accounts.query.filter(Accounts.email == session.get('email')).first()
        if session.get('password') == session.get('confirmpass') and not query:
            otp = ""
            for i in range(6):
                i = str(randint(0, 9))
                otp += i
                continue
            session['otp'] = otp
            mail_msg = Message(subject=f"Mail from ChatZenith", sender="ChatZenith@outlook.com", recipients=[session.get('email')], body=f"\n\nName:\t{session.get('firstname')} {session.get('lastname')}\n\nEmail:\t{session.get('email')}\n\nMessage:\tPlease verify your email with the otp {otp}")
            mail.send(mail_msg)
            return redirect("/otp")
            
    return render_template("/register.html")

@app.route("/otp", methods = ['GET', 'POST'])
def otp():
    if request.method == 'POST':
        user_entered_otp = request.form.get("otp")
        if user_entered_otp == session.get('otp'):
            newacc = Accounts(email = session.get('email'), first_name = session.get('firstname'), last_name = session.get('lastname'), password = session.get('password'))
            db.session.add(newacc)
            db.session.commit()
            newquery = Accounts.query.filter(Accounts.email== session.get('email'), Accounts.password== session.get('password')).first()
            if newquery:
                session['logged_in'] = True
                session.pop('otp')
                session.pop('email')
                session.pop('firstname')
                session.pop('lastname')
                session.pop('password')
                session.pop('confirmpass')
                return redirect("/default")
    return render_template("/otp_verify.html")

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