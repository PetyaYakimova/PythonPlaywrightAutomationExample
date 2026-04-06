import os
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def base_UI_URL(self):
        return os.getenv("BASE_UI_URL")

    def click(self, selector):
        self.page.locator(selector).click()

    def fill(self, selector, text):
        self.page.locator(selector).fill(text)

    def is_visible(self, selector):
        return self.page.locator(selector).is_visible()

    def status_alert_success_locator(self):
        return self.page.locator("div.status.alert-success")

    def logged_in_message_locator(self):
        return self.page.locator("text=Logged in as")
