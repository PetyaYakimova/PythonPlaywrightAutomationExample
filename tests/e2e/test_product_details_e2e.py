import pytest


@pytest.mark.e2e
def test_open_product_details(page):
    page.goto("https://automationexercise.com/products")

    # Click first product "View Product"
    page.click("text=View Product")

    # Assert product details visible
    assert page.locator("text=Availability").is_visible()
    assert page.locator("text=Condition").is_visible()
    assert page.locator("text=Brand").is_visible()
