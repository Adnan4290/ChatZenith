from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
import os
from werkzeug.utils import secure_filename
from random import randint
from flask_socketio import SocketIO

# Create the Flask application instance
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/ChatZenith'
db = SQLAlchemy(app)
socketio = SocketIO(app)
app.config.update(
    MAIL_SERVER='smtp.office365.com',
    MAIL_PORT='587',
    MAIL_USE_SSL=False,
    MAIL_USE_TLS=True,
    MAIL_USERNAME="ChatZenith@outlook.com",
    MAIL_PASSWORD="Chat@Zenith"
)
mail = Mail(app)

def get_username(chatfrom):
    user = Accounts.query.filter_by(id_no=chatfrom).first()
    if user:
        return f"{user.first_name} {user.last_name}"
    return 'Unknown User'

# Register the custom filter using the template_filter decorator
@app.template_filter('get_username')
def get_username_filter(chatfrom):
    return get_username(chatfrom)

class Accounts(db.Model):
    id_no = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(26), nullable=False)

class Chats(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True)
    chatroute = db.Column(db.Integer, nullable=False)
    userid = db.Column(db.Integer, nullable=False)
    chatfrom = db.Column(db.Integer, nullable=False)
    chatTitle = db.Column(db.String(50), nullable=False)
    last_msg = db.Column(db.String(50), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)

class Chatting(db.Model):
    msgid = db.Column(db.Integer, primary_key=True)
    chatroute = db.Column(db.Integer, nullable=False)
    chattingid = db.Column(db.Integer, nullable=False)
    userid = db.Column(db.Integer, nullable=False)
    chatfrom = db.Column(db.Integer, nullable=False)
    chatTitle = db.Column(db.String(50), nullable=False)
    msg = db.Column(db.String(255), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)

@app.route("/", methods=['GET', 'POST'])
def home():
    if 'user_id' in session:
        return redirect("/default")
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        query = Accounts.query.filter(Accounts.email == email, Accounts.password == password).first()
        if query:
            account = Accounts.query.filter_by(email=email).first()
            session['user_id'] = account.id_no
            return redirect("/default")
    return render_template("/login.html")

@app.route("/logout")
def logout():
    session.pop('user_id')
    return redirect("/")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect("/")
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
            session['otp'] = otp
            mail_msg = Message(subject=f"Mail from ChatZenith", sender="ChatZenith@outlook.com",
                               recipients=[session.get('email')],
                               body=f"\nDear {session.get('firstname')} {session.get('lastname')},\nThank you for registering with ChatZenith. To verify your email, please use the following OTP: {otp}\nIf you did not register for ChatZenith, please ignore this email.\nBest regards,\nThe ChatZenith Team")
            mail.send(mail_msg)
            return redirect("/otp")
    return render_template("/register.html")

@app.route("/otp", methods=['GET', 'POST'])
def otp():
    if request.method == 'POST':
        user_entered_otp = request.form.get("otp")
        if user_entered_otp == session.get('otp'):
            newacc = Accounts(email=session.get('email'), first_name=session.get('firstname'),
                              last_name=session.get('lastname'), password=session.get('password'))
            db.session.add(newacc)
            db.session.commit()
            newquery = Accounts.query.filter(Accounts.email == session.get('email'),
                                             Accounts.password == session.get('password')).first()
            if newquery:
                session['user_id'] = newquery.id_no
                session.pop('otp')
                session.pop('email')
                session.pop('firstname')
                session.pop('lastname')
                session.pop('password')
                session.pop('confirmpass')
                return redirect("/default")
    return render_template("/otp_verify.html")

@app.route("/chat/<int:chatroute>/", methods=['GET', 'POST'])
def chat(chatroute):
    if 'user_id' in session:
        session['chatroute'] = chatroute
        if request.method == 'POST':
            message = request.form.get('message')
            chat = Chats.query.filter_by(chatTitle=request.form.get('chatTitle')).first()
            new_message = Chatting(
                chatroute=session.get('chatroute'),
                chattingid=chat.chat_id,
                userid=session.get('user_id'),
                chatfrom=session.get('user_id'),
                chatTitle=request.form.get('chatTitle'),
                msg=message,
                datetime=datetime.now()
            )
            db.session.add(new_message)
            db.session.commit()
            socketio.emit('new_message', {
                'chatroute': session.get('chatroute'),
                'chatTitle': request.form.get('chatTitle'),
                'msg': message,
                'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }, broadcast=True)
            return redirect("/chat/{}".format(session.get('chatroute')))
        else:
            chatting = Chatting.query.filter_by(chatroute=session.get('chatroute')).all()
            titles = Chatting.query.filter_by(chatroute = session.get('chatroute')).all()
            heading = ''
            for title in titles:
                if title.msg and title.userid == session.get('user_id'):
                    heading = title.chatTitle
                    break
                else :
                    continue
            return render_template("chat.html", chats=chatting, title=heading, linkid=session.get('chatroute'),
                                   userid=session.get('user_id'))
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    
@app.route("/new_chat", methods = ['POST'])
def newchat():
    if 'user_id' in session:
        if request.method == 'POST':
            to = request.form.get('search')
            result  = Accounts.query.filter_by(email = to).first()
            return render_template("new_chat.html", result =  result)
        return render_template("new_chat.html", result = None)
    else:
        return redirect("/")

@app.route("/default")
def default():
    if 'user_id' in session:
        chats = Chats.query.filter_by(userid=session.get('user_id')).all()
        usernames = []
        for chat in chats:
            user = Accounts.query.filter_by(id_no=chat.chatfrom).first()
            if user:
                usernames.append(user.first_name + " " + user.last_name)
        return render_template("default_Screen.html", chats=chats, usernames=usernames)
    else:
        return redirect("/")

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
