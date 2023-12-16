"""This app.py file will hold the api for the Angular application"""
from flask import Flask, request, Response
from flask_cors import CORS
from backend_util.api_util import confirmLoginCredentials


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
    confirmLogin = confirmLoginCredentials(username, password)
    if not confirmLogin:  # If user doesn't exist
        return Response("No", status=404)  # Returns a user not found
    return Response("Yes", status=200)  # Returns ok when user is found


"""This route will act as an api endpoint for new account creation"""


@app.route("/api/new/account")
def api_new_account():
    return ""


"""This route will act as an api endpoint for AT email communication"""


@app.route("/api/at/email")
def api_at_email():
    return ""
