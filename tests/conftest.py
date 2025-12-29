import os
import pytest

BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")


@pytest.fixture(scope="function")
def page(context):
    """
    Custom page fixture that automatically accepts cookies
    """
    page = context.new_page()
    page.goto(BASE_URL)

    # Handle cookie consent if present
    try:
        consent_button = page.get_by_role("button", name="Consent")
        if consent_button.is_visible():
            consent_button.click()
    except Exception:
        # If the banner doesn't appear, continue silently
        pass

    yield page
    page.close()


@pytest.fixture(scope="session")
def api_base_url():
    return "https://automationexercise.com/api"
