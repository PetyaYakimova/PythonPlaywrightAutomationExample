from .base_page import BasePage


class CartPage(BasePage):
    def open(self):
        # self.page.goto("https://automationexercise.com/view_cart")
        self.page.goto(f"{super.base_UI_URL()}/view_cart")

    def remove_first_item(self):
        return self.page.click(".cart_quantity_delete")

    def item_in_cart_locator(self):
        return self.page.locator(".cart_product")

    def has_items(self):
        return self.item_in_cart_locator().count() > 0

    def proceed_to_checkout(self):
        self.click("text=Proceed To Checkout")
