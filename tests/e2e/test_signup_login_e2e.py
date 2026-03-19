import pytest
from tests.e2e.pages.login_page import LoginPage
from utils.test_data import user_data
from playwright.sync_api import expect


@pytest.mark.e2e
def test_user_can_signup_and_login(page):
    data = user_data()

    login_page = LoginPage(page)
    login_page.open()

    login_page.start_signup(data)
    login_page.complete_signup(data)

    expect(login_page.account_created_message_locator()).to_be_visible()

    login_page.click_continue_button()
    expect(page.locator("text=Logged in as")).to_be_visible()


@pytest.mark.e2e
def test_login_with_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login("wrong@test.com", "wrongpass")

    assert login_page.error_visible()
