"""This test_ui.py file will hold all of the UI tests for this application"""
import random
import string
from faker import Faker
from playwright.sync_api import Page, expect

fake = Faker()
Faker.seed(random.random())


# Update this test when injury form page is created
def test_login_existing_user_ui(page: Page):
    """This test will login in an existing user and confirm the console log shows "Hooray"""
    page.goto("http://localhost:4200/")
    page.locator('input[name="username-input"]').click()
    page.locator('input[name="username-input"]').fill("JohnDoe123")
    page.locator('input[name="username-input"]').press("Tab")
    page.locator('input[name="password"]').fill("password123")
    page.get_by_role("button", name="Sign In!").click()
    assert (
        page.url == "http://localhost:4200/patient-outcome-reported-measure"
    )  # change url to injury forms page


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
    """This test will create a new random user"""
    page.goto("http://localhost:4200/")
    page.get_by_role("button", name="New User").first.click()
    page.wait_for_url("http://localhost:4200/sign/up")
    page.locator('app-sign-up-page input[name="username-input"]').click()
    page.locator('app-sign-up-page input[name="username-input"]').fill(fake.user_name())
    page.locator('app-sign-up-page input[name="username-input"]').press("Tab")
    page.locator('app-sign-up-page input[name="password"]').fill(fake.password())
    page.locator('app-sign-up-page input[name="password"]').press("Tab")
    page.locator('input[name="email"]').fill(fake.email())
    page.locator('input[name="email"]').press("Tab")
    page.locator('input[name="name"]').fill(fake.name())
    page.get_by_role("button", name="Create Account!").click()
    page.wait_for_url("http://localhost:4200/patient-outcome-reported-measure")
    assert (
        page.url == "http://localhost:4200/patient-outcome-reported-measure"
    )  # change to url of form page


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


# Update tests as more features are created
def test_download_patient_form_ui(page: Page):
    """This test will test download feature of a pdf in the table"""
    test_login_existing_user_ui(page)
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Hello").click()
    download = download_info.value
    assert download is not None

# Update tests as moer features are created
def test_email_sending_ui(page:Page):
    test_login_existing_user_ui(page)
    test_download_patient_form_ui(page)
    page.get_by_role("button", name="Next Page!").click()
    page.get_by_placeholder("Your Email").click()
    page.get_by_placeholder("Your Email").fill(fake.email())
    page.get_by_placeholder("Your Atletic Trainer Email").click()
    page.get_by_placeholder("Your Atletic Trainer Email").fill("studentInjuryTest@outlook.com")
    page.locator("input[name=\"form-upload\"]").click()
    page.locator("input[name=\"form-upload\"]").set_input_files("DashExample.png")
    page.get_by_role("button", name="Submit!").click()
    expect(page.get_by_text("Email Sent!")).to_be_visible()
