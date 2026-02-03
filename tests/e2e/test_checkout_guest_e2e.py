import pytest


#TODO: Update it to use the cart page
@pytest.mark.e2e
def test_guest_can_reach_checkout(page):
    page.goto("https://automationexercise.com/products")

    page.hover(".product-image-wrapper")
    page.click("text=Add to cart")
    page.click("text=View Cart")

    page.click("text=Proceed To Checkout")

    assert page.locator("text=Checkout").is_visible()
