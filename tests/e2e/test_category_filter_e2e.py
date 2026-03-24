import pytest
from tests.e2e.pages.products_page import ProductsPage


@pytest.mark.e2e
def test_filter_by_category(page):
    products_page = ProductsPage(page)
    products_page.open()

    products_page.click_filter("Women")
    products_page.click_filter("Dress")

    assert products_page.results_visible()
