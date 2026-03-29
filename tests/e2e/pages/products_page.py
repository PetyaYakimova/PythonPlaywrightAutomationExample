from .base_page import BasePage


class ProductsPage(BasePage):
    def open(self):
        self.page.goto("https://automationexercise.com/products")

    def search(self, text):
        self.fill("#search_product", text)
        self.click("#submit_search")

    def results_visible(self):
        return self.page.locator(".product-image-wrapper").count() > 0

    def product_description_locator(self):
        return self.page.locator("div.productinfo > p")

    def click_first_view_product(self):
        return self.page.locator("a[href*='/product_details/']").first.click()

    def add_first_product_to_cart(self):
        self.page.hover(".product-image-wrapper")
        self.page.click("text=Add to cart")

    def view_cart(self):
        self.page.click("text=View Cart")

    def click_filter(self, filter_name):
        self.page.click(f"text={filter_name}")
