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
            print_bus_chart()
            bus_chart = get_bus_chart()
            total_sales = get_sales(get_cost_matrix(), bus_chart)
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('admin.html')


@app.route('/reservations/', methods=('GET', 'POST'))
def reservations():

    return render_template('reservations.html')

def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

def get_bus_chart(data,cost):

    bus = [['O','O','O','O'] for row in range(12)]
    for seat in data:
        row,col = int(seat[1]),int(seat[2])
        bus[row][col] = 'X'

    return bus

def print_bus_chart(bus):
    for row in bus:
        print(row)

    return

def get_sales(cost_matrix, bus):
    sales = 0
    cost = get_cost_matrix()
    
    for row in range(len(bus)):
        for seat in range(len(bus[row])):
            if bus[row][seat] == 'X':
                sales += cost_matrix[row][seat]

    return sales

app.run(host="0.0.0.0", port=5001)