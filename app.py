from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1><br><a href='about'>About!</a>"

@app.route("/about")
def about():
    return "<h1>About Page</h1><br><a href='/home'>Back to Home!</a>"

@app.route("/user/<username>")
def show_user_profile(username):
    return "User %s" % escape(username)

#export FLASK_ENV=development # debug mode
#export FLASK_ENV=production # production mode