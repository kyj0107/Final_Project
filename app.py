import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)
app.config["DEBUG"] = True

app.config['SECRET_KEY'] = 'your secret key'

def generate_ticket(first_name):

    bus_name = "INFOTC4320"
    code = ""
    count = 0

    if len(first_name) < len(bus_name):
        for letter in range(len(first_name)):
            code += first_name[letter] + bus_name[letter]
            count += 1
        code += bus_name[count:]
    elif len(first_name) == len(bus_name):
        for letter in range(len(first_name)):
            code += first_name[letter] + bus_name[letter]
    else:
        for letter in range(len(bus_name)):
            code += first_name[letter] + bus_name[letter]
            count += 1
        code += first_name[count:]
    return code

def save_reservation(first_name, seat_row, seat_column, ticket_number):
    file = open("reservations.txt", "a")
    file.write("{}, {}, {}, {}\n".format(first_name, seat_row, seat_column, ticket_number))
    file.close()

# @app.route('/')
# def index():
    
    
#     return "<h1>Index Page</h1>"

# @app.route('/admin/', methods=('GET', 'POST'))
# def admin():
    

#     return "<h1>Admin Stuff</h1>"

# @app.route('/reservations/', methods=('GET', 'POST'))
# def reservations():

#     return "<h1>Reservations Stuff</h1>"


# app.run(host="0.0.0.0", port=5001)

def main():

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    seat_row = int(input("Enter a seat row: "))
    seat_column = int(input("Enter a seat column: "))

    ticket_number = generate_ticket(first_name)
    save_reservation(first_name, seat_row, seat_column, ticket_number)
    print("Congratulations, {}! Row: {}, Seat: {} has been reserved for you. Enjoy your trip!".format(first_name, seat_row, seat_column))
    print("Your e-ticket number is: {}".format(ticket_number))

main()