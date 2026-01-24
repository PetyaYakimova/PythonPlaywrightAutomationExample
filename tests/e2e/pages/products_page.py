from .base_page import BasePage


class ProductsPage(BasePage):
    def open(self):
        self.page.goto("https://automationexercise.com/products")

    def search(self, text):
        self.fill("#search_product", text)
        self.click("#submit_search")

    def results_visible(self):
        return self.page.locator(".product-image-wrapper").count() > 0
