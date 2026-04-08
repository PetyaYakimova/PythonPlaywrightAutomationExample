import pytest
from playwright.sync_api import expect
from tests.e2e.pages.products_page import ProductsPage


@pytest.mark.e2e
def test_search_product(page):
    keyword = 'Top'

    products_page = ProductsPage(page)
    products_page.open()

    products_page.search(keyword)

    expect(products_page.get_first_product_description_locator()).to_contain_text(keyword)
