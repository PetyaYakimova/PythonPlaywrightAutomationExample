import time
import pytest
from playwright.sync_api import expect


@pytest.mark.e2e
def test_open_product_details(page):
    page.goto("https://automationexercise.com/products")

    # Click first "View Product" link safely
    page.locator("a[href*='/product_details/']").first.click()

    # Assert product details visible - need to fix this the first assertion doesn't pass
    assert page.locator("text=Availability").is_visible()
    assert page.locator("text=Condition").is_visible()
    assert page.locator("text=Brand").is_visible()
