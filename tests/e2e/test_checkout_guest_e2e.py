import pytest
from playwright.sync_api import expect


# TODO: Update it to use the cart page
@pytest.mark.e2e
def test_guest_can_reach_checkout(page):
    page.goto("https://automationexercise.com/products")

    page.hover(".product-image-wrapper")
    page.click("text=Add to cart")
    page.click("text=View Cart")

    page.click("text=Proceed To Checkout")

    expect(page.get_by_role("heading", name="Checkout")).to_be_visible()
