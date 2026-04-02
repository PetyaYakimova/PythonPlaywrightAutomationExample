import pytest
from playwright.sync_api import expect
from tests.e2e.pages.products_page import ProductsPage


@pytest.mark.e2e
def test_search_product(page):
    products_page = ProductsPage(page)
    products_page.open()

    products_page.search("Top")

    assert products_page.results_visible()
