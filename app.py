"""This app.py file will hold the api for the Angular application"""
from flask import Flask, request, Response
from flask_cors import CORS
from backend_util.api_util import (
    confirm_login_credentials,
    add_new_user,
    check_user_exists,
)


app = Flask(__name__)
CORS(app)
"""This route will act as an api endpoint for the login page"""


@app.route("/api/login")
def api_login():
    username = request.args.get("username")
    password = request.args.get("password")
    if username == "" or password == "":
        return Response(
            "No username or password entered", content_type="text/plain", status=404
        )
    confirmLogin = confirm_login_credentials(username, password)
    if not confirmLogin:  # If user doesn't exist
        return Response(
            "User not Found!", status=404, content_type="text/plain"
        )  # Returns a user not found
    return Response(
        "User is found!", status=200, content_type="text/plain"
    )  # Returns ok when user is found


"""This route will act as an api endpoint for new account creation"""


@app.route("/api/new/account")
def api_new_account():
    username = request.args.get("username")
    password = request.args.get("password")
    email = request.args.get("email")
    name = request.args.get("name")

    new_user_list = (username, password, email, name) #Creates new user list

    if check_user_exists(new_user_list):
        return Response("User already exists!", status=404, content_type="text/plain") #Returns 404 if user already exists
    if add_new_user(new_user_list):
        return Response("User Created!", status=200, content_type="text/plain") #Returns 200 for an ok Response
    return Response("Error when creating user!", status=500, content_type="text/plain") #Returns a 500 if an error occurs


"""This route will act as an api endpoint for AT email communication"""


@app.route("/api/at/email")
def api_at_email():
    return ""
