import pytest
from tests.e2e.pages.login_page import LoginPage


@pytest.mark.e2e
def test_login_with_invalid_credentials(page):
    login = LoginPage(page)
    login.open()

    login.login("wrong@test.com", "wrongpass")

    assert login.error_visible()
