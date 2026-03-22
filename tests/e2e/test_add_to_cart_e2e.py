import pytest
from tests.e2e.pages.products_page import ProductsPage
from tests.e2e.pages.cart_page import CartPage
from playwright.sync_api import expect


@pytest.mark.e2e
def test_add_product_to_cart(page):
    products_page = ProductsPage(page)
    products_page.open()

    products_page.add_first_product_to_cart()
    products_page.view_cart()

    cart_page = CartPage(page)
    assert cart_page.has_items()


@pytest.mark.e2e
def test_remove_product_from_cart(page):
    products_page = ProductsPage(page)
    products_page.open()

    products_page.add_first_product_to_cart()
    products_page.view_cart()

    cart_page = CartPage(page)

    # Remove first item
    cart_page.remove_first_item()

    # Assert cart empty
    expect(page.locator(".cart_product")).to_have_count(0)
