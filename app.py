import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

# make a Flask application object called app
app = Flask(__name__)
app.config["DEBUG"] = True

#flash  the secret key to secure sessions
app.config['SECRET_KEY'] = 'your secret key'

def check_login(username, password):
    with open('passcodes.txt', 'r') as file:
        for line in file:
            user, pwd = line.strip().split(', ')
            if user == username and pwd == password:
                return True
    return False


# use the app.route() decorator to create a Flask view function called index()
@app.route('/')
def index():
    
    
    return render_template('index.html')


@app.route('/admin/', methods=('GET', 'POST'))
def admin():
    alert_message = None
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if check_login(username, password):
            flash('Login successful!', 'success')
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('admin.html')


@app.route('/reservations/', methods=('GET', 'POST'))
def reservations():

    return render_template('reservations.html')


app.run(host="0.0.0.0", port=5001)