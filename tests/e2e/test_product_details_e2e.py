import pytest
import re
from playwright.sync_api import expect
from tests.e2e.pages.products_page import ProductsPage


@pytest.mark.e2e
def test_open_product_details(page):
    products_page = ProductsPage(page)
    products_page.open()

    # Click first "View Product" link safely
    page.locator("a[href*='/product_details/']").first.click()
    close_google_vignette_if_present(page)

    # Wait for correct navigation
    expect(page).to_have_url(re.compile(r".*/product_details/.*"))

    # Assert product details visible
    product_info = page.locator(".product-information")

    expect(product_info).to_contain_text("Availability")
    expect(product_info).to_contain_text("Condition")
    expect(product_info).to_contain_text("Brand")


def close_google_vignette_if_present(page):
    if "#google_vignette" in page.url:
        page.goto(page.url.split("#")[0])
