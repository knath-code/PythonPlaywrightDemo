import pytest
from playwright.sync_api import sync_playwright

# Test data
testdata = [
    {"username": "standard_user", "password": "secret_sauce"},
    {"username": "locked_out_user", "password": "secret_sauce"},
    # Add more test data as needed
]


@pytest.mark.parametrize("credentials", testdata)
def test_login(credentials):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()

        # Open a new page
        page = context.new_page()

        # Navigate to the login page
        page.goto('https://www.saucedemo.com/v1/')

        # Perform login with test data

        page.fill('id=user-name', credentials["username"])
        page.fill('id=password', credentials["password"])
        page.click('id=login-button')

        # Validate login success
        assert page.title() == 'Swag Labs'

        # Close the browser
        browser.close()