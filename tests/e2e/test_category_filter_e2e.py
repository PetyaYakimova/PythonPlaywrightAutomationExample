import pytest
from tests.e2e.pages.products_page import ProductsPage


@pytest.mark.e2e
def test_filter_by_category(page):
    products = ProductsPage(page)
    products.open()

    products.click_filter("Women")
    products.click_filter("Dress")

    assert products.results_visible()
