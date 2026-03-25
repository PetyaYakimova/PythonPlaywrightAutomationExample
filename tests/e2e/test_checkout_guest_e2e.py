import pytest
from playwright.sync_api import expect
from tests.e2e.pages.products_page import ProductsPage
from tests.e2e.pages.cart_page import CartPage
from tests.e2e.pages.checkout_page import CheckoutPage


@pytest.mark.e2e
def test_guest_can_reach_checkout(page):
    products_page = ProductsPage(page)
    products_page.open()

    products_page.add_first_product_to_cart()
    products_page.view_cart()

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    expect(checkout_page.checkout_heading_locator()).to_be_visible()
