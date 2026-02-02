from .base_page import BasePage


#Move to login page
class AuthPage(BasePage):
    def open(self):
        self.page.goto("https://automationexercise.com/login")

    def start_signup(self, name, email):
        self.fill("input[data-qa='signup-name']", name)
        self.fill("input[data-qa='signup-email']", email)
        self.click("button[data-qa='signup-button']")

    def complete_signup(self, password):
        self.fill("input[data-qa='password']", password)
        self.click("button[data-qa='create-account']")

    def success_message_visible(self):
        return self.is_visible("text=Account Created!")
