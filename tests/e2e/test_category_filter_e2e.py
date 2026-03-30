import pytest
from playwright.sync_api import expect
from tests.e2e.pages.products_page import ProductsPage


@pytest.mark.e2e
def test_filter_by_category(page):
    products_page = ProductsPage(page)
    products_page.open()

    products_page.click_filter("Women")
    products_page.click_filter("Dress")

    expect(products_page.get_first_product_description_locator()).to_contain_text('Dress')
