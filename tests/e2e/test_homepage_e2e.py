import pytest
from .pages.home_page import HomePage


@pytest.mark.e2e
def test_homepage_title_and_products(page):
    home_page = HomePage(page)

    # Assert title contains site name
    assert "Automation Exercise" in home_page.title()

    # Click Products and assert we reach the products list
    home_page.open_products()

    # Products page usually has "All Products" or product list; wait for a product card
    assert page.locator("text=All Products").first.is_visible() or page.locator(
        "div.product-overlay").first.is_visible()
