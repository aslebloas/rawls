from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# Show device details
@app.route("/devices/1/")
def show_device():
    return render_template("show_device.html")

@app.route("/user/username/")
def profile():
   return render_template("profile.html")

# Add new device
@app.route("/devices/new/")
def add_device():
    return "Add new Device"

# Edit device
@app.route("/devices/1/edit")
def edit_device():
    return "Edit device"

# Delete device
app.route("/devices/1/delete")
def delete_device():
    return "Delete device"

# Stats
@app.route("/stats/")
def stats():
    return "Stats"

# Login
@app.route("/login/")
def login():
    return "Login"

# Sign up
app.route("/register")
def register():
    return "Register"
