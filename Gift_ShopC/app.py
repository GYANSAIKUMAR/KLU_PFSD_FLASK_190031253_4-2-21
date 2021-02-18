"""from flask import Flask

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return "<h1>Welcome to My Gift Shop World</h1>"

@app.route("/register")
def register():
	return "<h1>Register Now</h1>"

@app.route("/login")
def login():
	return "<h1>Login Now</h1>"""

from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title="My-Home")

@app.route("/register")
def register():
    return render_template('register.html',title="My-Register")

@app.route("/login")
def login():
    return render_template('login.html',title="My-Login")

@app.route("/view")
def view():
    return render_template('view.html',title="My-View")

@app.route("/contactus")
def contactus():
    return render_template('contactUs.html',)

