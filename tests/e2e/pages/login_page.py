from .base_page import BasePage


class LoginPage(BasePage):
    def open(self):
        self.page.goto("https://automationexercise.com/login")

    def login(self, email, password):
        self.fill("input[data-qa='login-email']", email)
        self.fill("input[data-qa='login-password']", password)
        self.click("button[data-qa='login-button']")

    def error_visible(self):
        return self.is_visible("text=Your email or password is incorrect!")
