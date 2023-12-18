"""This test_ui.py file will hold all of the UI tests for this application"""
import random
import string
from playwright.sync_api import Page, expect


# Update these tests as the project gets more defined
def test_login_existing_user_ui(page: Page):
    """This test will login in an existing user and confirm the console log shows "Hooray"""
    console_logs = []
    page.goto("http://localhost:4200/")
    page.locator('input[name="username-input"]').click()
    page.locator('input[name="username-input"]').fill("JohnDoe123")
    page.locator('input[name="password"]').click()
    page.locator('input[name="password"]').fill("password123")
    page.get_by_role("button", name="Sign In!").click()
    page.on(
        "console", lambda console_message: console_logs.append(console_message.text())
    )
    assert ("Hooray" in log for log in console_logs)


# Update these tests as the project gets more defined
def test_login_non_existent_user_ui(page: Page):
    """This test will login in an non-existent user and check console log shows "Boo" """
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    console_logs = []
    page.goto("http://localhost:4200/")
    page.locator('input[name="username-input"]').click()
    page.locator('input[name="username-input"]').fill(random_string)
    page.locator('input[name="password"]').click()
    page.locator('input[name="password"]').fill(random_string)
    page.get_by_role("button", name="Sign In!").click()
    page.on(
        "console", lambda console_message: console_logs.append(console_message.text())
    )
    assert ("Boo" in log for log in console_logs)


def test_create_new_user():
    """This test will confirm that a new user is created"""
    return ""


def test_user_already_exists():
    """This test will confirm that a user already exists when it is trying to be created"""
