import pytest
from playwright.sync_api import expect
from tests.e2e.pages.products_page import ProductsPage
from tests.e2e.pages.cart_page import CartPage


# TODO: Update it to use the cart page
@pytest.mark.e2e
def test_guest_can_reach_checkout(page):
    products = ProductsPage(page)
    products.open()

    products.add_first_product_to_cart()
    products.view_cart()

    cartPage = CartPage(page)
    page.click("text=Proceed To Checkout")

    expect(page.get_by_role("heading", name="Checkout")).to_be_visible()
