import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

# make a Flask application object called app
app = Flask(__name__)
app.config["DEBUG"] = True

#flash  the secret key to secure sessions
app.config['SECRET_KEY'] = 'your secret key'




# use the app.route() decorator to create a Flask view function called index()
@app.route('/')
def index():
    
    
    return render_template('index.html')

@app.route('/admin/', methods=('GET', 'POST'))
def admin():
    

    return render_template('admin.html')

@app.route('/reservations/', methods=('GET', 'POST'))
def reservations():

    return render_template('reservations.html')


app.run(host="0.0.0.0", port=5001)