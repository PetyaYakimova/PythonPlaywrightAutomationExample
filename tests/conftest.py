import os
import pytest
from playwright.sync_api import sync_playwright

BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


# Optional fixture showing how to provide Playwright's "page" using pytest-playwright
# If you installed pytest-playwright, you can just use the 'page' fixture from the plugin
# but here's a helper if you want manual control:
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p
