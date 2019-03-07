from flask import Flask, render_template

import Database as db

import random

app = Flask(__name__)

@app.route("/")
def home():
    data = {"randomNumber": random.random()}
    return render_template("home.html", data=data)

if __name__ == '__main__':
    with app.app_context():
        db.create_database_tables()
    app.run(debug=True)
