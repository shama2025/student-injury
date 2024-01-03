"""This file will contain functions related to the API"""
import mysql.connector
import smtplib
import getpass

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
    HOST = "smtp-mail.outlook.com"
    PORT = 587
    # users_password = get_users_password(user_email)
    # if users_password == False:
    #     return False
    EMAIL = "studentInjuryTest@outlook.com"
    PASSWORD = "ASDFGHJKL;z123"

    MESSAGE = f"""Subject: Patient Outcome Reported Meaasure
        Hi, 

        I finished my injury form! What days can we meet to discuss it?
        
        {injury_form}
    """
    try:
        smtp = smtplib.SMTP(HOST, PORT)

        staus_code, response = smtp.ehlo()
        print(f"Echoing the server:  {staus_code} {response}")

        staus_code, response = smtp.starttls()
        print(f"Starting tls connection:  {staus_code} {response}")

        staus_code, response = smtp.login(
            EMAIL, PASSWORD
        )  # This will need to be the users password
        print(f"Logging in: {staus_code} {response}")

        smtp.sendmail(EMAIL, trainer_email, MESSAGE)
        print("Email sent Succesfully!")
        return True
    except:
        print("Error!")
        return False


"""This function will get the users email password from the Database"""


def get_users_password(user_email):
    # Use this video guid for refreence: https://www.youtube.com/watch?v=x7SwgcpACng
    cursor.execute(f"SELECT * FROM usersdb.userinfo WHERE email is {user_email}")
    result = (
        cursor.fetchall()
    )  # gets all values from select statement and returns a list of tuples
    try:
        return result.pop(0)  # Return the first password
    except:
        return False  # If Something fails
