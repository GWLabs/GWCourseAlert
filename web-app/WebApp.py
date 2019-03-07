from flask import Flask, render_template

import Database as db

import random

app = Flask(__name__)

@app.route("/")
def home():
    data = {"randomNumber": random.random()}
    return render_template("home.html", data=data)

if __name__ == '__main__':
    # initialize the database tables right before running
    with app.app_context():
        db.create_database_tables()
    app.teardown_appcontext(db.close_database_connection)
    app.run(debug=True)
