from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, selector):
        self.page.locator(selector).click()

    def fill(self, selector, text):
        self.page.locator(selector).fill(text)

    def is_visible(self, selector):
        return self.page.locator(selector).is_visible()

    def status_alert_success_locator(self):
        return self.page.locator("div.status.alert-success")
