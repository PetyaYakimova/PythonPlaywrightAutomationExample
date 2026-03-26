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
def page(base_url):
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()

        # 🚫 Block ad-related requests
        context.route("**/*googlesyndication.com/**", lambda route: route.abort())
        context.route("**/*doubleclick.net/**", lambda route: route.abort())
        context.route("**/*googleadservices.com/**", lambda route: route.abort())

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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")
