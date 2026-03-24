from .base_page import BasePage


class CheckoutPage(BasePage):
    def checkout_heading_locator(self):
        return self.page.get_by_role("heading", name="Checkout")
