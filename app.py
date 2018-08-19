from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add")
def add_device():
    return "Add a new device"

@app.route("/login")
def login():
    return "login"

@app.route("/user/username/")
def profile():
    return "Profile page"
