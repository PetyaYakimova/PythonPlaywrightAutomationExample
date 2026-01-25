import pytest
from tests.e2e.pages.products_page import ProductsPage


@pytest.mark.e2e
def test_search_product(page):
    products = ProductsPage(page)
    products.open()

    products.search("Top")

    assert products.results_visible()
