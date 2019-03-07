from flask import Flask, render_template, request

import Database as db

import random

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    data = {"randomNumber": random.random()}
    return render_template("home.html", data=data)

@app.route("/create-request", methods=["POST"])
def createRequest():
    # extract the email address and comma separated list of CRNs from request
    emailAddress = request.form['emailAddress']
    commaSeparatedCRNs = request.form['crns']

    # listOfCRNs is now an array of CRNs, each represented as a string
    listOfCRNs = commaSeparatedCRNs.split(',')

    # for each CRN string, create a new request
    for crnString in listOfCRNs:
        # parse the string CRN to an int
        crn = int(crnString)
        print(emailAddress, crn)
        pass

    return render_template('home.html')

if __name__ == '__main__':
    # initialize the database tables right before running
    with app.app_context():
        db.create_database_tables()
    app.teardown_appcontext(db.close_database_connection)
    app.run(debug=True)
