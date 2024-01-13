"""This app.py file will hold the api for the Angular application"""
from flask import Flask, request, Response
from flask_cors import CORS
from api_util import (
    confirm_login_credentials,
    add_new_user,
    check_user_exists,
    send_email,
)


app = Flask(__name__)
CORS(app)
"""This route will act as an api endpoint for the login page"""


@app.route("/api/login")
def api_login():
    username = request.args.get("username")
    password = request.args.get("password")
    if username == "" or password == "":
        return {"Msg": "No username or password entered"}, 404
    confirmLogin = confirm_login_credentials(username, password)
    if not confirmLogin:  # If user doesn't exist
        return {"Msg": "User not Found!"}, 404  # Returns a user not found
    return {"Msg": "User is found!"}, 200
    # Returns ok when user is found


"""This route will act as an api endpoint for new account creation"""


@app.route("/api/new/account")
def api_new_account():
    username = request.args.get("username")
    password = request.args.get("password")
    email = request.args.get("email")
    name = request.args.get("name")

    new_user_list = (username, password, email, name)  # Creates new user list

    if check_user_exists(new_user_list):
        return {"Msg": "User already exists!"}, 404
        # Returns 404 if user already exists
    if add_new_user(new_user_list):
        return {"Msg": "User Created!"}, 200
        # Returns 200 for an ok Response
    return {"Msg": "Error when creating user!"}, 500  # Returns a 500 if an error occurs


"""This route will act as an api endpoint for AT email communication"""


@app.route("/api/at/email", methods=["POST"])
def api_at_email():
    user_email = request.form.get("userEmail")
    trainer_email = request.form.get("trainerEmail")
    # injury_form = request.form.get("injuryForm")
    injury_form = request.files.get("injuryForm")

    if injury_form:
        injury_form.save("uploads/" + injury_form.filename)

    print("Injury form: ", injury_form.headers)

    if user_email == None:
        return {"Msg": "User Email value cannot be read"}, 404
    elif trainer_email == None:
        return {"Msg": "Trainer Email value cannot be read"}, 404
    elif injury_form == None:
        return {"Msg": "Injury Form value cannot be read"}, 404
    response = send_email(user_email, trainer_email, injury_form)
    if response:
        return {"Msg": "Email sent!"}, 200
    return {"Msg": "Error When Sending Email!"}, 500
