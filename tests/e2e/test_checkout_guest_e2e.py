import pytest
from playwright.sync_api import expect
from tests.e2e.pages.products_page import ProductsPage
from tests.e2e.pages.cart_page import CartPage


@pytest.mark.e2e
def test_guest_can_reach_checkout(page):
    products_page = ProductsPage(page)
    products_page.open()

    products_page.add_first_product_to_cart()
    products_page.view_cart()

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    expect(page.get_by_role("heading", name="Checkout")).to_be_visible()
