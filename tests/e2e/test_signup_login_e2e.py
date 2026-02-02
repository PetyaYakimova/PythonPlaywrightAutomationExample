import pytest
from tests.e2e.pages.auth_page import AuthPage
from tests.e2e.pages.login_page import LoginPage
from utils.test_data import user_data


@pytest.mark.e2e
def test_user_can_signup_and_login(page):
    data = user_data()

    auth = AuthPage(page)
    auth.open()

    auth.start_signup(data["name"], data["email"])
    auth.complete_signup(data["password"])

    assert auth.success_message_visible()


@pytest.mark.e2e
def test_login_with_invalid_credentials(page):
    login = LoginPage(page)
    login.open()

    login.login("wrong@test.com", "wrongpass")

    assert login.error_visible()
