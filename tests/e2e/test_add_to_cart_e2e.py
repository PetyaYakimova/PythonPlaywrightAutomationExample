import pytest
from tests.e2e.pages.products_page import ProductsPage
from tests.e2e.pages.cart_page import CartPage


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
    page.goto("https://automationexercise.com/products")

    page.hover(".product-image-wrapper")
    page.click("text=Add to cart")
    page.click("text=View Cart")

    cart = CartPage(page)

    # Remove first item
    page.click(".cart_quantity_delete")

    # Assert cart empty
    assert page.locator("text=Cart is empty").is_visible()
