import json
import pytest
from playwright.sync_api import sync_playwright

# Load test data from JSON file
with open('test_data.json', 'r') as file:
    testdata = json.load(file)


@pytest.mark.parametrize("credentials", testdata)
def test_login_with_json(credentials):
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