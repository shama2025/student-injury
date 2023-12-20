"""This test_api.py file will hold all of the api tests for this application"""
import pytest
import random
import string
from faker import Faker
from app import app

fake = Faker()
Faker.seed(random.randint(0, 300))


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_login_existing_user_api(client):
    """This test will confirm the existing users login information is correct using the api"""
    response = client.get("/api/login?username=JohnDoe123&password=password123")
    assert response.status_code == 200


def test_login_non_existent_user_api(client):
    """This test will confirm the non-existent users login information is incorrect using the api"""
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    response = client.get(
        f"/api/login?username={random_string}&password={random_string}"
    )
    assert response.status_code == 404


def test_create_new_user(client):
    """This test will confirm that the new user was created"""
    response = client.get(
        f"/api/new/account?username={fake.user_name()}&password={fake.password()}&email={fake.email()}&name={fake.name()}"
    )
    assert response.status_code == 200


def test_create_existing_user(client):
    """This test will confirm that a user already exists when it was being created"""
    response = client.get(
        "/api/new/account?username=JohnDoe123&password=password123&email=JohnDoe@test.com&name=John Doe"
    )
    assert response.status_code == 404
