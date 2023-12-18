"""This test_ui.py file will hold all of the UI tests for this application"""
import random
import string
from faker import Faker
from playwright.sync_api import Page, expect

fake = Faker()
Faker.seed(42)


# Update this test when injury form page is created
def test_login_existing_user_ui(page: Page):
    """This test will login in an existing user and confirm the console log shows "Hooray"""
    page.goto("http://localhost:4200/")
    page.locator('input[name="username-input"]').click()
    page.locator('input[name="username-input"]').fill("JohnDoe123")
    page.locator('input[name="password"]').click()
    page.locator('input[name="password"]').fill("password123")
    page.get_by_role("button", name="Sign In!").click()
    # expect(page.url == "")#change url to injury forms page


# Update this test when injury form page is created
def test_login_non_existent_user_ui(page: Page):
    """This test will login in an non-existent user and check console log shows "Boo" """
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    page.goto("http://localhost:4200/")
    page.locator('app-login-page input[name="username-input"]').click()
    page.locator('app-login-page input[name="username-input"]').fill(random_string)
    page.locator('app-login-page input[name="password"]').click()
    page.locator('app-login-page input[name="password"]').fill(random_string)
    page.get_by_role("button", name="Sign In!").click()
    # expect warning to be on login page


# Update this test when injury form page is created
def test_create_new_user(page: Page):
    page.goto("http://localhost:4200/")
    page.get_by_role("button", name="New User").first.click()
    page.locator('app-sign-up-page input[name="username-input"]').click()
    page.locator('app-sign-up-page input[name="username-input"]').fill(fake.user_name())
    page.locator('app-sign-up-page input[name="username-input"]').press("Tab")
    page.locator('app-sign-up-page input[name="password"]').fill(fake.password())
    page.locator('app-sign-up-page input[name="password"]').press("Tab")
    page.locator('input[name="email"]').fill(fake.email())
    page.locator('input[name="email"]').press("Tab")
    page.locator('input[name="name"]').fill(fake.name())
    page.get_by_role("button", name="Create Account!").click()
    # expect(page.url == "") #change to url of form page


# Update this test when injury form page is created
def test_user_already_exists(page: Page):
    """This test will confirm that a user already exists when it is trying to be created"""
    page.goto("http://localhost:4200/")
    page.get_by_role("button", name="New User").first.click()
    page.locator('app-sign-up-page input[name="username-input"]').click()
    page.locator('app-sign-up-page input[name="username-input"]').fill("JohnDoe123")
    page.locator('app-sign-up-page input[name="username-input"]').press("Tab")
    page.locator('app-sign-up-page input[name="password"]').fill("password123")
    page.locator('app-sign-up-page input[name="password"]').press("Tab")
    page.locator('input[name="email"]').fill("JohnDoe@test.com")
    page.locator('input[name="email"]').press("Tab")
    page.locator('input[name="name"]').fill("John Doe")
    page.get_by_role("button", name="Create Account!").click()
    # Expect error to appear on screen
