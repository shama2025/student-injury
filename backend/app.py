"""This app.py file will hold the api for the Angular application"""
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
"""This route will act as an api endpoint for the login page"""


@app.route("/api/login")
def api_login():
    username = request.args.get("username")
    password = request.args.get("password")
    if username == "" or password == "":
        return {"Error": "No username or password entered"}, 404
    return {"Username": username, "Password": password}, 200


"""This route will act as an api endpoint for new account creation"""


@app.route("/api/new/account")
def api_new_account():
    return ""


"""This route will act as an api endpoint for AT email communication"""


@app.route("/api/at/email")
def api_at_email():
    return ""
