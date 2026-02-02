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

    def start_signup(self, name, email):
        self.fill("input[data-qa='signup-name']", name)
        self.fill("input[data-qa='signup-email']", email)
        self.click("button[data-qa='signup-button']")

    def complete_signup(self, password):
        self.fill("input[data-qa='password']", password)
        self.click("button[data-qa='create-account']")

    def success_message_visible(self):
        return self.is_visible("text=Account Created!")
