from flask import render_template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test_user:test_123456@localhost/RAWLS'
db = SQLAlchemy(app)

class User(db.Model):
    user_email = db.Column(db.String(50), primary_key = True)
    user_name = db.Column(db.String(50), nullable = False)
    user_password = db.Column(db.String(20))
    device = db.relationship("Devices",
                                backref= db.backref("users", cascade="all, delete-orphan"),
                                lazy='joined')
    def __init__(self, name, email, password=None):
        self.user_name = name
        self.user_email = email
        self.user_password = password

class Devices(db.Model):
    device_SN = db.Column(db.String(50), primary_key = True)
    user_email = db.Column(db.String(50), db.ForeignKey(User.user_email), nullable = False)
    device_brand = db.Column(db.String(50))
    permission = db.relationship("Permissions",
                                    backref=db.backref("devices", cascade="all, delete-orphan"), 
                                    lazy='joined')
    def __init__(self, email, SN, brand=None):
        self.user_email = email
        self.device_SN = SN
        self.device_brand = brand

class Permissions(db.Model):
    permission_id = db.Column(db.Integer, primary_key = True)
    device_SN = db.Column(db.String(50), db.ForeignKey(Devices.device_SN), nullable = False)
    gender = db.Column(db.Boolean)
    age = db.Column(db.Boolean)
    height = db.Column(db.Boolean)
    weight = db.Column(db.Boolean)
    heart_rate = db.Column(db.Boolean)
    sleeping_cycle = db.Column(db.Boolean)
    activity_frequency = db.Column(db.Boolean)

    def __init__(self, SN, **kwargs):
        self.device_SN = SN,
        super(Permissions, self).__init__(**kwargs)


@app.route("/")
def index():
    return render_template('index.html')


# Show device details
@app.route("/devices/<SN>/")
def show_device(SN):
    choose = Devices.query.filter_by(device_SN=SN)
    return render_template("show_device.html")


@app.route("/user/<username>/")
def profile(username):
    profile = User.query.filter_by(user_name=username)
    return render_template("profile.html")

# Add new user
# Make string in format: name-email-password. password part is optional
@app.route("/user/new/<string>")
def add_user(string):
    broken_up = string.split("-")
    if len(broken_up) == 2:
        user = User(broken_up[0], broken_up[1])
    else:
        user = User(broken_up[0], broken_up[1], broken_up[2])
    db.session.add(user)
    return render_template("new_device.html")

# Add new device
@app.route("/devices/new/")
def add_device():
    return render_template("new_device.html")


# Add Amazon Echo
@app.route("/amazon/")
def amazon():
    return render_template("amazon.html")


# Learn about privacy
@app.route("/learn/")
def learn():
    return render_template("learn.html")


# Delete device
@app.route("/devices/<SN>/delete")
def delete_device(SN):
    choose = Devices.query.filter_by(device_SN=SN)
    db.session.delete(choose)
    db.session.commit()
    return "Delete device"


# Login
@app.route("/login/")
def login():
    return "Login"


# Sign up
@app.route("/register")
def register():
    return "Register"

if __name__ == "__main__":
    """
    MAIN Flask App
    """
    db.create_all()
    app.run(host='0.0.0.0', port=5000)