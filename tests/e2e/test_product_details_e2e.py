import time
import pytest
from playwright.sync_api import expect


@pytest.mark.e2e
def test_open_product_details(page):
    page.goto("https://automationexercise.com/products")

    # Click first "View Product" link safely
    page.locator("a[href*='/product_details/']").first.click()

    # Wait until URL changes
    expect(page).to_have_url(lambda url: "/product_details/" in url)

    # Assert product details visible
    expect(page.locator(".product-information")).to_be_visible()
    expect(page.locator("text=Availability")).to_be_visible()
    expect(page.locator("text=Condition")).to_be_visible()
    expect(page.locator("text=Brand")).to_be_visible()
