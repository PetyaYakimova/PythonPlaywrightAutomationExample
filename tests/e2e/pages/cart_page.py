from .base_page import BasePage


class CartPage(BasePage):
    def open(self):
        self.page.goto("https://automationexercise.com/view_cart")

    def has_items(self):
        return self.page.locator(".cart_product").count() > 0
