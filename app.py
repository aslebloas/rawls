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
    devices = db.relationship("Devices",
                                backref= db.backref("users", cascade="all, delete"),
                                lazy='joined')
    def __init__(self, name, email, password=None):
        self.user_name = name
        self.user_email = email
        self.user_password = password

class Devices(db.Model):
    device_SN = db.Column(db.String(50), primary_key = True)
    user_email = db.Column(db.String(50), db.ForeignKey(User.user_email), nullable = False)
    device_brand = db.Column(db.String(50))
    permissions = db.relationship("Permissions",
                                    backref=db.backref("devices", cascade="all, delete"), 
                                    lazy='joined')
    def __init__(self, email, SN, brand=None):
        self.user_email = email
        self.device_SN = SN
        self.device_brand = brand

class Permissions(db.Model):
    permission_id = db.Column(db.Integer, primary_key = True)
    device_SN = db.Column(db.String(50), db.ForeignKey(Devices.device_SN), nullable = False)
    gender = db.Column(db.Boolean, nullable = False)
    age = db.Column(db.Boolean, nullable = False)
    height = db.Column(db.Boolean, nullable = False)
    weight = db.Column(db.Boolean, nullable = False)
    heart_rate = db.Column(db.Boolean, nullable = False)
    sleeping_cycle = db.Column(db.Boolean, nullable = False)
    activity_frequency = db.Column(db.Boolean, nullable = False)

    def __init__(self, SN, **kwargs):
        super(Permissions, self).__init__(**kwargs)
        self.device_SN = SN


@app.route("/")
def index():
    return render_template('index.html')


# Show device details
@app.route("/devices/<SN>/")
def show_device(SN):
    db.session.flush()
    choose = db.session.query(Devices).filter_by(device_SN=SN).first()
    return render_template("show_device.html")


@app.route("/user/<username>/")
def profile(username):
    db.session.flush()
    profile = db.session.query(User).filter_by(user_name=username).first()
    return render_template("profile.html")

# Add new user
# Make string in format: "name-email-password". password part is optional
@app.route("/user/new/<string>")
def add_user(string):
    db.session.flush()
    broken_up = string.split("-")
    if len(broken_up) == 2:
        user = User(broken_up[0], broken_up[1])
    else:
        user = User(broken_up[0], broken_up[1], broken_up[2])
    db.session.add(user)
    db.session.commit()
    return render_template("new_device.html")

# Add new device
# user_string is wanted user's email and name separated by "-"
# device_string is device's owner email and SN separated by "-", can also include brand
@app.route("/devices/<user_string>/<device_string>")
def add_device(user_string, device_string):
    broken_user = user_string.split("-")
    broken_device = device_string.split("-")
    chosen_user=db.session.query(User).filter_by(user_email=broken_user[0], user_name=broken_user[1])
    if len(broken_device) == 2:
        new_device=Devices(broken_device[0], broken_device[1])
    else:
        new_device=Devices(broken_device[0], broken_device[1], broken_device[2])
    chosen_user.devices.append(new_device)
    db.session.add(new_device)
    db.session.commit()
    return render_template("new_device.html")
# device string should be device SN and user_emailseparated by "-"
#permissions is the true or false for the permissions separted by "-", check order below
@app.route("/permissions/<device_string>/<permissions>")
def add_permissions(device_string, permissions):
    db.session.flush()
    broken_device=device_string.split("-")
    broken_permissions = permissions.split("-")
    permissions_key=["gender", "age", "height",  "weight", "heart_rate", "sleeping_cycle", "activity_frequency"]
    permiss_dict = dict(zip(permissions_key, broken_permissions))
    new_permissions = Permissions(broken_device[0], **permiss_dict)
    chosen_device = db.session.query(Devices).filter_by(device_SN=broken_device[0], user_email=broken_device[1])
    chosen_device.permissions.append(new_permissions)
    db.session.add(new_permissions)
    db.session.commit()

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
    choose = Devices.query.filter_by(device_SN=SN).delete()
    db.session.commit()
    db.session.flush()
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