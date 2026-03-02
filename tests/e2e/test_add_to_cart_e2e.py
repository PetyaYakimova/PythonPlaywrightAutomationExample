import pytest
from tests.e2e.pages.products_page import ProductsPage
from tests.e2e.pages.cart_page import CartPage
from playwright.sync_api import expect


@pytest.mark.e2e
def test_add_product_to_cart(page):
    products = ProductsPage(page)
    products.open()

    # Hover first product and click "Add to cart"
    page.hover(".product-image-wrapper")
    page.click("text=Add to cart")

    # Click View Cart in modal
    page.click("text=View Cart")

    cart = CartPage(page)
    assert cart.has_items()


@pytest.mark.e2e
def test_remove_product_from_cart(page):
    products = ProductsPage(page)
    products.open()

    products.add_first_product_to_cart()
    page.click("text=View Cart")

    cart = CartPage(page)

    # Remove first item
    cart.remove_first_item()

    # Assert cart empty
    expect(page.locator(".cart_product")).to_have_count(0)
