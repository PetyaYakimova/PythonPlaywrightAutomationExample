import os
import pytest
from utils.api_client import ApiClient
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def api_base_url():
    return os.getenv("BASE_API_URL")


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_UI_URL")


@pytest.fixture(scope="session")
def api_client(api_base_url):
    return ApiClient(api_base_url)


@pytest.fixture(scope="function")
def page(context, base_url):
    """
    Custom page fixture that automatically accepts cookies
    """
    page = context.new_page()
    page.goto(base_url)

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
