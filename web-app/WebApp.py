from flask import Flask, render_template

import random

app = Flask(__name__)

@app.route("/")
def home():
    data = {"randomNumber": random.random()}
    return render_template("home.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
