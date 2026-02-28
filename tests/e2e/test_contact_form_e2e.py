import time

import pytest
from tests.e2e.pages.contact_page import ContactPage
from playwright.sync_api import expect


@pytest.mark.e2e
def test_submit_contact_form(page):
    contact = ContactPage(page)
    contact.open()

    contact.submit_form(
        name="Test User",
        email="test@test.com",
        subject="Test Subject",
        message="This is a test message"
    )

    expect(page.locator("div.status.alert-success")).to_be_visible()
    # assert contact.success_visible()
