import pytest
from tests.e2e.pages.contact_page import ContactPage
from playwright.sync_api import expect


@pytest.mark.e2e
def test_submit_contact_form(page):
    contact_page = ContactPage(page)
    contact_page.open()

    contact_page.submit_form(
        name="Test User",
        email="test@test.com",
        subject="Test Subject",
        message="This is a test message"
    )

    expect(page.locator("div.status.alert-success")).to_be_visible()
