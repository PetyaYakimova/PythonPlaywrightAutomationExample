import pytest


@pytest.mark.e2e
def test_filter_by_category(page):
    page.goto("https://automationexercise.com/products")

    page.click("text=Women")
    page.click("text=Dress")

    assert page.locator(".product-image-wrapper").count() > 0
