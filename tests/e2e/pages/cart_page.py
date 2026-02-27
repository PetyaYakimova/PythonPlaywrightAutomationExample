from .base_page import BasePage


class CartPage(BasePage):
    def open(self):
        self.page.goto("https://automationexercise.com/view_cart")

    def remove_first_item(self):
        return self.page.click(".cart_quantity_delete")

    def has_items(self):
        return self.page.locator(".cart_product").count() > 0

    def proceed_to_checkout(self):
        self.click("text=Proceed To Checkout")
