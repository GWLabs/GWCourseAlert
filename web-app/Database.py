import sqlite3
from flask import g as request_data

DATABASE_FILEPATH = "./GWCourseAlert.db"

def get_database_connection():
    # check to see if a database connection has already been put in the request data
    db = getattr(request_data, '__database', None)
    # if no database connection is already in request data, connect
    if db is None:
        # connect to database
        db = sqlite3.connect(DATABASE_FILEPATH)
        # store the connection in the request data
        request_data.__database = db

    return db
