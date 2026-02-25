import pytest
import re
from playwright.sync_api import expect


@pytest.mark.e2e
def test_open_product_details(page):
    page.goto("https://automationexercise.com/products")

    # Click first "View Product" link safely
    page.locator("a[href*='/product_details/']").first.click()

    # Wait for correct navigation
    expect(page).to_have_url(re.compile(r".*/product_details/.*"))

    # Assert product details visible
    product_info = page.locator(".product-information")

    expect(product_info).to_contain_text("Availability")
    expect(product_info).to_contain_text("Condition")
    expect(product_info).to_contain_text("Brand")
