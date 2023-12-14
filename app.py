"""This app.py file will hold the api for the Angular application"""
from flask import Flask
app = Flask(__name__)

"""This route will act as an api endpoint for the login page"""
@app.route("/api/login")
def api_login():
    return ""

"""This route will act as an api endpoint for new account creation"""
@app.route("/api/new/account")
def api_new_account():
    return ""

"""This route will act as an api endpoint for AT email communication"""
@app.route("/api/at/email")
def api_at_email():
    return ""