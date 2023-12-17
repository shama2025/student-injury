"""This file will contain functions related to the API"""
import mysql.connector

# Initalizes a connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123",
    database="usersdb",
)

# Cursor to execute queries
cursor = mydb.cursor()

"""This function will search the table and return a true or false if the user exists"""


def confirmLoginCredentials(username, password):
    user = (username, password)
    # Use this video guid for refreence: https://www.youtube.com/watch?v=x7SwgcpACng
    cursor.execute("SELECT username , password FROM usersdb.userinfo")
    result = (
        cursor.fetchall()
    )  # gets all values from select statement and returns a list of tuples
    # Search result for the username and password values
    try:
        result.index(user)
        print("User does exist!")
        return True  # return Yes if the user does exist
    except ValueError:
        print("User does not exist!")
        return False  # return No if the user does not exist
