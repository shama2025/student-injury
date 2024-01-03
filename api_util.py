"""This file will contain functions related to the API"""
import mysql.connector
import smtplib

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


def confirm_login_credentials(username, password):
    user = (username, password)
    # Use this video guid for refreence: https://www.youtube.com/watch?v=x7SwgcpACng
    cursor.execute("SELECT username , password FROM usersdb.userinfo")
    result = (
        cursor.fetchall()
    )  # gets all values from select statement and returns a list of tuples
    # Search result for the username and password values
    try:
        result.index(user)
        return True  # return Yes if the user does exist
    except ValueError:
        return False  # return No if the user does not exist


"""This function will check if the new user data exists"""


def check_user_exists(new_user_list):
    # Use this video guid for refreence: https://www.youtube.com/watch?v=x7SwgcpACng
    cursor.execute("SELECT username , password, email, name FROM usersdb.userinfo")
    result = (
        cursor.fetchall()
    )  # gets all values from select statement and returns a list of tuples
    # Search result for the username and password values
    try:
        result.index(new_user_list)
        return True  # return Yes if the user does exist
    except ValueError:
        return False  # return No if the user does not exist


"""This function will add the new user to the database"""


def add_new_user(new_user_list):
    if check_user_exists(new_user_list):
        return False
    sqlQuery = (
        "INSERT INTO userinfo (username,password,email,name) VALUES (%s,%s,%s,%s)"
    )
    cursor.execute(sqlQuery, new_user_list)
    mydb.commit()
    if check_user_exists(new_user_list):
        return True
    return False


"""This function will take the users information, obtain the email password and send it to the athletic trainer"""


def send_email(user_email, trainer_email, injury_form):
    return ""
