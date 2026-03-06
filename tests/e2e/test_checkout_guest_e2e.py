import pytest
from playwright.sync_api import expect
from tests.e2e.pages.products_page import ProductsPage


# TODO: Update it to use the cart page
@pytest.mark.e2e
def test_guest_can_reach_checkout(page):
    products = ProductsPage(page)
    products.open()

    page.hover(".product-image-wrapper")
    page.click("text=Add to cart")
    page.click("text=View Cart")

    page.click("text=Proceed To Checkout")

    expect(page.get_by_role("heading", name="Checkout")).to_be_visible()
