from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# Show device details
@app.route("/device/")
def show_device():
    return "Show Device details"

@app.route("/user/username/")
def profile():
   return "Profile page"

# Add new device
@app.route("/device/new/")
def add_device():
    return "Add new Device"

# Edit device
@app.route("/edit/1")
def edit_device():
    return "Edit device"

# Delete device
app.route("/device/1/delete")
def delete_device():
    return "Delete device"

# Login
app.route("/login")
def login():
    return "Login"

# Sign up
app.route("/register")
def register():
    return "Register"
