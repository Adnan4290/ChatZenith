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
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        query = Accounts.query.filter(Accounts.email== email, Accounts.password== password).first()
        if query:
            session['user'] = email
            return redirect("/default")
    return render_template("/login.html")

@app.route("/register")
def register():
    return render_template("/register.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/default")
def default():
    return render_template("default_Screen.html")
@app.route('/new_chat')
def new_chat():
    return render_template("new_chat.html")
@app.route('/verify_otp')
def verify_otp():
    return render_template("otp_verify.html")

app.run(debug= True,host='0.0.0.0',port='80')