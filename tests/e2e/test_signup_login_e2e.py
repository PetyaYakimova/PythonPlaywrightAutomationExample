import pytest
from tests.e2e.pages.login_page import LoginPage
from utils.test_data import user_data


@pytest.mark.e2e
def test_user_can_signup_and_login(page):
    data = user_data()

    login = LoginPage(page)
    login.open()

    login.start_signup(data["name"], data["email"])
    login.complete_signup(data["password"])

    assert login.success_message_visible()


@pytest.mark.e2e
def test_login_with_invalid_credentials(page):
    login = LoginPage(page)
    login.open()

    login.login("wrong@test.com", "wrongpass")

    assert login.error_visible()
