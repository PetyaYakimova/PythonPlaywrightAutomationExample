from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def title(self):
        return self.page.title()

    def open_products(self):
        # there is a "Products" nav link; adjust selector if needed
        self.page.locator("a[href='/products']").click()

    def featured_items_visible(self):
        # The page shows many product cards; check some identifying element
        return self.page.locator("text=Added!").count() >= 0  # page contains product cards
