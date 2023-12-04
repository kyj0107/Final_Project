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
    
    
    return "<h1>Index Page</h1>"

@app.route('/admin/', methods=('GET', 'POST'))
def admin():
    

    return "<h1>Admin Stuff</h1>"

@app.route('/reservations/', methods=('GET', 'POST'))
def reservations():

    return "<h1>Reservations Stuff</h1>"


app.run(host="0.0.0.0", port=5001)