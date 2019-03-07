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

        # write the new request to the database
        connection = db.get_database_connection()
        #connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute("INSERT INTO requests (id,email,crn) VALUES (?,?,?)",(None,emailAddress,crn))
        print(cursor.lastrowid)
        connection.commit()
        
        print("added")

    return render_template('home.html')

@app.route("/all-requests", methods=["GET"])
def getAllRequests():
    conn = db.get_database_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM requests")

    rows = cur.fetchall()
    print(rows)
    for row in rows:
        print(row)

    #print(results)
    #cursor.close()
    return render_template('home.html')

"""
def query_db(query, args=(), one=False):
    cur = db.get_database_connection().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
"""

if __name__ == '__main__':
    # initialize the database tables right before running
    with app.app_context():
        db.create_database_tables()
    app.teardown_appcontext(db.close_database_connection)
    app.run(debug=True)
