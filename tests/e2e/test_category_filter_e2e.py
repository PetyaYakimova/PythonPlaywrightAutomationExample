import pytest
from tests.e2e.pages.products_page import ProductsPage


@pytest.mark.e2e
def test_filter_by_category(page):
    products = ProductsPage(page)
    products.open()

    page.click("text=Women")
    page.click("text=Dress")

    assert page.locator(".product-image-wrapper").count() > 0
